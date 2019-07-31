import numpy as np
import cv2
import csv
import argparse


def is_word(s):
  try:
    float(s)
    return False
  except ValueError:
    return True


if __name__ == '__main__':
  my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

  my_parser.add_argument('image_folder',
                        help='Path to folder that contains image files ex) /dataset/validation_big')

  my_parser.add_argument('csv_file',
                        help='Path to output csv file ex) ../subm/predictions_0.01_0.55_avg.csv')

  args = my_parser.parse_args()

  image_folder_path = args.image_folder
  csv_file_path = args.csv_file

  with open (csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      # Parse
      if line_count == 0:
          print('Column names are %s, %s' % (row[0], row[1]))
          line_count += 1
          continue
      else:
          # print('Contents are %s, %s' % (row[0], row[1]))
          line_count += 1
      prediction = row[1].split()
      i = 0
      while i < len(prediction) - 1:
        print("i is %d and length is %d" % (i, len(prediction)))
        if is_word(prediction[i]) and is_word(prediction[i+1]):
          print('Join with %s and %s done' % (prediction[i], prediction[i+1]))
          prediction[i:i+2] = [' '.join(prediction[i:i+2])]
        else:
          i += 1
      print(prediction)
      print('Length of prediction is %d' % len(prediction))

      # Draw squares
      image_file = row[0] + '.jpg'
      image_file_path = image_folder_path + image_file
      print(image_file_path)
      img = cv2.imread(image_file_path)
      height, width, channels = img.shape 
      print(image_file_path)
      for i in range(0, len(prediction), 6):
        if (float(prediction[i+1]) > 0.3):
          minX = int( width * float(prediction[i+2]) )
          minY = int( height * float(prediction[i+3]) )
          maxX = int( width * float(prediction[i+4]) )
          maxY = int( height * float(prediction[i+5]) )
          cv2.rectangle(img, (minX, minY), 
                              (maxX, maxY), 
                              (0, 255, 0), 4)
          if minY > 10:
            cv2.putText(img, prediction[i] + '|' + prediction[i+1], (minX, minY - 2),
                      cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
          else:
            cv2.putText(img, prediction[i] + '|' + prediction[i+1], (minX, minY + 25),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
      cv2.imwrite('/output/' + image_file, img)
      print(image_file)


  print("Done")