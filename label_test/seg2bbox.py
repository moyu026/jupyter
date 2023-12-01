
# 把segment-anythin中目标的bbox信息画出来
import json
import cv2

def get_point(file_path):
    button_dict = {}
    yaban_dict = {}
    with open(file_path, 'r') as load_f:
        json_dict = json.load(load_f)
        for obj_dict in json_dict['objects']:
            # print(obj_dict['category'])

            if obj_dict['category'].split('_')[-1] == '压板':
                yaban_dict[obj_dict['category'].split('_')[-2]] = obj_dict['bbox']
            if obj_dict['category'].split('_')[-1] == '旋钮':
                button_dict[obj_dict['category'].split('_')[-2]] = obj_dict['bbox']

    return button_dict, yaban_dict
                    # print(obj_dict['bbox'])
#             xmin, ymin, xmax, ymax = obj_dict['bbox'][0], obj_dict['bbox'][1], obj_dict['bbox'][2], obj_dict['bbox'][3]
#             cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), thickness=2)
#             print(xmin, ymin, xmax, ymax)
# #         print(obj_dict['bbox'])
# #         xmin, ymin, xmax, ymax = obj_dict['bbox'][0], obj_dict['bbox'][1], obj_dict['bbox'][2], obj_dict['bbox'][3]
# #         cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), thickness=2)
# #         print(xmin, ymin, xmax, ymax)
# #
# cv2.imwrite('file/bbx10.jpg', img)


path = 'file/1-1.json'
img_path = 'file/1-1.jpg'
button_dict, yaban_dict = get_point(path)
print(button_dict)

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(button_dict, json_file, ensure_ascii=False)

# img = cv2.imread(img_path)
# for button_name in button_dict:
#     button_point = button_dict[button_name]
#     xmin, ymin, xmax, ymax = int(button_point[0]), int(button_point[1]), int(button_point[2]), int(button_point[3])
#     button_img = img[ymin:ymax, xmin:xmax]
#     cv2.imshow('button', button_img)
#     cv2.waitKey()
#     print(button_point)
#     print(xmin)

