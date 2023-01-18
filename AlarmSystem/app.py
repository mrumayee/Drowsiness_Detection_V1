import cv2
import streamlit as st
import numpy as np
import pandas as pd


# st.title("Webcam Live Feed")
# run = st.checkbox('Run')
# FRAME_WINDOW = st.image([])
# camera = cv2.VideoCapture(0)

# while run:
#     _, frame = camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
# else:
#     st.write('Stopped')

from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading



RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

# st.set_page_config(page_title="Streamlit WebRTC Demo", page_icon="🤖")
# task_list = ["Video Stream"]

# with st.sidebar:
#     st.title('Task Selection')
#     task_name = st.selectbox("Select your tasks:", task_list)
# st.title(task_name)

# if task_name == task_list[0]:
#     style_list = ['color', 'black and white']
#     st.sidebar.header('Style Selection')
#     style_selection = st.sidebar.selectbox("Choose your style:", style_list)

#     class VideoProcessor(VideoProcessorBase):
#         def __init__(self):
#             self.model_lock = threading.Lock()
#             self.style = style_list[0]

#         def update_style(self, new_style):
#             if self.style != new_style:
#                 with self.model_lock:
#                     self.style = new_style

#         def recv(self, frame):
#             # img = frame.to_ndarray(format="bgr24")
#             img = frame.to_image()
#             if self.style == style_list[1]:
#                 img = img.convert("L")

#             # return av.VideoFrame.from_ndarray(img, format="bgr24")
#             return av.VideoFrame.from_image(img)

#     ctx = webrtc_streamer(
#         key="example",
#         video_processor_factory=VideoProcessor,
#         rtc_configuration=RTC_CONFIGURATION,
#         media_stream_constraints={
#             "video": True,
#             "audio": False
#         }
#     )

#     if ctx.video_processor:
#         ctx.video_transformer.update_style(style_selection)

# st.set_page_config(
#     page_title="Streamlit WebRTC Demo",
#     page_icon="chart_with_upwards_trend")

# st.title("Driver Drowsiness Detection")


# task_list = ["Video Stream", "About", "Manual"]
# with st.sidebar:
#     st.title('Task Selection')
#     task_name = st.selectbox("Select your tasks:", task_list)
# st.title(task_name)

# if task_name == task_list[0]:
#     style_list = ['color', 'black and white']
#     st.sidebar.header('Style Selection')
#     style_selection = st.sidebar.selectbox("Choose your style:", style_list)

# elif task_name == task_list[1]:
#     st.markdown('#Team Members')

# else:
#     st.markdown('#How to use the Application')

# Face Analysis Application #

st.title("Driver Drowsiness Detection Application") 
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)      
activiteis = ["Home", "Webcam Face Detection", "About"]
choice = st.sidebar.selectbox("Select Activity", activiteis)
st.sidebar.markdown(
    """ Developed for LY Project 22-23  
    """)
if choice == "Home":
    
    html_temp_home1 ="""
                        <div style="background-color:#6D7B8D;padding:20px;border-radius:5px">
                            <h4 style="color:white;text-align:center;">
                                Driver Drowsiness Detection Application using OpenCV, Custom CNN model and Streamlit.
                            </h4>
                        </div></br>
                    """
    st.markdown(html_temp_home1, unsafe_allow_html=True)
    st.write("""
                The application has two functionalities.
                1. Real time face detection using web cam feed.
                2. Real time face emotion recognization.
                """)
elif choice == "Webcam Face Detection":
    st.header("Webcam Live Feed")
    st.write("Click on start to use webcam and detect your face emotion")
    webrtc_streamer(
        key="example", video_transformer_factory=VideoTransformer)
elif choice == "About":
    st.subheader("About this app")
    html_temp_about1 = """<div style="background-color:#6D7B8D;padding:10px">
                                <h4 style="color:white;text-align:center;">
                                Real time face emotion detection application using OpenCV, Custom Trained CNN model and Streamlit.</h4>
                                </div>
                                </br>"""
    st.markdown(html_temp_about1, unsafe_allow_html=True)
    html_temp4 = """
                                <div style="background-color:#98AFC7;padding:10px">
                                <h4 style="color:white;text-align:center;">This Application is developed by Mohammad Juned Khan using Streamlit Framework, Opencv, Tensorflow and Keras library for demonstration purpose. If you're on LinkedIn and want to connect, just click on the link in sidebar and shoot me a request. If you have any suggestion or wnat to comment just write a mail at Mohammad.juned.z.khan@gmail.com. </h4>
                                <h4 style="color:white;text-align:center;">Thanks for Visiting</h4>
                                </div>
                                <br></br>
                                <br></br>"""
    st.markdown(html_temp4, unsafe_allow_html=True)  