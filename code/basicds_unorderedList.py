class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def setData(self, newdata):
		self.data = newdata

	def getNext(self):
		return self.next

	def setNext(self, newnext):
		self.next = newnext

class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self, item):
		found = False
		current = self.head
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head == current.get()
		else:
			previous.setNext(current.getNext())

	def index(self, item):
		current = self.head
		found = False
		index = 0
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				index += 1
				current = current.getNext()
		if not found:
			raise ValueError(str(item)+' not in this list')
		return index

