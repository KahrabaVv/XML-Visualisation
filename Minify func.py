file=open("E:\sample.xml","r")
file2=open("E:\sample2.xml","w")
for line in file:
      x=file.readline()
      x=x.replace("  ", " ")
      x=x.strip()
      file2.write(x)      
file.close()
file2.close()           
                  
