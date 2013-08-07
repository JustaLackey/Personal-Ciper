##Author: Jeffrey Chang
##https://github.com/JustaLackey
##Date 8/7/2013

class Crypter:

    def encrypt2(msg,key):
        res = ""
        temp = ''
        z = 0
        for i in range(len(msg)):
            temp = chr(((ord(msg[i])-97)^(ord(key[z])-97))+97)
            if(ord(temp)==9):
                temp = chr(0x001110)
            elif(ord(temp)==10):
                temp = chr(0x001111)
            res+=temp
            
            z+=1
            if(z>=len(key)):
               z = 0
        return res

    def decrypt2(msg,key):
        res = ""
        temp = ''
        temp2 = ''
        z = 0
        for i in range(len(msg)):
            temp2 = msg[i]
            if(ord(temp2)==0x001110):
                temp2 = chr(9)
            elif(ord(temp2)==0x001111):
                temp2 = chr(10)
            temp = chr(((ord(temp2)-97)^(ord(key[z])-97))+97)
            res+=temp
            
            z+=1
            if(z>=len(key)):
               z = 0
        return res

##ENCRYPTER RESTRICTIONS: MESSAGE AND KEYWORD MUST CONSIST OF COMMON KEYBOARD CHARACTERS ONLY

##TEST CASES

##Crypter.encrypt2("test message","keycode")
##Crypter.decrypt2("zakrpaywyek","keycode")

##ALL CHAR MSG TEST, 2 CHAR KEYWORD ALL CHAR
##9025 TEST CASES, 0 FAILURES

##count = 1
##ind = 0
##test = ""
##failures = []
##emsg = ""
##for v in range(95):
##    emsg+=chr(v+32)
##print(emsg)
##msgl = list("60")
##for a in range(95):
##    msgl[0]=chr(a+32)
##    for b in range(95):
##        msgl[1]=chr(b+32)
##        msg = ''.join(msgl)
##        print("\nTest " +str(count))
##        print(msg)
##        res = Crypter.encrypt2(emsg,msg)
##        test = Crypter.decrypt2(res,msg)
##        if(test != emsg):
##            failures+=msg
##        count+=1
##
##print("Num of failures: " + str(len(failures)))
##print("failed keywords:")
##for j in range(len(failures)):
##    print(failures[j])
