numbers={
    'n2': ('a', 'b', 'c'),
    'n3': ('d', 'e', 'f'),
    'n4': ('g', 'h', 'i'),
    'n5': ('j', 'k', 'l'),
    'n6': ('m', 'n', 'o'),
    'n7': ('p', 'q', 'r', 's'),
    'n8': ('t', 'u', 'v'),
    'n9': ('w', 'x', 'y', 'z')
}

keywords=[]
no_of_keyword = int(input("No of keywords : "))
for a in range(no_of_keyword):
    keyword = input("Keyword : ")
    keywords.append(keyword)

print(keywords)

matches=[]
for keyword in keywords:
    n=len(keyword)
    for i in range(n):
        for a in range(8):
            for j in numbers['n'+str(a+2)]:
                if keyword[i] == j:
                    matches.append(a+2)

print(matches)

