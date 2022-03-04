import json
with open('date.json') as json_file:
    new_data = json.load(json_file)


print('Interface Status')
print('='*100)
names = ['DN', 'Description', 'Speed', 'MTU']
form = "{:<50}  {:<15}  {:<10}  {:<5}";
print(form.format(*names))
print('-'*50 + '  ' + '-'*15 + '  ' + '-'*10 + '  ' + '-'*5)

for i in new_data["imdata"]:
    print('{DN:50}{Speed:30}{MTU:6}'.format(DN = i["l1PhysIf"]["attributes"]["dn"], Speed = i["l1PhysIf"]["attributes"]["speed"], MTU = i["l1PhysIf"]["attributes"]["mtu"]))
