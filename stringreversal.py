class StringReversal:
    def __init__(self, string_input, orig_list, new_list, new_string):
        self.string_input=string_input
        self.orig_list=orig_list
        self.new_list=new_list
        self.new_string=new_string

    def listify(self):
        self.orig_list=list(self.string_input)

    def a_new_list(self):
        while len(self.orig_list)!=0:
            self.new_list.append(self.orig_list[-1])
            self.orig_list.pop(-1)
    
    def stringify(self):
        for i in self.new_list:
            self.new_string+=i
        
    def __str__(self):
        return f"Your original string was {self.string_input}, and your new string is {self.new_string}"


inputter=input('What string do you want to reverse:')
my_string=StringReversal(inputter, [], [], "")
my_string.listify()
my_string.a_new_list()
my_string.stringify()
print(my_string)