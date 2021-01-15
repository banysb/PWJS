file=open("text_in.txt",'r')
text = file.read()
file.close()
delete = ["się ", "i ", "oraz ", "nigdy ", "dlaczego "]
for i in delete:
    text = text.replace(i, '')

file1 = open("text_out1.txt","w")
file1.write(text)
file1.close()