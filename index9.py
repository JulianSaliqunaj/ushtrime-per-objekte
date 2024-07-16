person = {
    "Emri":"julian",
    "mbiemri": "saliqunaj",
    "adresa": "prishtine",
    "mosha": 18
}

emri = person["Emri"]
print(emri)

x = person.get ("Emri")
print(x)
person["adresa"] = "Kline"
print(person)

for i in person.values():
    print(i)

    if"adresa" in person:
        print("po eshte ")
    else:
        print("jo nuk eshte ")
    