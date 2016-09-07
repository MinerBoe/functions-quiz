
# TODO - write has_teen
def has_teen(a, b, c):
	if a >= 13 and a <= 19:
		return True

	if b >= 13 and b <= 19:
		return True

	if c >= 13 and c <= 19:
		return True

	return False

print has_teen(1, 1, 1)    # expect False
print has_teen(20, 20, 20) # expect False
print has_teen(14, 1, 1)   # expect True
print has_teen(1, 14, 1)   # expect True
print has_teen(1, 1, 14)   # expect True
print has_teen(14, 14, 14) # expect True
print has_teen(18, 16, 14) # expect True

print
# TODO - write not_string


def icy_hot(x, y):
	hot = False
	cold = False

	if x > 100 or y > 100:
		hot = True

	if x < 0 or y < 0:
		cold = True

	if cold and hot:
		return True

	return False

print icy_hot(50, 50) # expect False
print icy_hot(110, -10) # expect True
print icy_hot(-10, 110) # expect True

# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
