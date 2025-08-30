# # Python-এ C#-এর মতো বিল্ট-ইন extension method নেই। সাধারণ প্র্যাক্টিস:
# # (ক) হেল্পার ফাংশন বানাও (সবচেয়ে সাধারণ ও নিরাপদ)
# # (খ) কাস্টম ক্লাস/র‍্যাপার তৈরি করো (যদি অবজেক্ট-ওরিয়েন্টেড API চাও)
# # ক) হেল্পার ফাংশন :
# import re
#
# def to_slug(value: str) -> str:
#     if value is None or value.strip() == "":
#         return ""
#     lower = value.strip().lower()
#     cleaned = re.sub(r"[^a-z0-9]+", "-", lower)
#     cleaned = re.sub(r"-{2,}", "-", cleaned)
#     return cleaned.strip("-")
#
# def truncate_safe(value: str, max_len: int) -> str:
#     if value is None:
#         return ""
#     if len(value) <= max_len:
#         return value
#     if max_len <= 3:
#         return "." * max_len
#     return value[:max_len-3] + "..."
#
# title = "  Hello, World! Python helper functions in action  "
# print(to_slug(title))          # "hello-world-python-helper-functions-in-action"
# print(truncate_safe(title, 18))# "  Hello, World!..."


# খ) কাস্টম র‍্যাপার ক্লাস (API স্টাইল)
import re

class S:
    def __init__(self, s: str):
        self.s = s or ""

    def to_slug(self) -> "S":
        lower = self.s.strip().lower()
        cleaned = re.sub(r"[^a-z0-9]+", "-", lower)
        cleaned = re.sub(r"-{2,}", "-", cleaned)
        return S(cleaned.strip("-"))

    def truncate_safe(self, max_len: int) -> "S":
        s = self.s
        if len(s) <= max_len:
            return S(s)
        if max_len <= 3:
            return S("." * max_len)
        return S(s[:max_len-3] + "...")

    def __str__(self):
        return self.s

title = S("  Hello, World! Python class style  ")
print(title.to_slug())          # __str__() কল হয়ে প্রিন্ট হয়
print(title.truncate_safe(18))