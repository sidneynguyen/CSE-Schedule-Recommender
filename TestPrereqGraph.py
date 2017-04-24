"""TestPrereqGraph"""

from PrereqGraph import PrereqGraph
from PrereqGraph import PrereqNode

# Test PrereqNode
TEST_NODE_1 = PrereqNode("CSE 100", ["CSE 21", "CSE 12", "CSE 15L", "CSE 30"])
assert TEST_NODE_1.getCourseName() == "CSE 100"
assert TEST_NODE_1.getPrereqList() == ["CSE 21", "CSE 12", "CSE 15L", "CSE 30"]

print "All PrereqNode tests passed"

# Test PrereqGraph
TEST_GRAPH_1 = PrereqGraph()
TEST_GRAPH_1.insert(TEST_NODE_1)
assert TEST_GRAPH_1.getNode("CSE 100") == TEST_NODE_1

print "All PrereqGraph tests passed"
