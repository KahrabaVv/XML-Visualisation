import re

ConvertingData = ""


class TreeLeaf:
    def _init_(self):
        self.__Children = []
        self.__Value = None
        self.__Tag = None
        self.__Parent = None

    @property
    def Children(self):
        return self.__Children

    @Children.setter
    def Children(self, value):
        self.__Children.append(value)

    def getAllChildren(self):
        return self.__Children

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        self.__Value = value

    @property
    def Tag(self):
        return self.__Tag

    @Tag.setter
    def Tag(self, value):
        self.__Tag = value

    @property
    def Parent(self):
        return self.__Parent

    @Parent.setter
    def Parent(self, value):
        self.__Parent = value

    @staticmethod
    def ParseXml(FilePath):
        Xml = ""
        with open(FilePath, 'r') as f:
            Xml = f.read()
            Xml = re.sub('\s+', '', Xml)
        f.close()
        Root = TreeLeaf()

        TreeLeaf.Parsing(Xml, 0, Root, True)
        return Root.Children[0]

    @staticmethod
    def Parsing(Xml, ind, Node, NotFirstNone = False):
        if (Node is None and NotFirstNone is False) or ind >= len(Xml):
            return
        while ind < len(Xml):
            char = Xml[ind]
            ind += 1
            if ind >= len(Xml):
                break
            if char == '<' and Xml[ind] != '/':
                child = TreeLeaf()
                child.Parent = Node
                Node.Children = child
                i = 0
                end = 0
                for c in Xml[ind - 1:]:
                    i += 1
                    if c == '>':
                        end = i
                        break
                child.Tag = Xml[ind: ind + end - 2]
                ind += end - 1
                if ind > len(Xml):
                    break
                char = Xml[ind]
                if char == '<':
                    TreeLeaf.Parsing(Xml, ind, child)
                    return
                else:
                    i = 0
                    end = 0
                    start = 0
                    for c in Xml[ind:]:
                        i += 1
                        if c == '<':
                            start = i - 1
                        if c == '>':
                            end = i
                            break
                    child.Value = Xml[ind: ind + start]
                    ind += end
                    TreeLeaf.Parsing(Xml, ind, child.Parent)

                    return
            else:

                i = 0
                end = 0
                for c in Xml[ind - 2:]:
                    i += 1
                    if c == '>':
                        end = i
                        break
                ind += end - 2
                TreeLeaf.Parsing(Xml, ind, Node.Parent)
                return


def ConvertToJson(Root):
    global ConvertingData
    ConvertingData = "{"
    ConvertingNodes(Root)
    ConvertingData += "}"
    return ConvertingData


def ConvertingNodes(Node):
    global ConvertingData
    if Node.Value is None:
        ConvertingData += '"' + Node.Tag + '":{'
        ind = 0
        length = len(Node.Children)
        for child in Node.Children:
            ConvertingNodes(child)
            ind += 1
            if ind != length:
                ConvertingData += ","
        ConvertingData += "}"
    else:
        ConvertingData += '"' + Node.Tag + '":"' + Node.Value + '"'
    return
