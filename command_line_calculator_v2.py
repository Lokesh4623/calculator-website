
def prec(c):
  if(c=='*' or c=='/'):
     return 2
  elif(c=='+' or c=='-'):  
     return 1  
  else:
     return -1
     
def calculate(expression):
  try:    
   stack=[]
   res=[]
   r=0
   i=0
   stack.append('~')
   while i<len(expression):
     #for numbers
     if(expression[i].isnumeric()): 
       while((i<len(expression))and(expression[i].isnumeric())):
         r=int(expression[i])+r*10
         i=i+1
       res.append(r)
       r=0
       if(i==len(expression)):
           break
     if(expression[i]=='('):
           stack.append(expression[i])
     elif(expression[i]==')'):
            c=stack.pop()
            while(c!='('):
                res.append(c)
                c=stack.pop()  
     #for symbols
     else: 
          c=stack.pop()
          while((c!='~' and (prec(expression[i])<=prec(c)))):
              res.append(c)
              c=stack.pop()  
          stack.append(c)     
          stack.append(expression[i])
     i=i+1
   c=stack.pop()                  
   while(c!='~'):
     res.append(c)
     c=stack.pop()
   #print(res)    

   stack1=['~']
   symbol=['+','-','*','/']
   for i in res:
    if(i not in symbol):
      stack1.append(i)
    else:
      val1=stack1.pop()
      val2=stack1.pop()
      if i=='+':
         stack1.append(val2+val1)
      elif i=='-':
         stack1.append(val2-val1)
      elif i=='*':
         stack1.append(val2*val1)
      elif i=='/':
          stack1.append(val2/val1)
   c=stack1.pop()
  
   if(c!='~' and stack1.pop()=='~'):
      return c
   else:
      return "INVALID INPUT..."
  
  except:
     return "INVALID INPUT..."
#e=input("ENTER AN EXPRESSION:")
#print("THE RESULT IS:",calculate(e))
