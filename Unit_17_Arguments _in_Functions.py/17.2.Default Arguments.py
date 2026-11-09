# default Argument
'''
You can assign default value to argument in function definition
if ale is not given function is called,the default value is used

'''

# Example 1.Function defined using one paramater and default value

def greeting(name="Name is Missing"):
    print("Hello,",name)

greeting()        #Runs without error by default Value

# 1.1 

def greeting(name="Name is Missing"):
    print("Hello,",name)

#greeting()

greeting("Anil")



