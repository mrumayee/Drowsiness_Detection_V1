import cv2
import streamlit as st
import numpy as np
import pandas as pd
import base64

from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

st.set_page_config(page_title="WebRTC DDD",
                   page_icon="chart_with_upwards_trend")

with open('frontend\style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# ------------------ SideBar  -----------------------

activities = ["Home", "Webcam", "Maps", "Manual", "Team"]
icons1 = ['house', 'camera', 'map', 'gear', 'sun']
# choice = st.sidebar.selectbox("Select Activity", activities)
choice = option_menu(None, ["Home", "Webcam", "Maps", "Manual", "Team"], icons=['house', 'camera', 'map', 'gear', 'sun'], menu_icon="cast",
                     default_index=0, orientation="horizontal",styles={
                        "container": {"margin-top":"0px"},})

st.header("Real Time Driver Drowsiness Detection System")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)



# ------------------- Menu Options ---------------------

if choice == "Home":
    html_option_bar ="""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <div class="container my-4">
    <div class="row row row-cols-1 row-cols-md-4 g-4">
      <div class="col">
        <div class="card h-100">
            <img src="https://source.unsplash.com/1200x600?image" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Open Cv & DLIB </h5>
                <a type="button" href="https://opencv.org/" class="btn btn-sm btn-dark">Visit Website</a>
            </div>
        </div>
    </div>
    <div class="col">
      <div class="card h-100 w-100">
          <img src="https://source.unsplash.com/1200x600?google" class="card-img-top" alt="...">
          <div class="card-body">
              <h5 class="card-title">Google Maps API </h5>
              <a type="button" href="https://mapsplatform.google.com/"class="btn btn-sm btn-dark">Visit Website</a>
          </div> 
      </div>
  </div>
  <div class="col">
    <div class="card h-100 w-100">
        <img src="https://source.unsplash.com/1200x600?fitbit" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">FitBit API </h5>
            <a type="button" href="https://www.fitbit.com/dev"class="btn btn-sm btn-dark">Visit Website</a>
        </div>
    </div>
</div>
<div class="col">
  <div class="card h-100 w-100">
      <img src="https://source.unsplash.com/1200x600?ui" class="card-img-top" alt="...">
      <div class="card-body">
          <h5 class="card-title">Streamlit</h5>
          <a type="button" href="https://docs.streamlit.io/" class="btn btn-sm btn-dark">Visit Website</a>
      </div>
  </div>
</div>
</div>
</div>"""
    st.markdown(html_option_bar, unsafe_allow_html=True)

elif choice == "Webcam":
    st.header(f"Welcom to Webcam Live Feed")
    st.write("Click on start to use webcam and detect your face emotion")
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)


elif choice == "Maps":
    st.header("Welcome to Navigation system")
    st.write("Search for nearby Hospitals and Hotels")
    col1, col2 = st.columns([0.5,0.5])
    
    with col1:
        if st.button('Hospitals'):
            st.write("Displaying nearby Hospital list")
    with col2:
        if st.button('Hotels'):
            st.write("Displaying nearby Hotels list")
    
    
elif choice == "Manual":
    st.header("Welcome to Documentation")
    
    

elif choice == "Team":
    st.header("About Creators")
    

# -------------  Footer code  ---------------------

html_footer = """<div class="footer-container">
                <div class="footer-content">
                    Copyright &copy; Your Website
                </div>
            </div>"""
st.markdown(html_footer, unsafe_allow_html=True)
