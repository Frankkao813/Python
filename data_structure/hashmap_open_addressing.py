# HashMap implementation - using open addressing method to resolve compressor comflict
# current drawbacks on this version
# - can't handle the case when hash map is full

class HashMap:
	def __init__(self, array_size):
		self.array_size = array_size
		self.array = [None for item in range(array_size)]

	def hash(self, key, num_collision = 0):
		# using the addition result of key bytes
		key_bytes = key.encode()
		hash_code = sum(key_bytes)
		return hash_code + num_collision

	def compressor(self, hash_code):
		return hash_code % self.array_size

	# we have to store key and value at the same time
	
	def assign(self, key, value, num_collision = 0):
		ind = self.compressor(self.hash(key) + num_collision)
		curr_value = self.array[ind]


	
		#1. if there is nothing at the position
		#2. If there is already something at that position, 
		#		key is the same
			
		#print(num_collision)
		if(curr_value is None or curr_value[0] == value):
		    self.array[ind] = [key, value]
		    return

		self.assign(key, value, num_collision + 1)

	def retrieve(self, key, collision_cnt = 0):
		ind = self.compressor(self.hash(key) + collision_cnt)
		curr_value = self.array[ind]
		if(curr_value is None):
			return None
		elif(curr_value[0] == key):
			return curr_value[1]
		else:
			self.retrieve(key, collision_cnt + 1)
			
	def print_hash(self):
	    return self.array
			
	
# test code
myMap = HashMap(5);
# The two key below will cause collision (use myMap.hash(key))

result1 = myMap.assign("happy", "1") 
result2 = myMap.assign("hfppy", "2")
result3 = myMap.assign("hkppy", "3")
result4 = myMap.assign("hpppy", "4")
result5 = myMap.assign("huppy", "5") 
print(myMap.print_hash())
	