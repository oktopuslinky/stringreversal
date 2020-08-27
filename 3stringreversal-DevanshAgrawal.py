class StringReversal:
    def __init__(self, original_string):
        self.original_string=original_string
        self.foward_list = []
        self.reversed_list = []
        self.reversed_string = ""

    def string_processor(self):
        #runs the methods needed to reverse string
        self.listify()
        self.list_reverser()
        self.stringify()

    def listify(self):
        #turns original string into list
        self.foward_list=list(self.original_string)

    def list_reverser(self):
        #reverses list
        self.reversed_list=list(reversed(self.foward_list))
    
    def stringify(self):
        #turns reversed list into string
        self.reversed_string = f"".join(self.reversed_list)
        
    def __str__(self):
        return f"Your original string was {self.original_string}, and your new string is {self.reversed_string}"

inputter=input('What string do you want to reverse?: ')
my_string=StringReversal(inputter)
my_string.string_processor()
print(my_string)