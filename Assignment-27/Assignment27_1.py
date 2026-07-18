class BookStore :

	NoOfBooks = 0

	def __init__(self,bookname,bookauthor) :
		self.Name = bookname
		self.Author = bookauthor
		BookStore.NoOfBooks += 1

	def Display(self) :
		print(f"{self.Name} by {self.Author}.\nNo of Books : {BookStore.NoOfBooks}")

Obj1 = BookStore("Linux System Programming","Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming","Dennis Ritchie")
Obj2.Display()