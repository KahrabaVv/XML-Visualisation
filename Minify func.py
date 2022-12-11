def minify(string):
      
      string=string.translate({ord('\t'): None})
      string=string.translate({ord('\n'): None})
      string= string.replace('  ', '')
      return string            
      