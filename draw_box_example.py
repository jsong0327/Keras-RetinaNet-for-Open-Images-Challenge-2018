import numpy as numpy
import cv2
import sys


if len(sys.argv) != 3 or (sys.argv[1] != '-file' and sys.argv[1] != '-folder'):
  print("Write -file FILEPATH for one image and -folder FOLDERPATH for folder\nex) python csv_to_boxed_image.py -folder data/coco")
  exit(0)
if sys.argv[1] == '-folder' and sys.argv[2][-1] != '/':
    sys.argv[2] = sys.argv[2] + '/'

if (sys.argv[1] == '-file'):
  img_file_path = sys.argv[2]
  img = cv2.imread(img_file_path)
  height, width, channels = img.shape 
  # cv2.rectangle(img, (250, 70), (330, 150), (0, 255, 0), 4)
  cv2.rectangle(img, (int(0.2248*width), int( 0.0018*height)), (int(0.4889*width), int(0.8249*height)), (0, 255, 0), 4)
  cv2.imwrite('rectangle.jpg', img)
  # 0.669474 0.0016 0.3786 0.4380