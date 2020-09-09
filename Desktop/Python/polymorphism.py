class instruments:
  def intro(self): 
    print("There are many types of instruments.")
      
  def sound(self):
    print("All of the instruments crate a thier own unique sound")
    
class Guitar(instruments):
  def sound(self):
    print("Guitar creates a bass and high piched sound by struming the strings and pressing on the fretboard")
      
class bass(instruments):
  def sound(self):
    print("bass also has strings but can only play low piched sounds and not high piched sounds  ")


class Trumpet(instruments):
    def sound(self):
      print("trumpet has no string, but you can create high and low piched sounds.The trumpet sounds allmost like a horn")
      
obj_inst = instruments()
obj_Guit = Guitar()
obj_Bass = bass()
obj_trum = Trumpet()
  
obj_inst.intro()
obj_inst.sound()
  
obj_Guit.intro()
obj_Guit.sound()
  
obj_Bass.intro()
obj_Bass.sound()

obj_trum.intro()
obj_trum.sound()
