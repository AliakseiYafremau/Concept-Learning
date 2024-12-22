class Life:
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        if self.a < 100:
            self.a += 1
            return self.a
        else:
            raise StopIteration


mylife = Life()
for i in mylife:
    print(i)
