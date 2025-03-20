# # 2.3.1 使用方法修改字符串的大小写
# name = "ada lovelace"
# print(name.title())
# name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())
# #2.3.2 在字符串中使用变量
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# message = f"hello,I am  {full_name.title()}"
# print(message)
# #2.3.3 使用制表符或换行符来添加空白
# print("python")
# print("\tpython")
# # print("Language:\nPythgon\nC\nJavascript")
# # 2.4.4 数中的下划线
# universe_age = 14_000_000_000
# print(universe_age)
# # 2.4.5 同时给多个变量赋值
# x,y,z = 0,1,2
# print(x,y,z)
# #3.1 列表
# bicycles = ['A','B','C']
# print(bicycles)
# bicycles = ['A','B','C']
# print(bicycles[0])
# bicycles = ['A','B','C']
# print(bicycles[-1])
# #3.1.3使用列表中的各个值
# bicycles = ['trek','cannondale','redline','specialized']
# message = f"My first bicycle was a {bicycles[0].title()}"
# # print(message)
# # 3.2.2 在列表中添加元素
# motocycles = ['honda','yamaha','suzuki']
# print(motocycles)
# # motocycles.append('ducati')
# # print(motocycles)
# # 在列表中插入元素
# motocycles = ['honda','yamaha','suzuki']
# motocycles.insert(0,'suzuki')
# # print(motocycles)
# # # 从列表中删除元素
# # motocycles = ['honda','yamaha','suzuki']
# # # del motocycles[0]
# # # print(motocycles)
# # motocycles = ['honda','yamaha','suzuki']
# #
# # # first_owned = motocycles.pop(0)
# # # print(f"the first motocycles i owned was a {first_owned.title()}")
# # for x in range(1,5):
# #     print(f"其中的值为,{x}")
# magicians = ['alice','david','carolina']
# for a in magicians:
#     print(f"{a.title()},that was a great trick!")
#     print(f"I can't wait to see your next trick, {a.title()}.\n")