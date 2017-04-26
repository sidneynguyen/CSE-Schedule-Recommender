"""PrereqGraph.py"""

class PrereqGraph(object):
    """PrereqGraph"""
    def __init__(self):
        self.graph = dict()

    def insert(self, node):
        """Insert a node into the graph"""
        self.graph[node.getcoursename()] = node

    def getnode(self, coursename):
        """Get the node given the course name"""
        return self.graph[coursename]

class PrereqNode(object):
    """PrereqNode"""
    def __init__(self, coursename, prereqlist):
        self.coursename = coursename
        self.prereqlist = prereqlist

    def getcoursename(self):
        """getcoursename"""
        return self.coursename

    def getprereqlist(self):
        """getprereqlist"""
        return self.prereqlist
