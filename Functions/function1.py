#--------mixed parameters-----
#here you can pass both arbitary arguments and keyword arbitary arguments
#the order for defining such a parameter should always be *args , **kwargs
#cannot place positional argu,ments after keyword arguments

def colors(*args,**kwargs):
    for items in args:
        print(items.upper()) #its a tuple

    for key,value in kwargs.items():
        print(f"{key}:{value}")

print("---------1st----------")
colors("red","blue",name="blue",shade1="yellow",shade2="green")
print("---------2nd--------")
# colors(name="blue",shade1="yellow",shade2="green","red","blue",1100) #syntax error
colors(name="blue",shade1="yellow",shade2="green")
print("---------3rd---------")
colors("red","blue")
colors()