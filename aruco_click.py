import cv2
import numpy as np
import cv2.aruco as aruco
import paho.mqtt.client as mqtt
from math import atan2
import time

client = mqtt.Client()
client.connect("192.168.0.196", 1883, 60)

# kalibrasyon datalarını yüklüyorum
def load_coefficients(path):
    """ Loads camera matrix and distortion coefficients. """
    # FILE_STORAGE_READ
    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

    # note we also have to specify the type to retrieve other wise we only get a
    # FileNode object back instead of a matrix
    camera_matrix = cv_file.getNode("K").mat()
    dist_matrix = cv_file.getNode("D").mat()

    cv_file.release()
    return [camera_matrix, dist_matrix]
mtx, dist = load_coefficients('calib.yml')

def anglee(v1,v2):
    angle1 = atan2(v1[1], v1[0]) * 180 / np.pi
    angle2 = atan2(v2[1], v2[0]) * 180 / np.pi
    dif = angle2 - angle1
    if dif < 0: dif += 360
    return dif

target = []
def mousePoints(event,x,y,flags,params):
    global target
    if event == cv2.EVENT_LBUTTONDOWN:
        target = [x,y]
        print("TTTTTTTTTTTTTTTTTTTarget:::::::", target)
    return target

# rodrigues fonksiyonu ile rotasyon matrisi elde ediyorum
def create_rot_mat(rvec):
    rot_mat, _ = cv2.Rodrigues(rvec)
    return rot_mat

def direction(rvec):
    R = create_rot_mat(rvec)
    x_basis_of_marker0 = np.dot(R, np.array([0, 1, 0]), )
    x_new = np.delete(x_basis_of_marker0,2)
# kırmızı vectorun tersine gidiyor arac
    return x_new

# Aruco detection
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    arucoParameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(grayImg, aruco_dict, parameters=arucoParameters)
    #print(ids)

    if ids is not None:
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.0225, mtx, dist)
        (rvec - tvec).any()

        for i in range(rvec.shape[0]):
            cv2.drawFrameAxes(frame, mtx, dist, rvec[i, :, :], tvec[i, :, :], 0.0225)
            aruco.drawDetectedMarkers(frame, corners, ids)

            center_x = (corners[0][0][0][0]+corners[0][0][1][0]+corners[0][0][2][0]+corners[0][0][3][0])/4
            center_y = (corners[0][0][0][1]+corners[0][0][1][1]+corners[0][0][2][1]+corners[0][0][3][1])/4
            center_l = [center_x,  center_y]
            center = np.array(center_l)
            #print("center:", center)
            unit_dir = direction(rvec[0,:,:])
            if target:
                target_vector = np.subtract(target, center)
                target_vector_magnitude = np.sqrt(target_vector.dot(target_vector))
                #print("target_vector_magnitude:",target_vector_magnitude )
                if target_vector_magnitude > 100:
                    #print("targetvector:", target_vector)
                    unit_target_vector = target_vector/np.linalg.norm(target_vector)
                    #print("Unit_target_vector:", unit_target_vector)
                    angle = anglee(unit_target_vector, unit_dir)
                    print("Angle", angle)
                    if 10 < angle <= 180:
                        client.publish("rot_commands", "Turn_Right")
                        print("Turning Left...")

                    elif 180 < angle < 350:
                        print("Turning Right...")
                        client.publish("rot_commands", "Turn_Left")

                    else:
                        print("Moving to the Target...")
                        client.publish("rot_commands", "Move_Forward")



    cv2.imshow('Frame', frame)
    cv2.setMouseCallback("Frame", mousePoints)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
