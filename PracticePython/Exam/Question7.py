# একটি Car ক্লাস তৈরি করুন যেখানে id, brand এবং model নামে তিনটি প্রোপার্টি থাকেব। মেইন মেথড থেকে গাড়ির তথ্য প্রিন্ট করবে

class Car:
    # Constructor
    def __init__(self, car_id, brand, model):
        self.id = car_id
        self.brand = brand
        self.model = model

    # Method to display car info
    def display_info(self):
        print(f"Car ID: {self.id}, Brand: {self.brand}, Model: {self.model}")


# Main part
car1 = Car(1, "Toyota", "Corolla")

# গাড়ির তথ্য প্রিন্ট করা
car1.display_info()
