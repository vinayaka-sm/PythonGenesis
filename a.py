""" 
TEAM 5
PATTERN MATCHING

"""
import io
class Demo:
	""" CREATING CLASS"""
	def __init__(self):
		""" CONSTRUCTOR"""
		self.myfile=None
	def read_file(self):
		""" to read file """
		self.myfile=io.open("input.txt","r",encoding='utf8')
		print("File Readed Succesfully")
	def put_file(self,file_name,line):
		"""WRITING INTO NEW FILE"""
		out_file=open(file_name,"a",encoding='utf8')
		out_file.write(line)
		out_file.close()
	def process_file(self,key):
		"""main"""
		k=0
		self.read_file()
		lines=self.myfile.readlines()
		for line in lines:
			if key in line:
				self.put_file(key+".txt",line)
				k=k+1
		print(key,k)
		return k
obj=Demo() 
x= int(input("ENTER total number of words to search"))  
for i in range(x):
	obj.process_file(input("enter a word to search:"))