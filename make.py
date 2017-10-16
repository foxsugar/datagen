# coding:gbk
import configparser
import os
import sys
import codecs
import xlrd
import python_out.static_data_proto_pb2
import importlib,sys

importlib.reload(sys)
# sys.setdefaultencoding("utf8")

base_dir = os.getcwd() + os.sep + "%s" + os.sep
in_dir = base_dir % "input"
out_dir = base_dir % "out"
python_out_dir = base_dir % "python_out"
proto_dir = base_dir % "proto"
config_dir = base_dir % "conf" + os.sep + "config.conf"

data_type_map = dict()
data_type_map["int32"] = "int"
data_type_map["float"] = "float"
data_type_map["string"] = "str"


def list_file_names(dir):
    return os.listdir(dir)


def generate_proto():
    print("生成static_data_proto.proto...")
    proto_file = open(proto_dir + "static_data_proto.proto", "w")
    inputs = list_file_names(in_dir)
    msg_manager = list()
    msg_manager.append("syntax = \"proto3\";\n")
    msg_manager.append("option java_package = \"%s\";\n" % get_config("java", "package_name"))
    msg_manager.append("option java_outer_classname = \"%s\";\n" % get_config("java", "class_name"))
    msg_manager.append("option csharp_namespace = \"%s\";\n" % get_config("csharp", "csharp_namespace"))
    msg_manager.append("message DataManager {\n")
    msg_records = list()
    for i, f in enumerate(inputs):
        f_name = f.split(".")[0]
        s = str(f_name)
        attrName = s[0].lower() + s[1:]
        # print(attrName)

        msg_manager.append("\tmap<string,%s> %s = %s;\n" % (f_name, attrName, i + 1))
        msg_records.append("message %s {\n" % f_name)
        wb = xlrd.open_workbook(in_dir + f)
        sheet = wb.sheets()[0]

        msg = "\t"
        index = 1
        for k in range(sheet.ncols):
            data_type = sheet.col_values(k)[2]
            data_name = sheet.col_values(k)[1]
            if sheet.col_values(k)[0] == 3:
                continue
            else:
                msg_records.append("\t%s %s = %s;\n" % (data_type, data_name, index))
                index = index + 1
        msg_records.append("}\n")
    msg_manager.append("}\n")
    msg_manager.extend(msg_records)
    proto_file.write("".join(msg_manager))

    print("完成static_data_proto.proto")


def generate_class(command):
    py_result = os.system(command)
    return py_result


def init(obj, args_build_type, args_names, args_types, arg_values):
    for i, arg in enumerate(args_names):
        if arg_values[i] is None or len(str(arg_values[i])) == 0:
            continue
        t = int(args_build_type[i])
        if t == 3:
            continue
        if t == 0 or build_type == t:
            if hasattr(obj, arg):
                arg_type = str(args_types[i])
                arg_values[i] = str(arg_values[i]).strip()
                if arg_type == "int32":
                    setattr(obj, arg, int(float(arg_values[i])))
                elif arg_type == "float":
                    setattr(obj, arg, float(arg_values[i]))
                elif arg_type.split(" ")[0] == "repeated":
                    string = str(str(arg_values[i]))
                    value = [int(float(x)) for x in string.split(",")]
                    getattr(obj, arg).extend(value)
                elif arg_type[:3] == "map":
                    string = str(str(arg_values[i]))
                    entrys = [str(x) for x in string.split(",")]
                    kv_types = arg_type[4:len(arg_type) - 1]
                    k_type = data_type_map[kv_types.split(",")[0]]
                    v_type = data_type_map[kv_types.split(",")[1]]
                    d = {}
                    for k in range(len(entrys)):
                        entry = entrys[k].split("=")
                        k = eval("%s(%s)" % (k_type, entry[0]))
                        v = eval("%s(%s)" % (v_type, entry[1]))
                        d[k] = v

                    getattr(obj, arg).update(d)
                else:
                    setattr(obj, arg, str(str(arg_values[i])))


def init_data_manager():
    manager = python_out.static_data_proto_pb2.DataManager()
    inputs = os.listdir(in_dir)
    print("数据表数据写入...")
    for i, f in enumerate(inputs):
        print(f)
        wb = xlrd.open_workbook(in_dir + f)
        sheet = wb.sheets()[0]
        for r in range(3, sheet.nrows):
            row = sheet.row_values(r)
            fn = f.split(".")[0]
            attrName = fn[0].lower() + fn[1:]

            # print((" =====attrName = " + attrName))
            attr = getattr(manager, attrName )[str(row[0])]
            init(attr, sheet.row_values(0), sheet.row_values(1), sheet.row_values(2), row)
            # func(getattr(manager, f[:-4] + "Record")[r - 3], row)
    out = open(get_config("build", "out_path") + "/static_data.data", "w")

    msg = manager.SerializeToString()

    print(msg)


    # print msg

    # entityattr2 = python_out.static_data_proto_pb2.DataManager
    # man = entityattr2.ParseFromString(msg)
    # print(man)
    out.write(msg)
    out.close()


def get_config(section, name):
    config = configparser.ConfigParser()
    config.readfp(open(config_dir))
    return config.get(section, name)


def main():
    cmd_base = " --proto_path=" + proto_dir + " " + proto_dir + "*.proto"
    py_cmd = "protoc --python3_out=" + get_config("python", "out_path") + cmd_base
    java_cmd = "protoc --java_out=" + get_config("java", "out_path") + cmd_base
    csharp_cmd = "protoc --csharp_out=" + get_config("csharp", "out_path") + cmd_base

    generate_proto()
    print("  mingling = "+py_cmd)
    generate_class(py_cmd)
    print("生成python文件")
    generate_class(java_cmd)
    print("生成java文件")
    generate_class(csharp_cmd)
    print("生成csharp文件")
    # 0:both 1:client 2:server
    print(("打包类型：%s" % build_type))
    init_data_manager()
    print("打包完成")


build_type = int(get_config("build", "type"))


if __name__ == '__main__':
    main()
