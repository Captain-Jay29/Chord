class FingerTable:

	def __init__(self, node):
		self.node = node
		self.fingerTable = [node]*8


	def set(self, index, successor):
		self.fingerTable[index] = successor


	def get(self, index):
		return self. fingerTable[index]


	def prettyPrint(self):

		print(f'----------Node id: {self.node.id}----------')
		print(f'Successor: {self.node.successor.id}, \tPredecessor: {self.node.predecessor.id}')
		print(f'FingerTables:')

		for i in range(8):
			print(f'| {i} =  \t[{self.node.id + 2**i}, {self.node.id + 2**(i+1)}) \tsucc. = {self.fingerTable[i].id if self.fingerTable[i] else -1}')


		print(f'--------------------------------------')
		print(f'**************************************\n')
		




	