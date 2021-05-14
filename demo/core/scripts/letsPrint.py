import omni.ext

# Classes inheriting from "omni.ext.IExt" would be auto instantiated at runtime
# and the on_startup would be called. Besides, on_shutdown will be called while 
# disabling this extension from the Extensions menu
class LetsPrint(omni.ext.IExt):
	def __init__(self):
		self.printer = Printer()

	def on_startup(self):
		print("Starting Up [epg.browser]")

	def on_shutdown(self):
		print("Shuting Down [epg.browser]")

	def delegatedPrint(self):
		self.printer.printSomething()


class Printer():
	def __init__(self):
		print("Printer Initialized")

	def printSomething(self):
		print("PRINTING SOMETHING NOW!!!")
