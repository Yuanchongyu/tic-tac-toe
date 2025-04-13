# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

# s1 = Student("Alice", "A")
# s2 = Student("Bob", 16, "B")



# 定义一个 Dog 类
# class Dog:
#     # 初始化方法，创建狗时会自动调用
#     def __init__(self, name, age):
#         self.name = name    # 狗的名字
#         self.age = age      # 狗的年龄

#     # 狗狗的叫声方法
#     def bark(self):
#         print(f"{self.name}：汪汪！")


# # 创建两只狗对象
# dog1 = Dog("Lucky", 3)
# dog2 = Dog("Coco", 5)

# # 打印狗狗的名字和年龄
# print(f"{dog1.name} - {dog1.age}岁")
# print(f"{dog2.name} - {dog2.age}岁")

# # 让它们各叫一声
# dog1.bark()
# dog2.bark()



class ShoppingCart:
    def __init__(self):
        self.items = {}  # 用字典保存商品和数量
        # {
        # "apple": 2,
        # "banana": 3,
        # "orange": 5
        # "pinapple": 1
        # }
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"{item_name} 不在购物车中。")

    def update_quantity(self, item_name, new_quantity):
        if new_quantity <= 0:
            self.remove_item(item_name)
        else:
            self.items[item_name] = new_quantity

    def view_cart(self):
        if not self.items:
            print("购物车是空的。")
        else:
            print("🛒 当前购物车内容：")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")

shopping_cart_1 = ShoppingCart()
print(shopping_cart_1.items)
shopping_cart_1.add_item("苹果", 5)
print(shopping_cart_1.items)
shopping_cart_1.add_item("香蕉", 3)
print(shopping_cart_1.items)
shopping_cart_1.remove_item("香蕉")
print(shopping_cart_1.items)


# import os
# import random
# import time
# import msvcrt  # Windows only

# WIDTH, HEIGHT = 20, 20

# class Snake:
#     def __init__(self):
#         self.body = [(5, 5)]
#         self.direction = (0, 1)  # 初始向下 (dx, dy)

#     def move(self):
#         head_x, head_y = self.body[0]
#         dx, dy = self.direction
#         new_head = (head_x + dx, head_y + dy)
#         self.body.insert(0, new_head)
#         self.body.pop()  # 默认每次不增长

#     def grow(self):
#         tail = self.body[-1]
#         self.body.append(tail)  # 尾部再复制一份，达到“增长”效果

#     def change_direction(self, key):
#         if key == b'w' and self.direction != (0, 1): self.direction = (0, -1)
#         if key == b's' and self.direction != (0, -1): self.direction = (0, 1)
#         if key == b'a' and self.direction != (1, 0): self.direction = (-1, 0)
#         if key == b'd' and self.direction != (-1, 0): self.direction = (1, 0)

#     def check_collision(self):
#         head = self.body[0]
#         if head in self.body[1:]: return True  # 咬到自己
#         if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT): return True  # 撞墙
#         return False

# class Game:
#     def __init__(self):
#         self.snake = Snake()
#         self.food = self.spawn_food()

#     def spawn_food(self):
#         while True:
#             food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
#             if food not in self.snake.body:
#                 return food

#     def draw(self):
#         os.system('cls')  # 清屏
#         for y in range(HEIGHT):
#             row = ""
#             for x in range(WIDTH):
#                 pos = (x, y)
#                 if pos == self.snake.body[0]:
#                     row += "@"
#                 elif pos in self.snake.body:
#                     row += "o"
#                 elif pos == self.food:
#                     row += "*"
#                 else:
#                     row += "."
#             print(row)

#     def run(self):
#         while True:
#             time.sleep(0.1)
#             if msvcrt.kbhit():
#                 key = msvcrt.getch()
#                 if key == b'q':
#                     print("退出游戏。")
#                     break
#                 self.snake.change_direction(key)

#             self.snake.move()

#             # 检查是否吃到食物
#             if self.snake.body[0] == self.food:
#                 self.snake.grow()
#                 self.food = self.spawn_food()

#             self.draw()

#             if self.snake.check_collision():
#                 print("💥 Game Over!")
#                 break

# if __name__ == "__main__":
#     Game().run()








# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#     # 添加商品
#     def add_item(self):
#         pass
#     def remove_item(self):
#         pass
#     def view_cart(self):
#         pass