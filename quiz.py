
# TODO - write has_teen
def has_teen(a, b, c):
	if a >= 13 and a <= 19:
		return True

	if b >= 13 and b <= 19:
		return True

	if c >= 13 and c <= 19:
		return True

	return False

print has_teen(1, 1, 1)  # expect False
print has_teen(14, 1, 1) # expect True
print has_teen(1, 14, 1) # expect True
print has_teen(1, 1, 14) # expect True
print has_teen(14, 14, 14) # expect True
print has_teen(18, 16, 14) # expect True

# TODO - write not_string

# TODO - write icy_hot

# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
