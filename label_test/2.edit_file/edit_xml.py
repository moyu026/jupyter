# 编辑xml文件内容

import xml.etree.ElementTree as ET
import codecs

# 打开XML文件并指定编码方式
with codecs.open("file/1653467639.65203.xml", "r", encoding="utf-8") as file:
    xml_content = file.read()

# 解析XML内容为ElementTree对象
root = ET.fromstring(xml_content)

# 找到所有名为 "element1" 的元素
elements_to_modify = root.findall(".//name")


# 遍历所有匹配的元素并输出其内容
for element in elements_to_modify:
    if element.text == '红色_矩形':
        new_content = "red_rectangle"
    if element.text == '粉色_矩形':
        new_content = "pink_retangle"

    element.text = new_content
    # print(element.text)

# 将修改后的XML写回文件
tree = ET.ElementTree(root)
tree.write("example.xml", encoding="utf-8")
