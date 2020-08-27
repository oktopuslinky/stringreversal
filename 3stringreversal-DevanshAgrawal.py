class StringReversal:
    def __init__(self, string_input, input_list, reverse_list, new_reverse_string):
        self.string_input=string_input
        self.input_list=input_list
        self.reverse_list=reverse_list
        self.new_reverse_string=new_reverse_string

    def listify(self):
        self.input_list=list(self.string_input)

    def list_reverser(self):
        while len(self.input_list)!=0:
            self.reverse_list.append(self.input_list[-1])
            self.input_list.pop(-1)
    
    def stringify(self):
        for i in self.reverse_list:
            self.new_reverse_string+=i
        
    def __str__(self):
        return f"Your original string was {self.string_input}, and your new string is {self.new_reverse_string}"


inputter=input('What string do you want to reverse:')
my_string=StringReversal(inputter, [], [], "")
my_string.listify()
my_string.list_reverser()
my_string.stringify()
print(my_string)