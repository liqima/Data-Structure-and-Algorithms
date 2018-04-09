class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, data):
		hash_value = self.hash(key, len(self.slots))
		if self.slots[hash_value] == None:
			self.slots[hash_value] = key
			self.data[hash_value] = data
		elif self.slots[hash_value] == key:
			self.data[hash_value] = data # replace
		else:
			next_slot = self.hash(hash_value+1, len(self.slots))
			while self.slots[next_slot] != None and self.slots[next_slot] != key and next_slot != hash_value:
				next_slot = self.hash(next_slot + 1, len(self.slots))
			if self.slots[next_slot] == None:
				self.slots[next_slot] = key
				self.data[next_slot] = data
			elif self.slots[next_slot] == key:
				self.data[next_slot] = data

	def get(self, key):
		hash_value = self.hash(key, len(self.slots))
		stop = False
		found = False
		data = None
		position = hash_value
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.hash(position + 1, len(self.slots))
				if position == hash_value:
					stop = True
		return data

	def hash(self, key, size):
		return key % size

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		return self.put(key, data)

h = HashTable()
h[54] = 'cat'
h[26] = 'dog'
h[93] = 'lion'
h[17] = 'tiger'
h[77] = 'bird'
h[31] = 'cow'
h[44] = 'goat'
h[55] = 'pig'
h[20] = 'chicken'
print(h.slots)
print(h.data)
print(h[20])
print(h[17])
