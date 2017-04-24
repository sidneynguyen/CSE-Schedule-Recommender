"""PrereqGraph.py"""

class PrereqGraph(object):
    """PrereqGraph"""
    def __init__(self):
        self.graph = dict()

    def insert(self, node):
        """insert"""
        self.graph[node.getCourseName()] = node

    def getnode(self, coursename):
        """getNode"""
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
