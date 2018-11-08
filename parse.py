#15 ethnicity
#5 nationality
i = 0
vocb = []
while i<1:
    i+=1
    j = 0
    with open("html/LGBT.html","r") as f:
        lines = f.readlines()
        for l in lines:
            vo =""
            if(j>=174):
                break
            elif j>=66:
                b = l.find("<li>")
                if(b>=0):
                    for c in range(b+4,len(l)):
                        if l[c].isalpha() or l[c] ==" ":
                            vo+=l[c]
                        else:
                            break
                if(vo==""):
                    d = l.find("wiki/")
                    if(d>=0):
                        c = l.find("\"",d)
                        e = l.find("(",d)
                        if(e<c and e!=-1):
                            vo=l[d+5:e].replace("_"," ")
                        else:
                            vo=l[d+5:c].replace("_"," ")
                if(vo!=""):
                    vocb.append(vo)
            j+=1
           

myList = open('LGBT','a')    
for w in vocb:
    myList.write(w+", LGBT\n")
myList.close()