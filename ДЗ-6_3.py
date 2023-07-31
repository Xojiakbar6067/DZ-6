class Car:
    def __init__(self, color, type, year):
        self.color=color
        self.type=type
        self.year=year
    def start(self):
        print('Автомобиль заведен')
    def stop(self):
        print('Автомобиль заглушен')
    def change_year(self, new_year):
        self.year=new_year
    def change_type(self, new_type):
        self.type=new_type
    def change_color(self, new_color):
        self.color=new_color
cobalt=Car(color='white', type='sedan', year=2022)
while True:
    print('---------------------------------', '\n''1-запуск автомобиля', '\n''2-отключение автомобиля',
          '\n''3-присвоение автомобилю год випуска', '\n''4-присвоение автомобилю типа',
          '\n''5-присвоение автомобилю света','\n''6-показат информацию об автомобиле')
    operator=int(input('выбирайте: '))
    if operator==1:
        cobalt.start()
    elif operator==2:
        cobalt.stop()
    elif operator==3:
        cobalt.change_year(int(input('какой год? ')))
    elif operator==4:
        cobalt.change_type(input('какой тип? '))
    elif operator==5:
        cobalt.change_color(input('какой свет? '))
    elif operator==6:
        print(cobalt.__dict__)
    else:
        print('выберайте правилный действие ')