#------------------------------------------------------------------------------------------------------------------
#   Maze solver using different search strategies.
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
import math

#------------------------------------------------------------------------------------------------------------------
#   Class TreeNode
#------------------------------------------------------------------------------------------------------------------
class TreeNode:
    """ 
        Class that is used to represent a node in the search algorithm. A node contains the following elements:
        * A reference to its parent.
        * The position in the map that is represented by the node.
        * The total path cost from the initial position to the current position.
    """   
    
    def __init__(self, parent, s, c):
        """ 
            This constructor initializes a node. 
            
            param parent: The node parent.
            param s: The current position that is represented by the node.
            param c: The path cost to the current position from the initial position.
        """
        self.parent = parent
        self.s = s
        self.c = c
        
    def __lt__(self, node):
        """ 
            Operator <. This definition is requiered by the PriorityQueue class.
        """
        return False;


    def path(self):
        """ 
            This method builds a list with the vertices of the path from the root to the node.
            
            return: The path from the root to the node
        """
        node = self
        path = [] 
        while node != None:
            path.insert(0, node.s)
            node = node.parent                
        return path;

#------------------------------------------------------------------------------------------------------------------
#   Breadth-first search algorithm
#------------------------------------------------------------------------------------------------------------------
def maze_bfs(maze, s0, sg):
    """ 
        This method finds a path in a maze from an initial position s0 to a goal position sg using the 
        breadth-first search algorithm.
            
        param maze: The map of the maze.
        param s0: The initial position.
        param sg: The goal position.
        return: A tuple with the path from s0 to sg and its cost, or null if there is no a path.
    """

    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = Queue()
    frontier.put(TreeNode(None, s0, 0))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                frontier.put(TreeNode(node, neighbor, node.c + 1))
                
        # Add node to the explored set
        explored_set[node.s] = 0  

#------------------------------------------------------------------------------------------------------------------
#   Depth-first search algorithm
#------------------------------------------------------------------------------------------------------------------
def maze_dfs(maze, s0, sg):
    """ 
        This method finds a path in a maze from an initial position s0 to a goal position sg using the 
        depth-first search algorithm.
            
        param maze: The map of the maze.
        param s0: The initial position.
        param sg: The goal position.
        return: A tuple with the path from s0 to sg and its cost, or null if there is no a path.
    """

    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = LifoQueue()
    frontier.put(TreeNode(None, s0, 0))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                frontier.put(TreeNode(node, neighbor, node.c + 1))
                
        # Add node to the explored set
        explored_set[node.s] = 0  
        
#------------------------------------------------------------------------------------------------------------------
#   Uniform-cost search algorithm
#------------------------------------------------------------------------------------------------------------------
def maze_ucs(maze, s0, sg):
    """ 
        This method finds a path in a maze from an initial position s0 to a goal position sg using the 
        uniform-cost search algorithm.
            
        param maze: The map of the maze.
        param s0: The initial position.
        param sg: The goal position.
        return: A tuple with the path from s0 to sg and its cost, or null if there is no a path.
    """

    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, s0, 0)))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()[1]
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                frontier.put((node.c + 1, TreeNode(node, neighbor, node.c + 1)))
                
        # Add node to the explored set
        explored_set[node.s] = 0  
       
#------------------------------------------------------------------------------------------------------------------
#   A* search algorithm
#------------------------------------------------------------------------------------------------------------------
def maze_astar(maze, s0, sg):
    """ 
        This method finds a path in a maze from an initial position s0 to a goal position sg using the 
        a-star algorithm.
            
        param maze: The map of the maze.
        param s0: The initial position.
        param sg: The goal position.
        return: A tuple with the path from s0 to sg and its cost, or null if there is no a path.
    """

    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, s0, 0)))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()[1]
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                
                # Calculate squared distance to the goal
                h = math.sqrt((neighbor[0]-sg[0])**2 + (neighbor[1]-sg[1])**2)
                g = node.c + 1
                f = g + h
                
                # Add new node
                frontier.put((f, TreeNode(node, neighbor, g)))
                
        # Add node to the explored set
        explored_set[node.s] = 0  
        
#------------------------------------------------------------------------------------------------------------------
#   IDA* search algorithm
#------------------------------------------------------------------------------------------------------------------
def maze_idastar(maze, s0, sg, flimit = 1):
    """ 
        This method finds a path in a maze from an initial position s0 to a goal position sg using the 
        iteerative deepening a-star algorithm.
            
        param maze: The map of the maze.
        param s0: The initial position.
        param sg: The goal position.
        param flimit: The limit of the value for ordering the nodes.
        return: A tuple with the path from s0 to sg and its cost, or null if there is no a path.
    """

    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, s0, 0)))

    # Initialize explored set
    explored_set = {}
    
    # Initialize next limit value
    fnext = 100000000000
    flimitChanged = False
    
    # Find path
    while True:
        if frontier.empty():
            if not flimitChanged:
                # In this case, the limit has not changed, so there is no solution.
                return None
            else:
                # In this case, there is at least one node that have surprass the initial limit. Try again using fnext.
                return maze_idastar(maze, s0, sg, fnext) 
        
        # Get node from frontier
        node = frontier.get()
        fval = node[0]
        node = node[1]
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            # Check if the f value of the node is below the limit.
            if fval <= flimit:
                neighbors = []
            
                # Check possible neighbors
                row = node.s[0]
                col = node.s[1]

                if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                    neighbors.append((row - 1, col))

                if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                    neighbors.append((row + 1, col))
        
                if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                    neighbors.append((row, col-1))

                if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                    neighbors.append((row, col+1))

                # Add neighbors to the frontier
                for neighbor in neighbors:
                
                    # Calculate squared distance to the goal
                    h = math.sqrt((neighbor[0]-sg[0])**2 + (neighbor[1]-sg[1])**2)
                    g = node.c + 1
                    f = g + h
                
                    # Add new node
                    frontier.put((f, TreeNode(node, neighbor, g)))    
                    
            else:
                fnext = min(fnext, fval)
                flimitChanged = True
                
        # Add node to the explored set
        explored_set[node.s] = 0  
        
#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

# Initialize map
# initial_position = (1, 2)
# goal_position = (19, 23)
# #          01234567890123456789012345678
# maze =  ( '++++++++++++++++++++++++++++++',
#           '+ S                          +',
#           '+++++++++ +++++++ ++++++ + +++',
#           '+       +      +       +     +',
#           '+ +++ + +++++++ + +++++ +   ++',
#           '+   +       +   +   +        +',
#           '++ +++++++ + +++++ + +++++  ++',
#           '+    +      + +   + +        +',
#           '++++ +++++++++++++++ +++++  ++',
#           '+      +         +   +       +',
#           '+ +++++++ + +++++ + +++++   ++',
#           '+       +   +   +   +        +',
#           '+ +++ + + +++++++++++++++   ++',
#           '+   + +   +             +    +',
#           '+ + + +++++++++++ +++++++++  +',
#           '+ +     +     +   +          +',
#           '+ ++++ + + + + +++++ ++++++  +',
#           '+      +   + + +     +       +',
#           '++++++++++++++ ++++++++  +++++',
#           '+                            +',
#           '++++++++++++++++++++++++++++++')

# initial_position = (3,0)
# goal_position = (18, 7)
# #         0123456789012345678
# maze =  ('+++++++++++++++++++',
#          '+   +     +       +',
#          '+ +++ + +++++ +++ +',
#          '      +   +   +   +',
#          '+++++++++ + +++++ +',
#          '+         +   +   +',
#          '+ +++++ + +++ +++ +',
#          '+   + +   +     + +',
#          '+ + + +++ + +++ + +',
#          '+ + +   +   +   + +',
#          '+++ +++ +++++++++++',
#          '+   +         +   +',
#          '+ + + +++ + ++++ ++',
#          '+ + + +   +       +',
#          '+ +++ +++++++++++ +',
#          '+     +       +   +',
#          '+++ +++ +++ +++++ +',
#          '+   +             +',
#          '+++++++ +++++++++++')    

initial_position = (1,2)
goal_position = (1,19)
maze = ('++++++++++++++++++++++',
        '+   +   ++ ++        +',
        '+     +     +++++++ ++',
        '+ +    ++  ++++ +++ ++',
        '+ +   + + ++         +',
        '+          ++  ++  + +',
        '++ ++ + +      ++  + +',
        '++ ++ +++  + +  ++   +',
        '+          + +  + +  +',
        '+++++ +  + + +       +',
        '++++++++++++++++++++++')

#### Solve maze using BFS ####
print("***** BFS *****")
result = maze_bfs(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('X', end = '')
        elif ((r,c) == goal_position):
            print('O', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using DFS ####
print("***** DFS *****")

result = maze_dfs(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('X', end = '')
        elif ((r,c) == goal_position):
            print('O', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using UCS ####
print("***** UCS *****")

result = maze_ucs(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('X', end = '')
        elif ((r,c) == goal_position):
            print('O', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using A-Star ####
print("***** A-Star *****")

result = maze_astar(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('X', end = '')
        elif ((r,c) == goal_position):
            print('O', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using IDA-Star ####
print("***** IDA-Star *****")

result = maze_idastar(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('X', end = '')
        elif ((r,c) == goal_position):
            print('O', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
