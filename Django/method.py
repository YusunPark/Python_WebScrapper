class Bread():

    def __init__(self, **kwargs):
        self.price = 1000
        self.color = "Yellow"
        self.size = "Midium"
        self.time = "10/23"
        self.type = kwargs.get("type", "normal")


    def __str__(self):
        return f"Bread's color is {self.color}."

donut = Bread(size="big")
print(donut.type, donut.size)

