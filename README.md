# StaticDataGenerator
A static data generator written in Python<br>

**目录说明**

1. **conf**<br>存放配置文件，目前可配置java文件输出目录，类名以及所属包名
2. **input**<br>存放配置表文件，格式为.xls
3. **out**<br>存放打包后的数据文件，格式为.data
4. **proto**<br>存放由.xls生成的.proto文件


**数据表结构定义**
<table>
	<tr>
		<td>标志位</td>
      	<td>0:client&server</td>
      	<td>1:client</td>
      	<td>2:server</td>
      	<td>3:comment</td>
	</tr>
	<tr>
     	<td>字段名</td>
      	<td>id</td>
      	<td>name</td>
      	<td>age</td>
      	<td>comment</td>
  	</tr>
	<tr>
		<td>字段类型</td>
      	<td>int32</td>
      	<td>string</td>
      	<td>int32</td>
      	<td>comment</td>
  	</tr>
	<tr>
		<td>数据</td>
      	<td>1</td>
      	<td>tom</td>
      	<td>2</td>
      	<td>comment</td>
  	</tr>
</table>


**使用方法**<br>
首先需要安装python2.7环境，导入各种依赖包（xlrd, protobuf, ConfigParser）设置好**conf**文件夹下的配置文件，将需要打包的配置表放入input目录中，在该目录执行命令python make.py命令即可
