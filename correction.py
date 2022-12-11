from validation import ErrorCheck,Node
def correction(path = 'sample.xml'):
    file = open(path,'r')

    lineNumber = 0
    data = []
    allTags = []
    errors = ErrorCheck(allTags,path)
    backError:Node = None
    sortedErrors = []
    for i in range(0,len(errors)-1):
        min = i
        for j in range(i+1,len(errors)):
            # print((errors[min].line < errors[j].line) , (errors[min].line == errors[j].line and errors[min].index < errors[min].index))
            if (errors[min].line > errors[j].line) or (errors[min].line == errors[j].line and errors[min].index > errors[min].index):
                min = j
                pass
            pass
        temp = errors[i]
        errors[i] = errors[min]
        errors[min] = temp
        pass
    backErrorMisMatch:Node = None
    for line in file:
        lineNumber +=1
        line = line.strip()

            
        if errors and lineNumber == errors[0].line or backError or backErrorMisMatch :
            additionSpace = 0
            if backError:
                addition = '</' + error.tagName + '>'
                line = line[:nextTag.index] + addition + line[nextTag.index:]
                additionSpace += len(addition)
                backError = None
            pass
        
            if backErrorMisMatch and nextTag.line == lineNumber:
                addition = '</' + error.tagName + '>'
                line = line[:nextTag.index] + addition + line[nextTag.index + len(nextTag.tagName) +2:]
                additionSpace += len(addition)
                backErrorMisMatch = None
                nextTag = None
            pass
        

            while errors and errors[0].line == lineNumber :
                error:Node = errors.pop(0)
                if error.errMsg == "Missing>":
                    addition = '>'
                    index = error.index + len(error.tagName) + 1+ additionSpace
                    line = line[:index] + addition + line[index:]
                    additionSpace +=1

                elif error.errMsg == "Missing<":
                    addition = '<'
                    index = error.index - len(error.tagName) + additionSpace
                    line = line[:index] + addition + line[index:]
                    additionSpace +=1

                elif error.errMsg == "unClosedTag":
                    if error.id < len(allTags)-1:
                        nextTag:Node = allTags[error.id + 1]
                        if nextTag.line == lineNumber + 1:
                            backError = error
                            continue

                    addition = '</' + error.tagName + '>'
                    index = error.index + additionSpace + len(error.tagName) + 2
                    line = line[:index] + addition + line[index:]
                    additionSpace += len(addition)
                    pass

                elif error.errMsg == "unOpenedTag":
                    addition = '<' + error.tagName[1:] + '>'
                    if error.id-1 > 0:    
                        prevTag = allTags[error.id - 1]
                        if prevTag.line != error.line:
                            data[prevTag.line -1] += addition
                        else:
                            index = error.index + additionSpace
                            line = line[:index] + addition + line[index:]
                            additionSpace += len(addition)
                            pass
                        pass

                    else:
                        index = error.index + additionSpace
                        line = line[:index] + addition + line[index:]
                        additionSpace += len(addition)
                        pass
                elif error.errMsg == "MisMatchTag":
                    mismatchTag = error.unMatchedTag
                    addition = '</' + error.tagName + '>'
                    if error.id < len(allTags)-1:
                        nextTag:Node = mismatchTag
                        backErrorMisMatch = error
                        continue
                    else:
                        index = mismatchTag.index + additionSpace + 2
                        line = line[:index] + addition + line[(len(mismatchTag.tagName)+index):]
        data.append(line)
    dataStr = ""
    for d in data:
        dataStr += d
    return dataStr
                    


#         print(line)
#     
#     pass
# # print("************end correct************")
# dataStr = ""
# for d in data:
#     dataStr += d
#     # print(d)
# print("************end print line by line************")
# print(dataStr)
            