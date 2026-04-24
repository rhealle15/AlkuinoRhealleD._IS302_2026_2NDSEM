class Car_rda:
    def __init__(self_rda, brand_rda, model_rda, year_rda):
        self_rda.brand_rda = brand_rda
        self_rda.model_rda = model_rda
        self_rda.year_rda = year_rda
    
    def display_car_rda(self_rda):
        print(self_rda.brand_rda, self_rda.model_rda, self_rda.year_rda)

car1_rda = Car_rda("Toyota", "Corolla", 2020)
car1_rda.display_car_rda()
