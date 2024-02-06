def message(what, number):
    print("Entrar", what, "número", number)

message("telefone", 11)
message("preço", 5)
message("número", "número")

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
introduction(first_name = "Jeon", last_name = "Jungkook")
introduction(last_name = "Namjoon", first_name = "Kim")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(4, c = 6, b = 5)

def apresentar(prim_nome, seg_nome = "Smith"):
    print("Olá meu nome é", prim_nome, seg_nome)

apresentar("James", "Doe")
apresentar("Henry")
apresentar(prim_nome = "William")