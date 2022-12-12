class Node:
    def __init__(self, tagName, index, line, errMsg = None) -> None:
        self.tagName = tagName
        self.index = index
        self.line = line
        self.errMsg = errMsg
        pass

def ErrorCheck(allTags = [], path = "sample.xml",correction = True):
    tagStack = []
    id = 0

    Pj = 0
    Pf = 0

    errors = []
    lineNumber = 0
    symbolStack = []
    comment = False
    tagName = ""
    line:str = ""
    file = open(path,'r')
    # if correction:

    for line in file:
        line = line.strip()
        if correction == True:
            for insideline in file:
                line += insideline.strip()

        lineNumber +=1
        
        for ind in range(0,len(line)):
            #check begin of tag
            if line[ind] == '<' and not comment:
                #check if there is unclosed tag before
                if len(line) > (ind + 3) and  line[ind+1:ind+4] == '!--': 
                    comment = True
                    continue
                
                # Missing '>'
                if( symbolStack and symbolStack[-1] == '<' ):
                    currentTag.tagName = tagName
                    if tagName[0] != '/':    
                        tagStack.append(currentTag)
                        currentTag.id = id
                        allTags.append(currentTag)
                        id+=1
                    else:
                        #close of open tag
                        if tagName[1:] == tagStack[-1].tagName:
                            tagStack.pop()

                            cur = Node(tagName,ind,lineNumber)
                            cur.id = id
                            id+=1
                            allTags.append(cur)

                        else:
                            tagStack.append(currentTag)
                            currentTag.id = id
                            allTags.append(currentTag)
                            id+=1
                            pass
                    symbolStack.pop()
                    errMsg = "Missing>"
                    currentTag.errMsg = errMsg
                    errors.append(currentTag)
                    pass
                currentTag = Node("",ind,lineNumber)
                
                #
                symbolStack.append(line[ind])
                tagName = ""
                pass

            elif line[ind] == '>':
                # check end of Comment
                if ind > 3 and line[ind-2:ind] == '--': 
                    comment = False
                    continue
                if comment: continue

                #check Missing <
                if not symbolStack:
                    n = 1
                    tempTag = []
                    while True:
                        tempTag.append(line[ind-n])
                        # print(line[ind-n-1], ind-n-1)
                        if ind-n-1 <0 or line[ind-n-1] == " " or line[ind-n] == "/" or line[ind-n-1] == ">":
                            break
                        n+=1
                    tagName = ""
                    while tempTag:
                        tagName += tempTag.pop()
                    symbolStack.append('<')
                    currentTag = Node(tagName,ind,lineNumber,"Missing<")
                    errors.append(currentTag)

                    
                #if begin of tag

                if tagName[0] != '/':    
                    currentTag.tagName = tagName
                    tagStack.append(currentTag)
                    currentTag.id = id
                    allTags.append(currentTag)
                    id+=1
                else:
                    #close of tag with open tag
                    if tagName[1:] == tagStack[-1].tagName:
                        tagStack.pop()

                        cur = Node(tagName,ind,lineNumber)
                        cur.id = id
                        id+=1
                        allTags.append(cur)

                    else:
                        currentTag.tagName = tagName
                        tagStack.append(currentTag)
                        currentTag.id = id
                        id+=1
                        allTags.append(currentTag)
                        pass
                symbolStack.pop()
                pass

            elif symbolStack:
                if not comment:
                    tagName = tagName + line[ind] 


    Pf = len(tagStack) -1
    while tagStack:
        Pj = 0
        done = False
        if Pf == Pj:
            buttonTag = tagStack.pop(0)
            err = Node(buttonTag.tagName, buttonTag.index,buttonTag.line)
            err.id = buttonTag.id
            if buttonTag.tagName[0] == '/':
                err.errMsg = "unOpenedTag"
            else:
                err.errMsg = "unClosedTag"
            Pf = len(tagStack) -1
            errors.append(err)
            continue

        buttonTag = tagStack.pop(0)
        err = Node(buttonTag.tagName, buttonTag.index,buttonTag.line)
        err.id = buttonTag.id

        Pf -=1
        if buttonTag.tagName[0] == '/':
            err.errMsg = "unOpenedTag"
            errors.append(err)
        else:
            if Pf == 0:
                if tagStack[Pj].tagName[0] == '/':
                    err.unMatchedTag = tagStack.pop(Pj)
                    err.errMsg = "MisMatchTag"
                    err.index = err.unMatchedTag.index
                    err.line = err.unMatchedTag.line
                    

                else:
                    err.errMsg = "unClosedTag"
                Pf = len(tagStack) -1
                errors.append(err)
                continue



            while Pj <= Pf:
                if tagStack[Pj].tagName == ('/' + buttonTag.tagName):
                    tagStack.pop(Pj)
                    Pf = Pj -1
                    done = True
                    break
                Pj += 1
            if done: continue
            err.errMsg = "unClosedTag"
            errors.append(err)    
    return errors