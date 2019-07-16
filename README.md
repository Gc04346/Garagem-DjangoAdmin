# Projeto Garagem - Django Admin
### Sobre o projeto
Pequeno projeto realizado com Django 2.0.4 para customização do Django Admin. 
Foi feita uma simulação de garagem com o banco de dados sqlite3, padrão do Django. Cada carro possui um chassi (primary key), marca, modelo, cor, ano, estado, e mais.

### Alterações feitas no Django Admin
Na página Carros, é possível criar, deletar ou alterar carros no banco de dados. O Django Admin já providencia todo o CRUD necessário para tal.
Porém, adicionei a possibilidade de buscar por modelo de carro ou chassi, e de filtragem por alguns parâmetros.

### Geração de relatório
Ao selecionar alguns carros e clicar na aba de ações, é possível gerar um PDF com todas as informações de cada carro que foi selecionado. O browser
providencia uma caixa de download, para que o PDF possa ser baixado sem problemas.

### Pacotes externos
É necessário a instalação do weasyprint e do django-object-actions, para que o projeto funcione corretamente:
```shell
$ pipenv install weasyprint

$ pipenv install django-object-actions
```
