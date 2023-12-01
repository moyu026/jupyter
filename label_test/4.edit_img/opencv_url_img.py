import cv2
import numpy as np
import urllib.request  # 引入 urllib.request 模块

# 网络图片的URL
image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png"

# 从URL加载图像
resp = urllib.request.urlopen(image_url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)



# 显示图像（可选）
cv2.imshow("Loaded Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

