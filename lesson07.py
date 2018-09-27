
import json

person = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

with open ('person.json', 'w+') as f :
    json.dump(person, f)
    f.seek(0)                           # 寫完之後指標在最後一項，要 seek 回第零項，讀才讀得到東西。
    print(f)                            # f 終究是個檔案，是把 person 的內容寫「進」檔案裡面，不是寫「成」檔案，所以 print(f) 只會出現這個檔案的說明。
    print(json.load(f))                 # 要 print(json.load(f)) 才能把 f 這個檔案的內容印出來。
    print(json.load(f)['firstName'])    # json.load(f)是把 f 這個檔案轉成 python 的 dictionary，然後 print 其中的 key。

# 以下程式碼和上面的意義相同，只是把讀寫分開。

with open ('person.json', 'w') as f :
    json.dump(person, f)
with open ('person.json', 'r') as f :
    json.load(f)
    print(f)
    print(json.load(f))
    print(json.load(f)['firstName'])
