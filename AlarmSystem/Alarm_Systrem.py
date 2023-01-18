import time
import keyboard
import vlc

def alarm_level_1():
    alarm_level_1_yes = 0 #---web-app --> yes
    alarm_level_1_no = 0 #----web-app--> no
    alarm_response = "" 
#     code to play sound
    p = vlc.MediaPlayer(r"C:\Users\MRUNMAYEE J. MORE\Desktop\AlarmSystem\audio\Fatigue_Alert.mp3")
    print("Playing Fatigue Alarm for 6 seconds")
    p.play()
    time.sleep(3)
    starttime = time.time()
    print("PLEASE GIVE YOUR RESPONSE, DRIVER (y for yes, n for no): ")
    while True:
        if keyboard.is_pressed("y"):
            alarm_level_1_yes = 1
            print('Activating hotel assistance system: ')
            #call hotel api python code
            break   
        elif keyboard.is_pressed("n"):
            alarm_level_1_no = 1
            print("Going back to fatigue detection")
            return 0
            break
            
        time_spent = round((time.time() - starttime), 2)
        
        if time_spent > 10:
            print("TL exceed: {}".format(time_spent))
            play_alarm()
            break

def alarm_level_2():
    
    alarm_level_2_yes = 0 #---web-app --> yes
    alarm_level_2_no = 0 #----web-app--> no
    alarm_response = ""
    print("Calculating Medical Parameters")
    #call fitbit api
    threshold = ""

    if threshold == "abnormal":
        print("Triggering Call System - Calling the Ambulance")
        #Finding the location
       
    elif(threshold == "normal"):
        print("Do you need medical assistance? Press (y for yes, n for no):")
        start_time = time.time()
        if keyboard.is_pressed("y"):
            alarm_level_2_yes = 1
            print('Activating the medical assistance. ')
            #call hotel api python code  
                
        elif keyboard.is_pressed("n"):
            alarm_level_2_no = 1
            print("Going back to fatigue detection : normal condition")
            return 0
        
        end_time =(time.time()-start_time,2)

        if end_time> 10:
            print("TL exceed: {}".format(time_spent))
            print("Triggering the emergency alarm system ")
            #call alarm

def play_alarm():
    snooze_press = 0

    b = vlc.MediaPlayer(r"C:\Users\MRUNMAYEE J. MORE\Desktop\AlarmSystem\audio\medical_assistance.mp3")
    b.play()
    start_time = time.time()
    time.sleep(3)

    while True:
        print("Press S to snooze the alarm")

        if keyboard.pressed("s"):
            print("Snoozing the Alarm!")
            b.stop()
            alarm_level_2()
            snooze_press = 1

        time_spent = round((time.time() - starttime), 2)

        if time_spent > 10:
            print("Alarm Stopped!".format(time_spent))
            alarm_level_2()
            break

#test code loop



if __name__ == "__main__":
    alarm_level_1()
  