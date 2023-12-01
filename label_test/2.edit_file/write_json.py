import json

# 创建一个示例字典
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 将字典写入 JSON 文件
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

print("字典已写入data.json")
