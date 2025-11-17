# abstrak class
# abc = abstract base class
from abc import ABC, abstractmethod

class Button(ABC):
    
    @abstractmethod
    def click(self):
        pass
        
class PushButton(Button):
    
    def click(self):
        print("push button click")
        
class RadioButton(Button):
    
    def click(self):
        print("button radio")
        
tombol1 = PushButton()        
tombol2 = RadioButton()        
tombol1.click()
tombol2.click()