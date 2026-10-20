class Car:
  def __init__(self, model, year):
    self.model = model
    self.year = year  

  def drive(self):
    print(f"The {self.year} {self.model} is driving.")


car1 = Car("Toyota Camry", 2020)
car1.drive()  # Output: The 2020 Toyota Camry is driving.

car2 = Car("Honda Civic", 2021)
car2.drive()  # Output: The 2021 Honda Civic is driving.