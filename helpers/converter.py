import re


class xmlTreeNode:
    def __init__(self, name, value, parent):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []

    def __str__(self):
        return f"Name: {self.name} Value: {self.value} Parent: {self.parent} Children: {self.children}"

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__


def xmlPayloadToTree(payload: str) -> xmlTreeNode:
    # Create a root node
    root = xmlTreeNode(None, None, None)

    currentNodes = [root]

    for line in payload.splitlines():
        line = line.strip()
        if line == "":
            continue

        if line.startswith("<"):
            # This is a tag
            if line.startswith("</"):
                # This is a closing tag
                currentNodes.pop()
            else:
                # This is an opening tag
                # Get the tag name
                tagName = line.split(" ")[0][1:]

                # Remove > from the end of the tag
                if tagName.endswith(">"):
                    tagName = tagName[:-1]

                # Get the tag value
                tagValue = line.split(">")[1]

                # Create a new node
                newNode = xmlTreeNode(tagName, tagValue, currentNodes[-1])

                # Add the new node to the current node
                currentNodes[-1].children.append(newNode)

                # Add the new node to the current nodes
                currentNodes.append(newNode)
        else:
            # This is a value
            currentNodes[-1].value = line

    return root


def xmlTreeToJSON(root: xmlTreeNode) -> str:
    if root.children == []:
        return f'"{root.name}": "{root.value}"'

    output = ""

    if root.parent is None:
        output += "{"
    else:
        output += f'"{root.name}": {{'

    for child in root.children:
        # Check if the child has children with the same name
        if len(child.children) > 0:
            # Check if the child has children with the same name
            if len(child.children) > 0 and child.children[0].name == child.children[-1].name:
                # Case 4
                output += f'"{child.name}": ['
                count = len(child.children)
                for grandchild in child.children:
                    output += "{"
                    output += xmlTreeToJSON(grandchild)
                    if count > 1:
                        output += "},"
                    else:
                        output += "}"
                    count -= 1
                output += "]"
            else:
                # Case 5
                output += xmlTreeToJSON(child)
        else:
            # Case 3
            output += f'"{child.name}": "{child.value}"'

        if child != root.children[-1]:
            output += ","

    output += "}"
    return output


def xmlToJSON(payload: str) -> str:
    return xmlTreeToJSON(xmlPayloadToTree(payload))
