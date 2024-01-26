# Crachá Virtual - Seletiva LEDES (Equipe 6)
Como parte do processo seletivo para participação do Laboratório de Engenharia e Desenvolvimento de Software (LEDES), foi-se proposto um projeto que deveria ser desenvolvido durante entre 22 de janeiro e 26 de janeiro, em grupos com 6 integrantes, formados pela equipe do próprio laboratório e composta por outros estudantes visando em fazer parte do LEDES.

O desafio proposto foi o desenvolvimento de um crachá virtual com as seguintes características:
1. O crachá poderá ser acessado em navegadores em dispositivos móveis, desktop e outros similares;
2. A interface deve ser adptável, fluída;
3. Deve haver serviço de autenticação;
4. O usuário pode atualizar suas informações, porém as mudanças devem passar por aprovação de um administrador.


## Documentos
Com o principal intuito de registrar o decorrer do desenvolvimento e como forma de manter a organização, criamos um documento de requisitos para o desenvolvimento, um mockup do design das telas e um quadro no trello com as tarefas a serem realizadas. Segue o link para os documentos:

- [Figma](https://www.figma.com/file/Hyn2tKWl1JuWCZFbvYM85K/Design-Seletiva-LEDES?type=design&mode=design)
- [Trello](https://trello.com/b/arx6hunl/seletiva-ledes)
- [Documento de requisitos](https://docs.google.com/document/d/1-h-CMDqq4-RB2DNmR4LUarToD2kkioz9OwV0J1W-0kg/edit?usp=sharing)


## Tecnologias e Ferramentas
As tecnologias que optamos por utilizar foram:

- Django;
- HTML/CSS;
- SQLite.


## Exemplos
![Tela de login](photos/login-screen.png?raw=true "Tela de login")
![Crachá](photos/cracha.png?raw=true "Crachá")
![Editar usuário](photos/editar-usuario.png?raw=true "Tela para usuário alterar suas informações")
![Tela do admin](photos/admin.png?raw=true "Tela para o administrador aprovar/rejeitar alterações de informações")

## Instalação e como utilizar

### Iniciando o projeto
Para começar clone o repositório para sua máquina.
```
git clone https://github.com/FernandoAyach/seletiva-ledes.git
```

Entre no diretório do projeto e rode o comando `python -m venv ./venv` para começar o ambiente virtual e execute o comando `pip install -r requirements.txt` para instalar todas as dependências do projeto.

Para executar o projeto, rode os comandos `python manage.py migrate` para que as migrações iniciais do banco de dados sejam realizadas e o comando `python manage.py runserver` para executar a aplicação. Por padrão, o site será exibido em `http://127.0.0.1:8000` ou `http://localhost:8000`.


### Autenticação e acessos
Para acessar o sistema, deixamos um banco de dados SQLite básico com dois usuários para teste:
```
// Administrador
e-mail: admin@gmail.com
senha:  admin

// Usuário normal
e-mail: usuario@gmail.com
senha:  usuario
```

Para a criação de mais usuários, acesse o caminho `admin/` e acesse a conta de administrador.


## Colaboradores
- Alex Yasohati Hoshino;
- [Fernando Ribeiro Ayach;](https://github.com/FernandoAyach)
- [Marcelo Soares Antunes;](https://github.com/Mar-1)
- [Shynji Robbie Miyasato.](https://github.com/mshynji)
