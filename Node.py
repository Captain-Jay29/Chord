from FingerTable import FingerTable

class Node:



	def __init__(self, id):

		self.id = id
		self.fingerTable = FingerTable(self)
		self.successor = self
		self.predecessor = self
		self.localkeys = {}




	def validateNode(self, key, flag):

		"""
	    Checks if the current node is responsible for the given key.

	    Args:
	        key: The key to check.
	        flag: A flag checker

	    Returns:
	        The node responsible for the key, or None if not found.
	    """

		'''if key == self.id:
			return self

		if (self.predecessor == self):

			if self.successor == self:

				if flag:
					return self.predecessor

				return self


		if (self.predecessor.id > self.id):

			if (key > self.predecessor.id):
				return self

			if (key < self.predecessor.id and key < self.id):
				return self


		if (self.predecessor.id > self.id and key < self.id and key > self.predecessor.id):
			return self'''





		if key == self.id:
			return self
            

		if (self.predecessor == self == self.successor):

			if flag:
				return self.predecessor

			return self

		if (self.predecessor.id < key < self.id):
			return self

		if (self.predecessor.id > self.id):

			if (key > self.predecessor.id):
				return self


			if (key < self.predecessor.id and key < self.id):
				return self

		if (self.predecessor.id > self.id and key < self.id and key > self.predecessor.id):
			return self


        
        
             
                            
        
            





	def mapping(self, key, flag=False):

		"""
	    Finds the node responsible for storing the key-value pair for the given key.

	    Args:
	        key: The key to search for.
	        flag: A flag checker

	    Returns:
	        The node responsible for the key, or None if not found.
	    """

		target = self.validateNode(key, flag)
		
		if target:
			return target

		if key < self.id:
			distance = 256 - self.id + key

		else:
			distance = key - self.id


		e = -1
		while distance:
			distance //= 2
			e += 1

		server = self.fingerTable.get(e)

		if target:
			return target


		if (server.predecessor.id > key) and (server.predecessor == self):
			return server.predecessor

		else:
			return server.mapping(key, flag)





	def find(self, key):

		"""
	    Finds the value associated with a given key in the DHT network.

	    Args:
	        key: The key to search for.
	    """

		target = self.mapping(key, true)

		if key not in target.localkeys:
			print(f'key {key} not found\n')

		else:
			print(f'Value for key {key} is {target.localkeys[key]}\n')



	def insert(self, key, target):

		if target:
			target = int(target)

		"""
	    Inserts a key-value pair into the DHT network.

	    Args:
	        key: The key to associate the value with.
	        target: The value to store.
	    """


		target_node = self.mapping(key, True)
		target_node.localkeys[key] = target



	def remove(self, key):

		"""
	    Removes a key-value pair into the DHT network.

	    Args:
	        key: The key to associate the value with.
	    """

		self.localkeys.pop(key)





	def relocate(self, successor):

		"""
	    Relocate keys from the successor node to the current node when the current node joins the network.

	    Args:
	        successor: The successor node in the DHT network.
	    """

		all_keys = successor.localkeys.copy()

		relocate = []
		delete = []

		migrate = False
		for key, val in all_keys.items():
			flag = False

			if key <= self.id < self.successor.id:
				flag = True

			elif (self.id > self.successor.id) and (key > self.successor.id) and (key < self.id):
				flag = True

			elif (self.id < self.successor.id) and (key > self.successor.id):
				flag = True

			if flag:
				migrate = True

				print(f'migrate key {key} from node {successor.id} to node {self.id}')

				relocate.append(key)
				self.localkeys[key] = val
				delete.append(key)

			


		for key in delete:
			successor.remove(key)

		'''if relocate:
			print(f'Changes keys: {relocate}')

			for key in relocate:
				print(f'Changed key: {key}, from node: {successor.id} to node: {self.id}\n')'''





	def prettyPrint(self):

		print(f'----------Node id: {self.id}----------')
		print(f'{self.localkeys}\n')





	def remove_function(self, key):

		"""
	    Removes a key-value pair into the DHT network after finding it.

	    Args:
	        key: The key to associate the value with.
	    """

		target = self.mapping(key, True)

		if target not in target.localkeys:
			print(f'key {key} not found')

		else:
			target.remove(key)
			print(f'Removing key \t{key} with value \t{target.localkeys[key]}\n')





	def findall(self, start_node, depth):

		"""
	    Looks up all key-value pairs in the network and prints them.

	    Args:
	        start_node: The node where the lookup started.
	        depth: The current depth of the recursive search.
	    """


		if start_node == self and depth > 0:
			return

		if not depth:
			print(f'----------- node {self.id} -----------')

		path = [start_node.id]

		if start_node != self:
			path.append(self.id)

		for k, v in self.localkeys.items():

			print(f'Lookup result of key {k} from node {start_node.id} with path {path} value is {v}')

		

		self.successor.findall(start_node, depth + 1)

		print('\n')





	def update(self):

		"""
	    Updates the finger table of the current node in the DHT network.

	    This function is usually called after a new node joins the network or when a node leaves the network.
	    """

		allNodes = self.listofNodes([], self, 0)
		allNodes.sort(key = lambda x: x.id)

		for node in allNodes:
			for e in range(8):

				diff = node.id + 2**e
				node.fingerTable.set(e, self.binarySearching(allNodes, diff))





	def listofNodes(self, listN, start_node, depth):

		"""
	    Collects all nodes in the DHT network.

	    Args:
	        listN: A list to store discovered nodes.
	        start_node: The node where the search started.
	        depth: The current depth of the recursive search.
	    """

		if start_node == self and depth > 0:
			return

		listN.append(self)
		self.successor.listofNodes(listN, start_node, depth + 1)
		
		return listN





	def binarySearching(self, allNodes, target_id):

		"""
	    Finds the node responsible for a given target ID using binary search.

	    Args:
	        allNodes: A sorted list of all nodes in the network.
	        target_id: The ID to search for.

	    Returns:
	        The node responsible for the target ID.
	    """

		target = target_id % 256

		if target > allNodes[-1].id:
			return allNodes[0]

		l, r = 0, len(allNodes)

		while l<=r:

			mid = (l+r)//2

			if target == allNodes[mid].id:
				return allNodes[mid]

			elif target > allNodes[mid].id:
				l = mid + 1

			else: 
				r = mid - 1

		return allNodes[l]






	def join (self, node):

		"""
	    Joins the DHT network by connecting to an existing node and informing it.

	    Args:
	        node: The existing node to connect to.
	    """

		if node != None:

			self.successor = node.mapping(self.id)
			
			# if self.successor.predecessor:
			self.predecessor = self.successor.predecessor
			
			self.successor.predecessor = self
			self.predecessor.successor = self

			self.relocate(self.successor)

		self.update()





	def leave(self):

		"""
	    Leaves the DHT network by notifying the successor and predecessor.

	    """

		self.predecessor.successor = self.successor
		self.successor.predecessor = self.predecessor

		for k, v in self.localkeys.items():

			if k <= self.id:

				print(f'Migrate key {k} from {self.id} to node {self.successor.id}\n')

				self.successor.localkeys[k] = v

		self.successor.update()
























		    		
		    		
		    		


			



		    
		    


		    

		    	

		    	
		    		

		    	
		    		

		    	
		    		


		    	


		    
		    	


		    
		    	

		    	

		    		












			
















