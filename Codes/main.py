
import depthai as dai
import open3d as o3d
import numpy as np
import time
import gzip
import shutil
from pymavlink import mavutil


CAPTURE_DURATION_SEC = 60
MAVLINK_PORT = '/dev/ttyUSB0'  
MAVLINK_BAUD = 57600
POINTCLOUD_FILE = "map.ply"
COMPRESSED_FILE = "map_compressed.ply.gz"


print("Connecting to MAVLink IMU...")
mav = mavutil.mavlink_connection(MAVLINK_PORT, baud=MAVLINK_BAUD)
mav.wait_heartbeat()
print("✅ MAVLink connected.")


pipeline = dai.Pipeline()

monoLeft = pipeline.createMonoCamera()
monoRight = pipeline.createMonoCamera()
stereo = pipeline.createStereoDepth()

monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)

stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
stereo.setLeftRightCheck(True)

monoLeft.out.link(stereo.left)
monoRight.out.link(stereo.right)

xout = pipeline.createXLinkOut()
xout.setStreamName("depth")
stereo.depth.link(xout.input)


print("🗺️  Starting 3D Mapping...")

with dai.Device(pipeline) as device:
    depthQueue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)
    all_points = []
    start = time.time()

    while time.time() - start < CAPTURE_DURATION_SEC:
        depth_frame = depthQueue.get()
        depth = depth_frame.getFrame()

        y, x = np.mgrid[0:depth.shape[0], 0:depth.shape[1]]
        xyz = np.stack((x, y, depth), axis=-1).reshape(-1, 3)
        all_points.append(xyz)

        
        imu = mav.recv_match(type='ATTITUDE', blocking=False)
        if imu:
            print(f"IMU → Roll: {imu.roll:.2f}, Pitch: {imu.pitch:.2f}, Yaw: {imu.yaw:.2f}")

    print("✅ Mapping complete. Processing point cloud...")

    all_xyz = np.concatenate(all_points, axis=0)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(all_xyz / 1000.0)  # Convert mm to meters

    o3d.io.write_point_cloud(POINTCLOUD_FILE, pcd)
    print(f"📁 Map saved to {POINTCLOUD_FILE}")


print("🧪 Evaluating map quality...")

pcd = o3d.io.read_point_cloud(POINTCLOUD_FILE)
original_count = len(pcd.points)

_, inliers = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
filtered_count = len(inliers)

quality = (filtered_count / original_count) * 100
print(f"📊 Map Quality: {quality:.2f}%")


if quality >= 97:
    print("🎉 Quality OK. Compressing the map...")
    with open(POINTCLOUD_FILE, 'rb') as f_in:
        with gzip.open(COMPRESSED_FILE, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"✅ Map compressed to {COMPRESSED_FILE}")
else:
    print("❌ Map quality below 97%. Not compressing.")
