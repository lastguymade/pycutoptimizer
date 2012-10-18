class Vector:
	def __init__(self, data, func):
		self.data = []
		self.func = func

		for d1 in data:
			if (len(self.data) == 0):
				self.data.append(d1)
			else:
				count = 0
				for d2 in self.data:
					if self.func(d2, d1):
						count += 1
					else:
						break
				self.data.insert(count, d1)

	def __getitem__(self, index):
		return self.data[index]

	def __setitem__(self, key, item):
		self.data[key] = item

	def __len__(self):
		return len(self.data)

	def __add__(self, item):
		if (len(self.data) == 0):
			self.data.append(item)
		else:
			count = 0
			for d1 in self.data:
				if self.func(d1, item):
					count += 1
				else:
					break
			self.data.insert(count, item)
		return self.data
