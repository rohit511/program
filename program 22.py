terms = 10
result= list(map(lambda x: 2 ** x, range(terms)))
print("the total terms are",terms)

for i in range(terms):
    print(" 2 raised to power ",result[i])



[0, 1,2,3,4,5,6,7,8] |> map(x -> fn x + 2) |> [2,3,]