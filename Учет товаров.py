# Класс Product:
# Имеет атрибуты name, weight, category.
# Метод __str__ возвращает строку с информацией о продукте в нужном формате.
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
# Класс Shop:
# Имеет инкапсулированный атрибут __file_name, который указывает на файл для хранения продуктов.
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
# Метод get_products считывает содержимое файла и возвращает его как строку.
# Если файл не найден, возвращает пустую строку.
    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""
# Метод add принимает неограниченное количество объектов класса Product.
# Он проверяет, существует ли продукт с таким же названием в файле.
# Если продукт уже есть, выводит сообщение.
# Если нет — добавляет продукт в файл.
    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {p.split(", ")[0] for p in existing_products if p}

        for product in products:
            if product.name in existing_names:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')

# Пример работы программы
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
# При каждом добавлении нового продукта, информация записывается в файл с переходом
# на новую строку.
