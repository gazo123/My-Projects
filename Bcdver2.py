#VARIABLES

zero  = [1,1,0,1,1,1,1]
one   = [0,0,0,1,0,0,1]
two   = [1,0,1,1,1,1,0]
three = [1,0,1,1,0,1,1]
four  = [0,1,1,1,0,0,1]
five  = [1,1,1,0,0,1,1]
six   = [1,1,1,0,1,1,1]
seven = [1,0,0,1,0,0,1]
eight = [1,1,1,1,1,1,1]
nine  = [1,1,1,1,0,1,1]
list1 = [zero,one,two,three,four,five,six,seven,eight,nine]
temp  = [0,0,0,0,0,0,0]

#FUNCTION FOR DECIMAL INPUT

def decimalinput(num,list1):
   temp=list1[num]
   printing(temp)

#FUNCTION FOR BCD INPUT
def bcdinput():
      print("\nEnter 4-digit binary input: ")
      #f1, f2, f3, f4 = int(input("\nEnter 4-digit binary input: ")).split()

      f1 =  int(input("Enter 1st number:"))
      f2 =  int(input("Enter 2nd number:"))
      f3 =  int(input("Enter 3rd number:"))
      f4 =  int(input("Enter 4th number:"))

      if(f1==0 and f2==0 and f3==0 and f4==0):
        print("ZERO")
        temp = zero
      elif(f1==0 and f2==0 and f3==0 and f4==1):
         print("ONE")
         temp=one
      elif(f1==0 and f2==0 and f3==1 and f4==0):
         print("TWO")
         temp=two
      elif(f1==0 and f2==0 and f3==1 and f4==1):
         print("THREE")
         temp = three
      elif(f1==0 and f2==1 and f3==0 and f4==0):
         print("FOUR")
         temp=four
      elif(f1==0 and f2==1 and f3==0 and f4==1):
         print("FIVE")
         temp=five
      elif(f1==0 and f2==1 and f3==1 and f4==0):
         print("SIX")
         temp=six
      elif(f1==0 and f2==1 and f3==1 and f4==1):
         print("SEVEN")
         temp=seven
      elif(f1==1 and f2==0 and f3==0 and f4==0):
         print("EIGHT")
         temp=eight
      elif(f1==1 and f2==0 and f3==0 and f4==1):
         print("NINE")
         temp=nine
      else:
        print("Wrong Input!")
      printing(temp)      

#FUNCTION FOR PRINTING THE 7 SEGMENT OUTPUT 

def printing(temp):
   #Putting the character in a list   
   b=[]
   for i in range(0,7):
      if (i==0 or i==2 or i==5):
         if(temp[i] ==1):
            b.append("_")
         else:
               b.append(" ")
      else:
         if(temp[i]==1):
            b.append("|")
         else:
            b.append(" ")
         
      #print(b)
      
   print("\nLCD output : ")
   print(" ",b[0],sep="")
   print(b[1],b[2],b[3],sep="")
   print(b[4],b[5],b[6],sep="")

j=1 
print("BCD TO 7 SEGMENGT DISPLAY DECODER ")     
while(j==1):
   ch=int(input("\n1.Decimal input\n2.BCD input\n Enter your choice :"))
   if ch==1:
      num = int(input("Enter decimal value :"))
      decimalinput(num,list1)
   elif ch==2:
      bcdinput()
   else:
      print("Wrong input !!!")
   j=int(input("Enter '1' if you want to display another number :"))
      