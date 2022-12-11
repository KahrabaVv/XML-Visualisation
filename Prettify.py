def _do_pulldom_parse(func, args, kwargs):
    events = func(*args, **kwargs)
    toktype, rootNode = events.getEvent()
    events.expandNode(rootNode)
    events.clear()
    return rootNode
def parseString(string, parser=None):
    """Parse a file into a DOM from a string."""
    if parser is None:
        from xml.dom import expatbuilder
        return expatbuilder.parseString(string)
    else:
        from xml.dom import pulldom
        return _do_pulldom_parse(pulldom.parseString, (string,),
                                 {'parser': parser})
def prettify(string):
      OriginalXml = string
      temp = parseString(OriginalXml)
      new_xml = temp.toprettyxml()
      return new_xml
    
