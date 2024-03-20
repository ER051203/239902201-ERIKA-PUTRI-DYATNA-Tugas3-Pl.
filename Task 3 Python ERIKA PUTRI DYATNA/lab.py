print("--PROGRAM YANG MENGHITUNG DAN MENYIMPAN TB DAN BB DALAM METRIK--")

berat_kg = float(input("Berat Person1 :"))
tinggi_meter = float(input("Tinggi Person1 :"))
tinggi_meter = tinggi_meter/100     #rumus tinggi badan untuk satuan meter
BMI = berat_kg / (tinggi_meter ** 2)    #rumus bmi

    
print (f"BMI = {BMI}")  #tampilan metode BMI

class BMI:
    def __init__(self, weight, height):
        self.weight = weight  # Berat badan dalam kilogram
        self.height = height  # Tinggi badan dalam meter

    @property
    def Berat(self):
        return self.weight

    @property
    def Tinggi(self):
        return self.height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False
