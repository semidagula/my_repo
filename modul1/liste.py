data_type = "dictionary "
if data_type == "lista":

            #LISTE
            lista_1 = [1, 2, 3, 4, 5, 6]
            lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]
            lista_3 = [1, True, "_", False, 5.2]
            print(lista_1[0], lista_1[len(lista_1) - 1])
            x = lista_1.reverse()
            print(lista_1)
            print(x)
            lista_1.sort()
            print(lista_1)
            lista_2.sort()
            print(lista_2)
            lista_matrice = [lista_1, lista_2, lista_3]
            print(lista_matrice)
            lista_mare = [lista_matrice, [0, 1, lista_1, ["a", "b", "c"], [lista_matrice]], {}, True]

         #ok
            """todo sortatii lista 2 dupa penultimul element (ultima litera din fiecare string)
            expected result = [mac, ipad, apple, iphone]""" 

            lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]
            def sort_function(item):
                return len(item)
            lista_2.sort(key=sort_function)
            print(lista_2)
            
            
           

            """count cate elemente sunt intro lista, mai mult decat o data, app_le ( elimiinam spatiile), litera mare, mica, carcater special.....sa fei vazut ca apple
            lista. (metode de liste)
            #extragem din lista mare "_",  ultimul 6, 2 din mijloc (putem folosi if si count)
            
            """

            lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]
            count = len([lista_2.count(item) for item in lista_2])
            print(count)

            print(lista_mare[0][0][0:-1])




            x = ["a", "b", "c", "d"]
            o = x
            y = x.copy()
            u = x[:]
            y[0] = "E"
            p = list(x)
            print(x, y, u)
            print(id(x), id(y), id(u), id(o))# vezi in memorie unde este locat  stringul






elif data_type == "set":

            #SET
            # de testat celelalte metode
            print("SETURI")
            my_set = {2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7}
            print(my_set)
            my_list = [1, 1, 1, 1,]
            print(list(set(my_list)))
            second_set = {1, 2, 3, 5, 20, 7}
            print(my_set.difference(second_set), my_set.intersection(second_set))
elif data_type == "tuple":
            print("TUPLURI")
            # to do tot ce am facut la liste sa facem si aici
            tupla = (1, 2, 5, 7)
            #print (tuple[0], tuple[-1])
            #tuple[0] = 7
            print(type(tuple))
            a = (1, )
            print(type(a))
            print(a[:])

elif data_type == "dictionary ":
    print("dictionar")
    #toto display john and his email only if isActive is true
    dictionar = {
            "user1": "admin",
            "user2": "Petre",
            "user3": {
                        "name": "John",
                        "email": "john@john.com",
                        "isActive": True


            }

    }
    print(dictionar["user2"], dictionar["user3"]["email"])

