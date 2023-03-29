a = {'b': {'q':'we'}}
print('z' in a)
for k, v in a.items():
    if v['q'] == 'we':
        print("yey")
        break
else:
    print("nahhh")
