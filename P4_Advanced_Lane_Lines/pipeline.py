import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob

# Calibrate camera given calibration images
def camera_calibration(directory, nx, ny, draw = False):
  images = glob.glob(os.path.join(directory, 'calibration*'))
  objpoints = []
  imgpoints = []
  objp = np.zeros((nx*ny, 3), np.float32)
  objp[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)
  cnt = 0
  for file in images:
    # Read the calibration image
    img = cv2.imread(file)
    # Converting an image, imported by cv2 or the glob API, to grayscale:
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Finding chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    # If we detect the corners...
    if ret is True:
      imgpoints.append(corners)
      objpoints.append(objp)
      # If we want to draw the corners...
      if draw is True:
        # Drawing detected corners on the image
        img = cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
        plt.imshow(img)
        plt.show()
    else:
      print('Could not calibrate from %s' %file)

  # Camera calibration, given object points, image points, and the shape of the grayscale image:
  ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

  # Return the camera matrix and the distortion coefficients
  return mtx, dist

# 
def camera_undistort(directory, mtx, dist):



if __name__ == '__main__':

  mtx, dist = camera_calibration(directory = 'camera_cal/', nx = 9, ny = 6, draw = False)

  '''
  # Undistorting a test image:
  dst = cv2.undistort(img, mtx, dist, None, mtx)
  '''