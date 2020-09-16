class instruments:
  def intro(self): 
    print("There are many types of instruments.")
      
  def sound(slef):
    print("All of the instruments crate a thier own unique sound")
    
class Guitar(instruments):
  strings = 6
  frets = 23
  def sound(self):
    print("Guitar creates a bass and high piched sound by struming the strings and pressing on the fretboard")


class Trumpet(instruments):
  buttons = 3
  color = 'gold'
  def sound(self):
      print("trumpet has no string, but you can create high and low piched sounds.The trumpet sounds allmost like a horn")
      












instrument1 = instruments()
guitar1 = Guitar()
trump1 = Trumpet()
  
instrument1.intro()
guitar1.intro()

for x in (instrument1,guitar1,trump1):
  x.sound()
  
