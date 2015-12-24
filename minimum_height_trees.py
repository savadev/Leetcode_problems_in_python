class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]

        The problem is to find the trees with minimum height.
        Given: An undirected graph with edges
        Output: The roots of the trees which has minimum heights

        Approach1 : Naive
        construct a tree for each vertex and return the list of the tree's root which 
        has minimum height

        Approach 2: Most effecient one.

        Cut the leaves of the tree level by level. 
        Stop when the number of nodes is equal to or less than 2.

        There will be atleast 1 or atmost 2 trees with minumum height for any undirected graph (?)

        Now rather than forming a adj_list and constructing tree for each node,
        remove the leaves from the adj_list. (both in key and values)

        Now do this in a loop untill the number of keys in the adj_list is 2 or less than it.

        The keys of adj_list is the list of trees 
        """
        # Make an adjacency list
        adj_list = collections.defaultdict(set)
        for s,t in edges:
            adj_list[s].add(t)
            adj_list[t].add(s)
        vertices = adj_list.keys()
        while len(vertices) > 2:
            #print vertices
            # Get leaves
            leaves = [k for k,v in adj_list.items() if len(v) == 1]
            for each_leaf in leaves:
                # Remove it from other vertices
                vertices.remove(each_leaf)
                for each_v in adj_list[each_leaf]:
                    adj_list[each_v].remove(each_leaf)
                del adj_list[each_leaf]
        return vertices if len(vertices) != 0 else [0]
            
        '''
        Same problem with most elegant and effecient way of implementing
        The below code doesn't create dict

        It does everthing with list
        so adj_list = [set(), set(), set()]

        Now find the 1st level of the leaves

        Now inside the while loop rather find the subsequent levels of leaves everytime from adj list
        find the next level of leaves only from the nodes that are neighbouring nodes of the previous leaves
        this reduces the time drastically.
        '''  
        def findMinHeightTrees(self, n, edges):
            if n == 1: return [0] 
            adj = [set() for _ in xrange(n)]
            for i, j in edges:
                adj[i].add(j)
                adj[j].add(i)

            leaves = [i for i in xrange(n) if len(adj[i]) == 1]

            while n > 2:
                n -= len(leaves)
                newLeaves = []
                for i in leaves:
                    j = adj[i].pop()
                    adj[j].remove(i)
                    if len(adj[j]) == 1: newLeaves.append(j)
                leaves = newLeaves
            return leaves
        '''
        Naive Approach
        '''
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Make an adjacency list
        adj_list = dict()
        min_height_list = list()
        min_height = float('inf')
        for each_edge in edges:
            left = each_edge[0]
            right = each_edge[1]
            if left not in adj_list:
                adj_list[left] = []
            adj_list[left].append(right)
            if right not in adj_list:
                adj_list[right] = []
            adj_list[right].append(left)
        print "adj_list", adj_list
        for each_vert, n_nodes in adj_list.items():
            # consider it as root and find it height
            processed_nodes = []
            height = 0
            processed_nodes.append(each_vert)
            n_nodes.append(None)
            while len(n_nodes) != 0:
                print "N-nods", n_nodes, processed_nodes
                element = n_nodes.pop(0)
                print "popped elemt", element
                if element == None:
                    height += 1
                elif element not in processed_nodes:
                    processed_nodes.append(element)
                    flag = False
                    print adj_list[element]
                    for each_n in adj_list[element]:
                        print element, each_n
                        if each_n not in processed_nodes:
                            n_nodes.append(each_n)
                            flag = True
                    if flag:
                        n_nodes.append(None)
            if height < min_height:
                min_height = height
                min_height_list = [each_vert]
            elif height == min_height:
                min_height_list.append(each_vert)
            print "each_vert", each_vert, height
        print adj_list
        return min_height_list
            
                
        