# pessoas = {
#     'nome':'ana',
#     'idade':'25',
#     'cidade':'são paulo'
# }

# print(pessoas['nome'])
# print(pessoas['idade'])
# print(pessoas['cidade'])

# contato = {
#     'telefone':'123456789',
#     'email':'contato@exemplo.com',
# }
# contato['telefone'] = '987654321'

# print (contato)

# aluno = {
#     'nome':'joão',
#     'nota':'7.5',
# }
# aluno['curso']='masculino'
# print(aluno)

# produto ={
#     'nome':'laptop',
#     'preço':'3500',
#     'quantidade':'10'
# }
# del produto['quantidade']

# print(produto)

# biblioteca = {
#     '1984':{'autor':'george orwell','ano':'1949'},
#     'o senhor dos aneis':{'autor':'j.r.r tolkien','ano':'1954'},
#     'o hobbit':{'autor':'j.r.r tolkien','ano':'1937'}   
# }
# biblioteca['harry potter']= {'autor':'j.k rowling','ano':'1998'}
# biblioteca['o hobbit']={'ano':'1955'}
# print(biblioteca)

# estudantes = {
#     'ana':['matematica','historia'],
#     'pedro':['biologia','fisica'],
#     'maria':['quimica','biologia'],
# }
# del estudantes['maria'][0]
# estudantes['ana'] += ['biologia']

# print(estudantes)

compras_clientes = {
    'ana':['leite','pao','maca'],
    'pedro':['biologia','fisica'],
    'maria':['quimica','matematica']
}
for chave,valor in compras_clientes: