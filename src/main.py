import tempfile
import cv2
import numpy as np
import mediapipe as mp
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from yolo import *
import tempfile
import streamlit as st


def main():
    st.title("Object Detection Dashboard YOLOR")
    st.sidebar.title("Settings")
    st.markdown("""
    <style>
    [data-testid="stSidebar"][aria-exapnded="true"] > div:first-child{width:480px;}
    [data-testid="stSidebar"][aria-exapnded="false"] > div:first-child{width:400px;margin-left:-400px}
    </style>
    """,unsafe_allow_html=True)

    confidence = st.sidebar.slider('Confidence',min_value=0.0,max_value=1.0,value=0.25)
    st.sidebar.markdown('-----')

    save_img = st.sidebar.checkbox('Save Video')
    enabed_GPU = st.sidebar.checkbox('Enable_GPU')
    custom_classes = st.sidebar.checkbox('Use Custom CLasses')

    assigned_class_id =[]

    if custom_classes:
        assigned_class = st.sidebar.multiselect('Select The Custom Classes',list(names),default='person')
        for each in assigned_class:
            assigned_class_id.append(names.index(each))
    
    video_file_buffer = st.sidebar.file_uploader("Upload a Video",type=["mp4","mov",'avi','asf','m4v'])

    DEMO_VIDEO ='test.mp4'
    tffile = tempfile.NamedTemporaryFile(suffix='.mp4',delete=False)

    # We get out input video here

    if not video_file_buffer:
        vid = cv2.VideoCapture(DEMO_VIDEO)
        tffile.name = DEMO_VIDEO
        dem_vid = open(tffile.name,'rb')
        demo_bytes =dem_vid.read()

        st.sidebar.text('Input Video')
        st.sidebar.video(demo_bytes)
    
    else:
        ttfile.write(video_file_buffer.read())
        dem_vid = open(tffile.name,'rb')
        demo_bytes =dem_vid.read()

        st.sidebar.text('Input Video')
        st.sidebar.video(demo_bytes)

    print(tffile.name)

    sframe = st.empty()
    st.sidebar.markdown('-------')

    kpi1 , kpi2 ,kpi3 = st.columns(3)

    with kpi1:
        st.markdown("**Frame Rate**")
        kpi1_text=st.markdown("0")

    with kpi2:
        st.markdown("**Tracked Objects**")
        kpi2_text=st.markdown("0")

    with kpi3:
        st.markdown("**Width**")
        kpi3_text=st.markdown("0")
    
    st.text('Video is Processed')
    vid.release()

    # Inset code for KPI

    kpi1_text.write(f"<h1 style='text-align : center;color:red;'>{'{:.1f}'.format(f)}</h1>",unsafe_allow_html=True)






if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
