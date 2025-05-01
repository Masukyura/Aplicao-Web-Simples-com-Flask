Protótipo Funcional de uma Aplicação Web Simples com Flask

# Descrição do Projeto
O ShoPI é um sistema de gerenciamento para pequenos comércios, desenvolvido em Flask (Python), que permite o cadastro e gerenciamento de clientes e produtos. O sistema oferece uma interface web intuitiva para realizar operações CRUD (Create, Read, Update, Delete) sobre esses dados.

# Funcionalidades Implementadas
Módulo de Clientes
Cadastro de clientes: Inclusão de novos clientes com nome, e-mail, data de nascimento, cidade e telefone

Listagem de clientes: Visualização de todos os clientes cadastrados em formato de tabela

Edição de clientes: Atualização dos dados dos clientes existentes

Exclusão de clientes: Remoção de clientes do sistema

Validação de dados: Verificação dos campos antes do cadastro/atualização

# Módulo de Produtos
Cadastro de produtos: Inclusão de novos produtos com nome, preço, estoque, quantidade, marca e categoria

Listagem de produtos: Visualização de todos os produtos cadastrados em formato de tabela

Edição de produtos: Atualização dos dados dos produtos existentes

Exclusão de produtos: Remoção de produtos do sistema

Validação de dados: Verificação dos campos antes do cadastro/atualização

# Tecnologias Utilizadas
Backend: Python com Flask

Frontend: HTML5, CSS3

# Passos para Execução
Clone o repositório (se aplicável) ou copie os arquivos do projeto para uma pasta local

# Crie um ambiente virtual (recomendado):

python -m venv venv

# Ative o ambiente virtual:

# No Windows:

venv\Scripts\activate

# No Linux/MacOS:

source venv/bin/activate

# Instale as dependências:

pip install flask flask-sqlalchemy

# Execute a aplicação:

python run.py

# Acesse a aplicação:
Abra seu navegador e acesse:

http://localhost:5000

# Primeiros Passos
Ao acessar a aplicação, você verá a página inicial com opções para:

Cadastrar novo produto

Cadastrar novo cliente

Visualizar produtos cadastrados

Visualizar clientes cadastrados

Utilize os menus de navegação para acessar as diferentes funcionalidades do sistema
