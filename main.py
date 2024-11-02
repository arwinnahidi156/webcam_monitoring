import cv2 
import time
from emailing import send_email
import glob
import os
from threading import Thread

video=cv2.VideoCapture(0)
time.sleep(1)
status_list=[]
first_frame=None
count=1

def clean_folder():
  print("clean folder function started")
  images=glob.glob("images/*.png")
  for img in images:
    os.remove(img)
  print("clean folder function ended")
    
while True:
  status=0
  check,frame=video.read()
  
  gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  gray_frame_gau=cv2.GaussianBlur(gray_frame,(21,21),0)
  if first_frame is None:
    first_frame=gray_frame_gau
    
  delta_frame=cv2.absdiff(first_frame,gray_frame_gau)
  
  thresh_frame=cv2.threshold(delta_frame,60,255,cv2.THRESH_BINARY)[1]
  dil_frame=cv2.dilate(thresh_frame,None,iterations=2)
  cv2.imshow("my video",dil_frame)
  contours,check=cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  
  for counter in contours:
    if cv2.contourArea(counter) < 5000:
      continue
    
    x,y,w,h=cv2.boundingRect(counter)
    rectangle=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
    if rectangle.any():
      status=1
      cv2.imwrite(f'images/{count}.png',frame)
      count+=1
      all_images=glob.glob('images/*.png')
      index=len(all_images)//2
      img_with_object=all_images[index]
      
      
  status_list.append(status)
  
  status_list=status_list[-2:]
  print(status_list)
  if status_list[0]==1 and status_list[1]==0:
    email_thread=Thread(target=send_email,args=(img_with_object,))
    email_thread.daemon=True
    clean_thread=Thread(target=clean_folder)
    clean_thread.daemon=True
    # send_email(img_with_object)
    # clean_folder()
    
    email_thread.start()
    
    
    
    
  cv2.imshow('Video',frame) 
  key=cv2.waitKey(1)
  
  if key==ord('q'):
    break
  
clean_thread.start()
video.release()
  
  

