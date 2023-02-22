# Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape.
# Перевизначте їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма методами.
# В результаті повинно з’явитися зображення. Перегляньте їх.
from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (191, 205, 255, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


class Cone(Shape):
    def draw(self):
        self.draw1.polygon([(300, 100), (200, 300), (400, 300)], fill=(255, 208, 38))
        self.draw1.ellipse((200, 275, 400, 325), fill=(255, 208, 38))

        def hell_year():
            pass

        return hell_year()



    def erase(self):
        self.draw1.polygon([(300, 100), (200, 300), (400, 300)], fill=self.back_color)
        self.draw1.ellipse((200, 275, 400, 325), fill=self.back_color)

    def save(self):
        print("Image with cone was created")
        return self.im.save('draw-cone.png', quality=95)


class Paraboloid(Shape):
    def draw(self):
        self.draw1.polygon([(250, 95), (350, 95), (400, 300), (200, 300)], fill=(255, 208, 38))
        self.draw1.ellipse((200, 275, 400, 325), fill=(255, 208, 38))
        self.draw1.ellipse((252, 50, 348, 150), fill=(255, 208, 38))


    def erase(self):
        self.draw1.polygon([(250, 95), (350, 95), (400, 300), (200, 300)], fill=self.back_color)
        self.draw1.ellipse((200, 275, 400, 325), fill=self.back_color)
        self.draw1.ellipse((252, 50, 348, 150), fill=self.back_color)

    def save(self):
        print("Image with Paraboloid was created")
        return self.im.save('draw-paraboloid.png', quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                          '\n\t5. Створити конус\n\t6. Створити параболоїд'
                          '\n\t7. Зафарбувати коло\n\t8. Зафарбувати квадрат\n\t9. Зафарбувати трикутник'
                          '\n\t10. Зафарбувати конус\n\t11. Зафарбувати параболоїд'
                          '\n\t12. Вихід з програми\nОберіть необхідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                cone = Cone()
                work_with_obj(cone)
            case 6:
                parab = Paraboloid()
                work_with_obj(parab)
            case 7:
                c = Circle()
                update_obj(c)
            case 8:
                sq = Square()
                update_obj(sq)
            case 9:
                t = Triangle()
                update_obj(t)
            case 10:
                cone = Cone()
                update_obj(cone)
            case 11:
                parab = Paraboloid()
                update_obj(parab)
            case 12:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
