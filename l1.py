from pyduino import *
import time

if __name__ == '__main__':
    
    a = Arduino()
    # if your arduino was running on a serial port other than '/dev/ttyACM0/'
    # declare: a = Arduino(serial_port='/dev/ttyXXXX')

    time.sleep(3)
    # sleep to ensure ample time for computer to make serial connection 

    PIN = 13
    a.set_pin_mode(PIN,'O')
    # initialize the digital pin as output
    print ("Enter 1 to turn ON LED and 0 to turn OFF LED")


    time.sleep(1)
    # allow time to make connection

    while 1: 

      var = raw_input() #get input from user
      print "you entered", var #print the input for confirmation
   
      if (var == '1'): #if the value is 1
        a.digital_write(PIN,1) # turn LED on
        print ("LED turned ON")
        time.sleep(1)

      elif (var == '0'): #if the value is 0
        a.digital_write(PIN,0) # turn LED off
        print ("LED turned OFF")
        time.sleep(1)
