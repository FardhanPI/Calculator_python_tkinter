def sample(name, age=20):
    print("name : " + name + "\nage  : " + str(age))


sample("fardhan", 15)

# no need order= direct assignment possible
sample(age=12, name="Nooha")

# default argument given to age- so here not passed argument
sample("Nihal")
