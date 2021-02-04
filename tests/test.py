import basically_ti_basic as btb
import traceback

FILE = "test.8Xp"

print("")
print("")
print(u"\u001b[33m===================================================================\u001b[0m")
print(u"\u001b[36mInitializing test! (1/2)")
try:
	print(u"\u001b[33m===================================================================\u001b[0m")
	print("btb.decompile_file(FILE, \"output.txt\")")
	btb.decompile_file(FILE, "output.txt")
	print(u"\u001b[33m===================================================================\u001b[0m")
	print("")
except Exception as e:
	print(u"\u001b[31m===================================================================\u001b[0m")
	print(u"\u001b[31mWhoops! Error on calling decompile_file!\u001b[0m")
	traceback.print_exc()
	print(u"\u001b[31m===================================================================\u001b[0m")
	exit(2)
print(u"\u001b[33m===================================================================\u001b[0m")
print(u"\u001b[32mSuccessful Test! (1/2 COMPLETE)\u001b[0m")
print(u"\u001b[33m===================================================================\u001b[0m")
print(u"\u001b[36mInitializing test! (2/2)")
try:
	print(u"\u001b[33m===================================================================\u001b[0m")
	btb.compile_file("output.txt", "newlyCompiled.8Xp")
	print("btb.compile_file(\"output.txt\", \"newlyCompiled.8Xp\")")
	print(u"\u001b[33m===================================================================\u001b[0m")
	print("")
except Exception as e:
	print(u"\u001b[31m===================================================================\u001b[0m")
	print(u"\u001b[31mWhoops! Error on calling compile_file!\u001b[0m")
	traceback.print_exc()
	print(u"\u001b[31m===================================================================\u001b[0m")
	exit(2)
print(u"\u001b[33m===================================================================\u001b[0m")
print(u"\u001b[32mSuccessful Test! (2/2 COMPLETE)\u001b[0m")
print(u"\u001b[35mTerminating!\u001b[0m")
print(u"\u001b[33m===================================================================\u001b[0m")
exit()