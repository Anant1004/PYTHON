class poopsi():
    def __init__(self,looks,tall):
        self.looks = looks
        self.tall = tall

class mommy():
    def __init__(self,fair,cute):       
        self.fair = fair
        self.cute = cute

class daughter(mommy,poopsi):
    def __init__(self, fair, tall,cute,looks):
        super().__init__(fair, cute)
        poopsi.__init__(self,tall,looks)
    def show_details(self):
        print(f"The daughter skin is {self.fair} and the height is {self.tall}")



soni = daughter("light","7ft","yes","attractive")
soni.show_details()