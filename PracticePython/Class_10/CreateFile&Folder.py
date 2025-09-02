# Create Folder, File, Write data into file, Read data, Delete File and Folder
import os                   # অপারেটিং সিস্টেম সম্পর্কিত কাজ (ফাইল/ফোল্ডার তৈরি, মুছে ফেলা ইত্যাদি)।
import shutil               # advanced file operations (একসাথে পুরো ফোল্ডার মুছে ফেলা, কপি ইত্যাদি)।

try:
    # 1. ফোল্ডার তৈরি
    # folder_path = "/home/mehedi/Documents/MyFolder"  যদি ফোল্ডারের লোকেশন ইচ্ছামতো সেট করতে চাই Mac/Linux এর জন্য
    # folder_path = r"C:\Users\Mehedi\Documents\MyFolder" যদি ফোল্ডারের লোকেশন ইচ্ছামতো সেট করতে চাই Windows
    folder_path = r"C:\DemoFolder"
    if not os.path.exists(folder_path):         # os.path.exists(path) → চেক করে ওই ফোল্ডার/ফাইল আগে থেকে আছে কিনা। not মানে না থাকলে।
        os.makedirs(folder_path)                # os.makedirs(path) → নতুন ফোল্ডার তৈরি করে।
        print("Folder created successfully.")

    # 2. ফাইল তৈরি ও ডাটা লেখা
    file_path = os.path.join(folder_path, "example.txt")    # os.path.join(a, b) → ফোল্ডার আর ফাইল নাম মিলিয়ে সম্পূর্ণ path বানায়।
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("Hello, this is the first line in the file.\n")
        print("File created and text written.")

    # 3. ফাইলে ডাটা অ্যাপেন্ড করা
    with open(file_path, "a") as f:
        f.write("This is another line.\n")
    print("Text appended to file.")

    # 4. ফাইল থেকে ডাটা পড়া
    with open(file_path, "r") as f:
        content = f.read()
    print("File Content:")
    print(content)

    # 5. ফাইল ডিলিট করা (কমেন্ট করলে থাকবে)
    os.remove(file_path)
    print("File deleted.")

    # 6. ফোল্ডার ডিলিট করা (ফোল্ডার সহ সব ফাইল ডিলিট হবে)
    shutil.rmtree(folder_path)
    print("Folder deleted.")

except Exception as e:
    print("Error:", e)