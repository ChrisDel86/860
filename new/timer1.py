import sys
import threading 
import time 

    



def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))


thread1=threading.Thread(target=countdown).start()
    



def counter(bool):
    
    hours = 0
    seconds = 0
    minutes = 0

    while (True):
        
    
        sys.stdout.write("\r{hours} Hours {minutes} Minutes {seconds} Seconds".format(hours=hours, minutes=minutes, seconds=seconds))
        sys.stdout.flush()
    
        if (seconds <= 59):
            time.sleep(1)
            seconds += 1

            if (minutes <= 59 and seconds == 59 + 1):
                minutes += 1

                if (minutes == 60 and seconds == 59 + 1 ):
                    hours += 1
                    minutes = 0
                    seconds = 0
        
        
        else:
            seconds = 0

#if __name__=="__main__":
 #   counter()