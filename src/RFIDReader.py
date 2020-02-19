import time
import RPi.GPIO as GPIO
import mfrc522


class RFIDReader:
    
    def __init__(self):
        self.rfid = mfrc522.MFRC522()
    
    def read(self):
        # Create an object of the class MFRC522
        # This loop checks for chips. If one is near it will get the UID
        var1 = 0;
        print("Jetzt Karte scannen.")
        try:
        
  
            while var1 == 0:

                # Scan for cards
                (status,TagType) = self.rfid.MFRC522_Request(self.rfid.PICC_REQIDL)

                # Get the UID of the card
                (status,uid) = self.rfid.MFRC522_Anticoll()

                # If we have the UID, continue
                if status == self.rfid.MI_OK:

                    # Print UID
                    print("Card UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                    return str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
                    var1 = 1
            
        

        except KeyboardInterrupt:
            GPIO.cleanup()

