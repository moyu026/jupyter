import cv2

# 读取原始视频
input_video_path = 'F:\PythonWork\dataset\electrical_cabinet_test/button.mp4'
cap = cv2.VideoCapture(input_video_path)

if not cap.isOpened():
    print("无法打开输入视频文件。")
    exit()

# 获取原始视频的信息
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = int(cap.get(5))

# 创建输出视频写入器
output_video_path = 'F:\PythonWork\dataset\electrical_cabinet_test/output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (frame_width, frame_height))

if not out.isOpened():
    print("无法创建输出视频文件。")
    exit()

# 重复播放20次
repeats = 200
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    for _ in range(repeats):
        out.write(frame)
        frame_count += 1

cap.release()
out.release()

print(f"成功创建新视频文件 '{output_video_path}'，其中包含 {frame_count} 帧。")
