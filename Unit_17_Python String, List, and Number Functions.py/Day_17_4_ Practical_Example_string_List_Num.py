# Practical Example_String,Number and List Function

#1.Example:

# list =["mobile","LAPtop","tablet"]
# CLEAN=[p.strip().title() for p in list ]
# CLEAN.sort()
# print(CLEAN)

# 2. Example:

mobiles = ["9876543210", "9988AB2211", "12345"]

valid = [m for m in mobiles if m.isdigit() and len(m) == 10]

print(valid)

# 3. Example:

mobiles = ["9876543210", "9988AB2211", "12345"]

valid = []

for m in mobiles:
    if m.isdigit() and len(m) == 10:
        valid.append(m)

print(valid)

# 4. Example:

emails = ["rohit@gmail.com", "snehal@yahoo.com"]
domains = [mail[mail.find("@")+1:] for mail in emails]
print(domains)

