import re
def minify(string):
      string=string.translate({ord('\t'): None})
      string=string.translate({ord('\n'): None})
      string= string.replace('  ', '')
      string= string.replace('> <','><')
      return string

def beautify(string):
      string=minify(string)
      string=re.sub("<","\n<",string)
      string=re.sub(">",">\n",string)
      Lines = string.split("\n")
      string_output=""  
      def smallest_between_two(a, b, text):
           
            return re.findall(re.escape(a)+"(.*?)"+re.escape(b),text)
      o_tag=[]
      c_tag=[]
      count=-1
      f_close=False
      f_data=True
      for line in Lines:
            f_data=True
            f_close=False
            size=len(smallest_between_two('<', '>',line ))
      
            if(len(line)==0):
                  continue
            if(size!=0):
                  for tag in smallest_between_two('<', '>',line ):
                        f_data=False 
                        if("/" in tag):
                              c_tag.append(tag)
                              f_close=True
                        else:
                              o_tag.append(tag)
                              count+=1
            if(f_data):
                  count+=1
            string_output=string_output+ "\t"*count+line+"\n"
            if(f_close or f_data):
                  count=count-1
      return string_output
