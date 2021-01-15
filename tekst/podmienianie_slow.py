file=open("text_in.txt",'r')
text = file.read()
file.close()

slownik={"i": "oraz",
         "oraz": "i",
         "nigdy": "prawie nigdy",
         "dlaczego": "czemu"}

for i in slownik:
    text = text.replace(i, slownik[i])

file1 = open("text_out2.txt","w")
file1.write(text)
file1.close()