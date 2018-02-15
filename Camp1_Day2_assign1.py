Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
att=Sessions_Attended["sessions"]
a=att.split(",")
cc=0
for count in a:
 try:
  b=int(count)
  cc=cc+1
 except:
  cc=cc


print("I have attended " + str(cc) + " sessions")


