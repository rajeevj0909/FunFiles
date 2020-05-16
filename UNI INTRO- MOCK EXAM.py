'''def pretty_msg(m,l,s):
    p_msg=(s*l)+m+(s*l)
    return p_msg

def pretty_line(s,l):
    line=s*l
    return line


def say(message,symbol,message_length):
    newline=pretty_line(symbol,message_length)   
    print(newline)
    words=message.split(" ")
    for word in words:
        is_even=(message_length-len(word))%2
        if is_even==0:
            msg=word+" "
        else:
            msg=word
        side_length=int((message_length-len(msg))/2)
        newmsg=pretty_msg(msg,side_length,symbol)    
        print(newmsg)
    print(newline)

   
say("You are great","!",10)'''

'''def pretty_msg(m,l,s):
   p_msg=(s*l)+m+(s*l)
   return p_msg

newmsg=pretty_msg("hello",3,"-")
print (newmsg)'''

'''def size_msg(m):
   s=len(m)
   return s

x=size_msg("hello")
print (x)'''
'''SIDE_LENGTH=6
def good_line(s,l):
   line=s*l
   print (line)
def say(msg,s,sl=SIDE_LENGTH):
   side_length=sl
   l=len(msg)+side_length*2
   good_line(s,l)   
   print ((s*side_length)+msg+(s*side_length))
   good_line(s,l)
   
say(s="!",msg="You")

say(s=".",msg="I",sl=3)'''

'''SIDE_LENGTH=6
def good_line(s,l):
   line=s*l
   print (line)
def say(msg,s):
   side_length=SIDE_LENGTH
   l=len(msg)+side_length*2
   good_line(s,l)   
   print ((s*side_length)+msg+(s*side_length))
   good_line(s,l)
msg="YOU"
say(msg,"&")'''

'''def good_line(s,l):
   line=s*l
   print (line)
def say(msg,s):
   side_length=3
   l=len(msg)+side_length*2
   good_line(s,l)   
   print ((s*side_length)+msg+(s*side_length))
   good_line(s,l)
msg="Best"
say(msg,"-")'''

'''def good_line(s):
   line=s*11
   print (line)
def say(msg):
   good_line("$")   
   print ("***"+msg+"***")
   good_line("$")

msg="Best"
say(msg)'''

'''def star_line():
   line="*"*11
   print (line)
def say_hello():
   star_line()   
   print ("***"+"hello"+"***")
   star_line()

say_hello()'''
'''def star_line():
   line="*"*10
   print (line)
def say_hello():
   print ("hello")
star_line()
say_hello()
star_line()'''

'''def say_hello():
   print ("hello")
say_hello()'''


'''def say_hello():
   print ("hello")

for i in range(4):
   say_hello()'''
