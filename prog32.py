#Write a program to demonstrate constructor and destructor usage.

class bus:
    def __init__(self,speed):
        print("BUS NO- 125 IS HAVING SPEED OF ",speed)

    def __del__(self):
        print("BUS 125 ARRIVED AT LOCATION")


b=bus(65)
del b
