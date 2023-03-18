import time
import keyboard
import streamlit as st

from Fitbit import heartrate_fitbit

def alarm_level_1():
    alarm_level_1_yes = 0 #---web-app --> yes
    alarm_level_1_no = 0 #----web-app--> no
    alarm_response = "" 
#     code to play sound
    #p = vlc.MediaPlayer(r"C:\Users\Navya\Documents\GitHub\Drowsiness_Detection_V1\audio\Fatigue_Alert.mp3")
    html_string = """
                <audio controls autoplay>
                <source src="https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3" type="audio/mp3">
                </audio>
                """
    st.write("Do you need hotel assistance?")
    sound = st.empty()
    sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
                
   # p.play()
    time.sleep(3)
    starttime = time.time()
    st.write("PLEASE GIVE YOUR RESPONSE, DRIVER (y for yes, n for no): ")
    while True:
        if keyboard.is_pressed("y"):
            alarm_level_1_yes = 1
            st.write('Activating hotel assistance system: ')
            #call hotel api python code
            break   
        elif keyboard.is_pressed("n"):
            alarm_level_1_no = 1
            st.write("Going back to fatigue detection")
            return 0
            break
            
        time_spent = round((time.time() - starttime))
        
        if time_spent > 10:
            st.write("TL exceed: {}".format(time_spent))
            play_alarm()
            break

def alarm_level_2():
    
    alarm_level_2_yes = 0 #---web-app --> yes
    alarm_level_2_no = 0 #----web-app--> no
    alarm_response = ""
    st.write("Calculating Medical Parameters")
    # Fitbit Api here
    
    st.write(heartrate_fitbit.fitbit_callback())
    if heartrate_fitbit.fitbit_callback() == "abnormal":
        st.write("Triggering Call System - Calling the Ambulance")
        #Finding the location
       
    elif(heartrate_fitbit.fitbit_callback() == "normal"):
        html_string = """
                <audio controls autoplay>
                <source src="https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3" type="audio/mp3">
                </audio>
                """
        sound = st.empty()
        sound.markdown(html_string, unsafe_allow_html=True) 
        st.write("Do you need medical assistance? Press (y for yes, n for no):")

        start_time = time.time()
        while True:
            if keyboard.is_pressed("y"):
                alarm_level_2_yes = 1
                st.write('Activating the medical assistance. ')
                #call hospital api python code  
                break

            elif keyboard.is_pressed("n"):
                alarm_level_2_no = 1
                st.write("Going back to fatigue detection : normal condition")
                return 0

            end_time =(time.time()-start_time)

            if end_time > 10:
                # print("TL exceed: {}".format(time_spent))
                st.write("No response received! Triggering the emergency alarm system ")
                return 0
                #call alarm

def play_alarm():
    snooze_press = 0
    html_string = """
                <audio controls autoplay>
                <source src="https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3" type="audio/mp3">
                </audio>
                """
    st.write("Press S to snooze the alarm")
    sound = st.empty()
    sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
    #b = vlc.MediaPlayer(r"C:\Users\MRUNMAYEE J. MORE\Desktop\AlarmSystem\audio\medical_assistance.mp3")
    #b.play()
    start_time = time.time()
    time.sleep(3)

    while True:

        if keyboard.is_pressed("s"):
            st.write("Snoozing the Alarm!")
            #st.stop()
            alarm_level_2()
            snooze_press = 1

        time_spent = round((time.time() - start_time))

        if time_spent > 10:
            st.write("No response received! Alarm Stopped!".format(time_spent))
            alarm_level_2()
            break

#test code loop



if __name__ == "__main__":
    alarm_level_1()
  