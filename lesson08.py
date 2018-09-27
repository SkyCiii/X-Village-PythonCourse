
import re

text = 'Today is a good day to learn regular expression'    # Given a sentence or an aritcle...
pattern = r'regular expression'                             # Define regular expreesion as string 'regular expression'
match = re.search (pattern, text)                           # 在 text 裡面搜出 regular expression
print(match)                                                # 如果有 match 到，則 match 有 type（一樣在 re module 底下）
start_index = match.span()[0]                               # 如果沒有 match 到，則 match 為 NoneType
end_index = match.span()[1]
match_string = match.group()
print ("The location of '{}'is between'{}'and'{}'".format(match_string, start_index, end_index))

#

text1 = 'Cake and cookie'
text2 = 'cookie and Cake'

pattern = r'cookie'

match1 = re.match(pattern, text1)                   # re.match 和 MatchType 的 object 別搞混了
match2 = re.match(pattern, text2)                   # re.match 是 re module 裡面的 fuction，只搜整句話的第一個字
                                                    # 如果成功，回傳 ＭatchType 的物件；若沒有，回傳 NoneType 的物件。
print ("Type of 'match1' object :", type(match1))
print (match1)
print ("=" * 50)
print ("Type of 'match2' object :", type(match2))
print("Matching pattern : %r" %match2.group())

#

text = 'cookie and Cake'

pattern = r'cookie'

new_text = re.sub(pattern, 'biscuit', text)         # replace = biscuit
                                                    # 在 text 內 搜尋符合 pattern 的字串，replace 成 'biscuit'。
print ('Original text :', text)
print ('After substitution :', new_text)

#

text = 'cookie and Cake'

pattern = r'cookie'

def repl(match) :                                   # TypeError: repl() takes 0 positional arguments but 1 was given
    new_string = match.group()+'-'+match.group()
    return new_string
new_text = re.sub(pattern, repl, text)
print (text)
print (new_text)

#

text = 'cookie and Cake'

pattern = r'(?P<fat>cookie) and (?P<fatter>Cake)'

match = re.search(pattern, text)
d = match.groupdict()
print (d)
print (match.group())
print (match.group(1))
print (match.group(2))
print (match.group(1, 2))

#

text = 'Johnny Liu'

pattern = r'(?P<First_name>Johnny) (?P<Last_name>Liu)'

match = re.search(pattern, text)
d = match.groupdict()
print (d)
print (match.group(1, 2))

#

# import re

# text = input()

# pattern = r'(?P<First_name>\w\w\w) (?P<Last_name>\w\w\w\w)'

# match = re.search(pattern, text)
# d = match.groupdict()
# print (text, d)

#

text1 = " and cookie"
text2 = "CakeCakeCakeCake and cookie"
pattern = r'(Cake)+ and cookie'
match1 = re.search(pattern, text1)
# match2 = re.search(pattern, text2)
print (match1)
match2.group()
print (match2.group())