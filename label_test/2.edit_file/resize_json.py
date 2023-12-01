import json

json_path = r'F:\PythonWork\dataset\firedataset\segment\1\label\fire_dp1_1.json'

f = open(json_path, 'r')
content = f.read()
a = json.loads(content)
h, w = a['imageHeight'], a['imageWidth']

print(a)

print(h, w)

for shape_dict in a['shapes']:
    points = shape_dict['points']
    for point in points:
        point[0] = point[0] / w * 640
        point[1] = point[1] / w * 640

with open('test.json', 'w') as f:
    json.dump(a, f, ensure_ascii=False)

    # print(shape_dict)

