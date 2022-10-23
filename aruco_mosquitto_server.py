import cv2
import numpy as np
import cv2.aruco as aruco
import paho.mqtt.client as mqtt
import json

BROKER_ADDR = "192.168.92.4"
TOPIC = "deneme"

client = mqtt.Client()
client.connect(BROKER_ADDR, 1883, 60)


def load_coefficients(path):
    """ Loads camera matrix and distortion coefficients. """
    # FILE_STORAGE_READ
    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

    # note we also have to specify the type to retrieve otherwise we only get a
    # FileNode object back instead of a matrix
    camera_matrix = cv_file.getNode("K").mat()
    dist_matrix = cv_file.getNode("D").mat()

    cv_file.release()
    return [camera_matrix, dist_matrix]


mtx, dist = load_coefficients('calib.yml')

# Aruco detection
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    arucoParameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(grayImg, aruco_dict, parameters=arucoParameters)

    if ids is not None:
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 30, mtx, dist)
        (rvec - tvec).any()

        lst = []
        for i in range(len(ids)):
            vec = [round(elem) for elem in (tvec[i][0]).tolist() ]
            lst1 = [[int(ids[i][0]), vec]]
            lst += lst1
            lst1.clear()
        client.publish(TOPIC, json.dumps(lst))
        lst.clear()

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()

