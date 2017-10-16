# encoding=utf-8
import configparser
import os
import xlrd
import python_out.static_data_proto_pb2
import importlib, sys
import google.protobuf.json_format
import json

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
data_type_map["int64"] = "int"
data_type_map["double"] = "float"
data_type_map["float"] = "float"
data_type_map["string"] = "str"


def list_file_names(dir):
    return os.listdir(dir)


'''
生成proto文件
'''


def generate_proto():
    print("生成static_data_proto.proto...")
    proto_file = open(proto_dir + "static_data_proto.proto", "w")
    inputs = list_file_names(in_dir)
    msg_manager = list()
    msg_manager.append("syntax = \"proto3\";\n")
    msg_manager.append("option java_package = \"%s\";\n" % get_config("java", "package_name"))
    msg_manager.append("option java_outer_classname = \"%s\";\n" % get_config("java", "class_name"))
    msg_manager.append("option csharp_namespace = \"%s\";\n" % get_config("csharp", "csharp_namespace"))
    msg_manager.append("\n")
    msg_manager.append("message DataManager {\n")

    msg_records = list()
    for i, f in enumerate(inputs):
        f_name = f.split(".")[0]
        s = str(f_name)
        attrName = s[0].lower() + s[1:]
        # print(attrName)
        wb = xlrd.open_workbook(in_dir + f)
        sheet = wb.sheets()[0]
        # id的类型
        id_type = str(sheet.col_values(0)[2]).strip()

        msg_manager.append("\tmap<%s,%s> %s = %s;\n" % (id_type, f_name, attrName, i + 1))
        msg_records.append("message %s {\n" % f_name)

        msg = "\t"
        index = 1
        for k in range(sheet.ncols):
            data_type = sheet.col_values(k)[2]
            data_name = sheet.col_values(k)[1]
            # print("index : "+index+"  type : "+data_type)
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


'''
转换基本数据类型
'''


def convert_base_type(attr_type, value):
    if attr_type == "int32":
        return int(float(value))
    elif attr_type == "int64":
        return int(float(value))
    elif attr_type == "double":
        return float(value)
    elif attr_type == "float":
        return float(value)
    elif attr_type == "string":
        return value


'''
转换数据
'''


def convert_by_type(attr_type, value):
    if attr_type.split(" ")[0] == "repeated":
        list_type = attr_type.split(" ")[1]
        ls = []
        for x in value.split(","):
            ls.append(convert_base_type(list_type, x))
        return ls
    elif attr_type[:3] == "map":
        string = value
        entrys = [str(x) for x in string.split(",")]
        kv_types = attr_type[4:len(attr_type) - 1]
        k_type = data_type_map[kv_types.split(",")[0]]
        v_type = data_type_map[kv_types.split(",")[1]]
        mp = {}
        for k in range(len(entrys)):
            entry = entrys[k].split("=")
            k = eval("%s(%s)" % (k_type, entry[0]))
            v = eval("%s(%s)" % (v_type, entry[1]))
            mp[k] = v
        return mp
    else:
        return convert_base_type(attr_type, value)


def init(obj, args_build_type, args_names, args_types, arg_values):
    for i, arg in enumerate(args_names):
        if arg_values[i] is None or len(str(arg_values[i])) == 0:
            continue
        platform = int(float(str(args_build_type[i]).strip()))
        platform_type = int(str(build_type).strip())
        # 都不用
        if platform == 3:
            continue
        # 都使用 或者和定义平台相同
        if platform == 0 or platform_type == platform:
            if hasattr(obj, arg):
                arg_type = str(args_types[i]).strip()
                attr_value = str(arg_values[i]).strip()
                # list 结构
                if arg_type.split(" ")[0] == "repeated":
                    getattr(obj, arg).extend(convert_by_type(arg_type, attr_value))
                elif arg_type[:3] == "map":
                    getattr(obj, arg).update(convert_by_type(arg_type, attr_value))
                else:
                    setattr(obj, arg, convert_by_type(arg_type, attr_value))


'''
将序列化的数据写入文件
'''
def write_data_to_file():
    manager = python_out.static_data_proto_pb2.DataManager()
    inputs = os.listdir(in_dir)
    print("数据表数据写入...")
    for i, f in enumerate(inputs):
        print(f)
        wb = xlrd.open_workbook(in_dir + f)
        sheet = wb.sheets()[0]
        id_type = str(sheet.col_values(0)[2]).strip()
        #真正数据从第三行开始
        for r in range(3, sheet.nrows):
            row = sheet.row_values(r)
            fn = f.split(".")[0]
            data_name = fn[0].lower() + fn[1:]
            id_value = str(row[0]).strip()
            print((" data_name: "+ data_name+"  =====id: " + id_value))
            attr = getattr(manager, data_name)[convert_base_type(id_type, id_value)]
            init(attr, sheet.row_values(0), sheet.row_values(1), sheet.row_values(2), row)
            # func(getattr(manager, f[:-4] + "Record")[r - 3], row)
    out_json = open(get_config("build", "out_path") + "/static_data.json", "w+", encoding="utf-8")
    out_bin = open(get_config("build", "out_path") + "/static_data.data", "wb+")

    msg_bin = manager.SerializeToString()
    msg_json_dict = google.protobuf.json_format.MessageToDict(manager)

    msg_json = json.dumps(msg_json_dict)
    msg_json.encode(encoding='UTF-8', errors='strict')
    print(msg_bin)
    print(msg_json)
    out_json.write(msg_json)
    out_json.close()

    out_bin.write(msg_bin)
    out_bin.close()


def get_config(section, name):
    config = configparser.ConfigParser()
    config.read_file(open(config_dir))
    return config.get(section, name)


def main():
    cmd_base = " --proto_path=" + proto_dir + " " + proto_dir + "*.proto"
    py_cmd = "protoc --python_out=" + get_config("python", "out_path") + cmd_base
    java_cmd = "protoc --java_out=" + get_config("java", "out_path") + cmd_base
    csharp_cmd = "protoc --csharp_out=" + get_config("csharp", "out_path") + cmd_base

    generate_proto()
    print("  mingling = " + py_cmd)
    generate_class(py_cmd)
    print("生成python文件")
    generate_class(java_cmd)
    print("生成java文件")
    generate_class(csharp_cmd)
    print("生成csharp文件")
    # 0:both 1:client 2:server
    print(("打包类型：%s" % build_type))
    write_data_to_file()
    print("打包完成")


build_type = int(get_config("build", "type"))

if __name__ == '__main__':
    main()
    main()
