books = [
    {
        "name": "C#从入门到精通",
        "price": 25.7,
        "store": "卓越"
    },
    {
        "name": "ASP.NET高级编程",
        "price": 44.5,
        "store": "卓越"
    },
    {
        "name": "Python核心编程",
        "price": 24.7,
        "store": "当当"
    },
    {
        "name": "JavaScript大全",
        "price": 45.7,
        "store": "当当"
    },
    {
        "name": "Django简明教程",
        "price": 26.7,
        "store": "新华书店"
    },
    {
        "name": "深入Python",
        "price": 55.7,
        "store": "新华书店"
    },
]
print([item["price"] for item in books])
# print(min([item["price"] for item in books]))
