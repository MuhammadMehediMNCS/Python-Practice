# Strings Are Immutable
s = "A"
s += "B"             # নতুন "AB" অবজেক্ট
s += "C"             # নতুন "ABC" অবজেক্ট
print(s)

parts = []
for i in range(3):
    parts.append(str(i))   # লিস্টে যোগ করা সস্তা
result = "".join(parts)    # এক ধাপে স্ট্রিং বানাও
print(result)              # "012"