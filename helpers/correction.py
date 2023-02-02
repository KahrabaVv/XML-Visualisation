from helpers.validation import ErrorCheck, Node


def correction(path: str = None) -> str:
    file = open(path, 'r')
    line = ""
    for inline in file:
        line += inline.strip()
        pass
    allTags = []
    errors = ErrorCheck(allTags, path, True)
    for i in range(0, len(errors) - 1):
        min = i
        for j in range(i + 1, len(errors)):
            if (errors[min].index > errors[j].index):
                min = j
                pass
            pass
        temp = errors[i]
        errors[i] = errors[min]
        errors[min] = temp
        pass
    solvedErrors = []
    additionSpace = 0
    for ind in range(0, len(line)):
        while errors and errors[0].index == ind:
            error: Node = errors.pop(0)
            if error.errMsg == "Missing>":
                addition = '>'
                index = error.index + len(error.tagName) + additionSpace + 1
                line = line[:index] + addition + line[index:]
                additionSpace += 1
            elif error.errMsg == "Missing<":
                addition = '<'
                index = error.index - len(error.tagName) + additionSpace
                line = line[:index] + addition + line[index:]
                additionSpace += 1
            elif error.errMsg == "unClosedTag":
                addition = '</' + error.tagName + '>'
                index = error.index + additionSpace + len(error.tagName) + 2
                line = line[:index] + addition + line[index:]
                additionSpace += len(addition)
                pass
            elif error.errMsg == "unOpenedTag":
                addition = '<' + error.tagName[1:] + '>'
                index = error.index + additionSpace
                line = line[:index] + addition + line[index:]
                additionSpace += len(addition)
                pass
            elif error.errMsg == "MisMatchTag":
                addition = '</' + error.tagName + '>'
                index = error.index + additionSpace
                for er in solvedErrors:
                    if er.index == error.index:
                        index -= 1
                line = line[:index] + addition + line[index + len(error.unMatchedTag.tagName) + 2:]
                additionSpace += len(addition) - 2 - len(error.tagName)
                pass
            solvedErrors.append(error)
            pass
    return line
