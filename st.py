import streamlit as st
import cv2
import datetime

st.title("Motion detector")
start=st.button("Start Camera")

if start:
  streamlit_image=st.image([])
  camera=cv2.VideoCapture(0)
  
  while True:
    check,frame=camera.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    time_now=datetime.datetime.strftime(datetime.datetime.now(),'%H:%M:%S')
    weekday=datetime.datetime.today().strftime('%A')
    
    text=f"{weekday} {time_now}"
    cv2.putText(img=frame,text=weekday,org=(30,30),
                fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(255,0,0),
                thickness=2,lineType=cv2.LINE_AA)
    cv2.putText(img=frame,text=time_now,org=(30,80),
                fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(20,100,200),
                thickness=2,lineType=cv2.LINE_AA)
    
    streamlit_image.image(frame)