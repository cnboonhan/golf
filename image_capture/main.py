import depthai
import cv2

pipeline = depthai.Pipeline()

# Nodes are a building blocks when populating a pipeline
color_camera = pipeline.create(depthai.node.ColorCamera)

# XLink is a node to send data to the host
xout = pipeline.create(depthai.node.XLinkOut)
xout.setStreamName("color")

# Connect color_camera to xout
color_camera.video.link(xout.input)

# Connect to device and start pipeline
with depthai.Device(pipeline) as device:
    q = device.getOutputQueue(name="color", maxSize=4, blocking=False)

    while True:
        in_frame = q.get()
        frame = in_frame.getCvFrame()

        cv2.imshow("Color camera", frame)

        if cv2.waitKey(1) == ord("q"):
            break
cv2.destroyAllWindows()
