s = "in publishing and graphic design"
# s = input("enter srting")
while s != "":
   slen0 = len(s)
   print(slen0,"fffffffffff")
   ch = s[0]
   print(ch,"ooooooooooooooooooooooo")

   s = s.replace(ch, "")
   print(s,"rrrrrrrrrrrrrrrrrrrrr")

   slen1 = len(s)
   print(slen1,"dddddddddddddd")
   if slen1 == slen0-1:
      print ("First unique character is: ",ch)
      break;
