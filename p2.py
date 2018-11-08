with open("Hate Base Word List","r") as f:
    line = f.readlines()
    cur = "ethnicity"
    filename = open("slurs/"+cur+".csv","w")
    for l in line:
        (word, cat) = l.split(", ")
        if(cat!=cur):
            cur = cat
            filename.close()
            filename = open("slurs/"+cur+".csv","w")
            filename.write(word.lower()+", ")
        else:
            filename.write(word.lower()+", ")
