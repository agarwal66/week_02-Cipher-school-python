class Phone:
    class Smartphone():#derived
        def __init__(self , brand , model_name, price,internal_memory):
            
            #Phone. __init__(self , brand , model_name, price)
            super().__init__('brand','name',model_name)
            self.brand = brand
            self.model = model_name
            self.price = max(price,0)
            self.internal_memory = internal_memory
def full_name(self):
        return f"{self.brand} {self.moel_name}"
def make_a_call(self,number):
        return f"calling{number}"        
phone = Phone('nokia','1100','1000')
Smartphone =Smartphone('one-plus','s','3000','6 GB','65Gb')
print(phone.fullname())
print(Smartphone.full_name())               












#class Phone:
def __init__(self , brand , model_name, price,internal_memory):
        self.brand = brand
        self.model = model_name
        self.price = max(price,0)
        self.internal_memory = internal_memory
def full_name(self):
        return f"{self.brand} {self.moel_name}"
def make_a_call(self,number):
        return f"calling{number}"        