from lerobot.common.robot_devices.cameras.opencv import OpenCVCamera, OpenCVCameraConfig
import cv2
from tqdm import tqdm

camera_configs = {
    "top": OpenCVCameraConfig(0, fps=30, width=640, height=480),
    "side": OpenCVCameraConfig(1, fps=30, width=640, height=480),
    "arm": OpenCVCameraConfig(2, fps=30, width=640, height=480),
}

cameras = {name: OpenCVCamera(config) for name, config in camera_configs.items()}
for name, camera in cameras.items():
    print(f"Connecting to camera {name}")
    camera.connect()

    for i in tqdm(range(camera.fps * 30)):
        # image_data = camera.read()
        # # print(f"Read image from camera {name} with shape {image_data.shape}")
        # image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
        ret, color_image = camera.camera.read()
        cv2.imshow(name, color_image)
        if (cv2.waitKey(1) & 0xFF == ord("q")) or cv2.getWindowProperty(
            name, cv2.WND_PROP_VISIBLE
        ) < 1:
            break
    camera.disconnect()
