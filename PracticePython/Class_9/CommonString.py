# Common String Methods
name = "  Md. Mehedi Hasan  "   # আগে/পিছে স্পেস
print(len(name))                # মোট ক্যারেক্টার (স্পেসসহ)

trimmed = name.strip()          # শুরু/শেষের স্পেস কেটে ফেলা
print(trimmed)                  # "Md. Mehedi Hasan"

def is_null_or_empty(s):
    return s is None or s == ""

print(is_null_or_empty(name))

def is_null_or_whitespace(s):
    return s is None or s.strip() == ""

print(is_null_or_whitespace(name))

print(trimmed.upper())          # সব ক্যাপিটাল লেটারের হবে
print(trimmed.lower())          # সব স্মল লেটারের হবে

print("Hasan" in trimmed)       # সাবস্ট্রিং আছে কি? True/False
print(trimmed.startswith("Md."))# "Md." দিয়ে শুরু?
print(trimmed.endswith("Hasan"))# "Hasan" দিয়ে শেষ?

idx = trimmed.find("Mehedi")    # না পেলে -1 রিটার্ন করে
print(idx)

replaced = trimmed.replace("Mehedi", "M.")
print(replaced)                 # "Md. M. Hasan"

remove = trimmed[:10]           # index 0–9 পর্যন্ত নেবে, 10-এর পরের সব বাদ
print(remove)

part = trimmed[4:10]            # স্লাইসিং: 4 থেকে 10 (10 বাদ)
print(part)                     # "Mehedi"

# Split & Join
words = trimmed.split(" ")      # স্পেস দিয়ে ভাঙা
joined = "-".join(words)        # '-' দিয়ে জোড়া
print(joined)                   # "Md.-Mehedi-Hasan"