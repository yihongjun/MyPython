from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "The first variable is ", first
print "The second variable is ", second
print "The third variable is ", third
print "What %s do to %s"%(first, second),
action = raw_input('> ')
print "So %s %s %s"%(first, action, second)
