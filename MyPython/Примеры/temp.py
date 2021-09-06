class Foo(object):
	val = 0
	def fun(self):
		try:
			return self.val[-1]
		except TypeError:
			return self.val
o=Foo()
o.val=[1,2,3,4]
print о.fun(),
o.val='1234'
print (o.fun())
