import cv2
import asyncio

camera_indexes = []
for i in range(10):
    print(f"Checking camera {i}")
    cap = cv2.VideoCapture(i)
    print(f"Camera {i} initialized")
    if cap.isOpened():
        print(f"Camera {i} detected")
        camera_indexes.append(i)
        cap.release()

# 摄像头索引列表
indexes = camera_indexes
# indexes = [0] # 正常
# indexes = [1] # 正常


async def show_camera(index: int):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Camera {index} not found")
        return
    ret, frame = cap.read()
    if not ret:
        print(f"Camera {index} read failed")
    else:
        print(f"Camera {index}: {frame.shape} {cap.getBackendName()}")

    while True:
        # await asyncio.sleep(0)
        ret, frame = await asyncio.to_thread(cap.read)

        name = f"Camera {index}: {None if frame is None else frame.shape} {cap.getBackendName()}"

        cv2.imshow(name, frame)
        if (cv2.waitKey(1) & 0xFF == ord("q")) or cv2.getWindowProperty(
            name, cv2.WND_PROP_VISIBLE
        ) < 1:
            break

    print(f"Camera {index} released")
    cap.release()
    cv2.destroyWindow(name)


async def main():
    tasks = [asyncio.create_task(show_camera(index)) for index in indexes]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

    cv2.destroyAllWindows()
