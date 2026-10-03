# OpsTrack API

API desenvolvida em Python utilizando Flask para gerenciamento de chamados.

## Equipe

* Adriel Rattes
* Fernando Dias
* Giuliano
* Milton Wagner
* Paulo Ricardo
* Riquelme

## Repositório no GitHub

https://github.com/miltonwagner/opstrack-api

---

## Sobre o projeto

A OpsTrack API é uma API simples desenvolvida como exercício da disciplina de **Integração e Entrega Contínua**.

O projeto tem como objetivo praticar:

* Desenvolvimento de uma API utilizando Flask;
* Criação de rotas HTTP;
* Uso do Git para controle de versão;
* Utilização do GitHub;
* Organização dos commits utilizando o padrão Conventional Commits;
* Separação das alterações em commits independentes;
* Utilização de Linter para análise do código;
* Automação da verificação de código utilizando pre-commit e Flake8.

---

## Tecnologias utilizadas

* Python
* Flask
* Flake8
* pre-commit
* Git
* GitHub
* Visual Studio Code

---

## Estrutura do projeto

```text
opstrack-api/
├── hello.py
├── utils.py
├── README.md
├── .gitignore
├── .flake8
└── .pre-commit-config.yaml
```

---

# API

A API possui quatro rotas principais:

| Método | Rota       | Descrição                       |
| ------ | ---------- | ------------------------------- |
| GET    | `/`        | Retorna uma mensagem inicial    |
| GET    | `/status`  | Retorna o status do serviço     |
| GET    | `/tickets` | Retorna uma lista de chamados   |
| GET    | `/sobre`   | Retorna informações sobre a API |

---

## Rota inicial

### GET /

Retorna uma mensagem inicial da API.

Resposta:

```text
Hello World 1
```

---

## Rota de status

### GET /status

Retorna o status atual do serviço.

Resposta:

```json
{
    "status": "online"
}
```

---

## Rota de chamados

### GET /tickets

Retorna uma lista mockada de chamados.

Resposta:

```json
[
    {
        "id": 1,
        "titulo": "Computador não liga",
        "status": "aberto"
    },
    {
        "id": 2,
        "titulo": "Erro no sistema",
        "status": "em andamento"
    },
    {
        "id": 3,
        "titulo": "Solicitação de acesso",
        "status": "fechado"
    }
]
```

---

## Rota sobre

### GET /sobre

Retorna informações básicas sobre a API.

Resposta:

```json
{
    "nome": "OpsTrack API",
    "versao": "1.0.0"
}
```

---

# Instalação

Para utilizar o projeto, é necessário ter o **Python** e o **Git** instalados.

## 1. Clonar o repositório

```powershell
git clone https://github.com/miltonwagner/opstrack-api.git
```

Entrar na pasta do projeto:

```powershell
cd opstrack-api
```

---

## 2. Criar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv venv
```

Ativar o ambiente virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Instalar o Flask

```powershell
python -m pip install flask
```

---

# Linter — Flake8

O projeto utiliza o **Flake8** como ferramenta de Linter.

O Linter é utilizado para analisar automaticamente o código-fonte, identificando problemas relacionados à qualidade, formatação e padrões de escrita do código.

O **Flake8** realiza essa análise nos arquivos Python do projeto.

A configuração do Flake8 está armazenada no arquivo:

```text
.flake8
```

Essa configuração é versionada junto com o projeto para que os integrantes da equipe utilizem as mesmas regras.

---

## Executar o Flake8 manualmente

Para executar o Flake8 no projeto:

```powershell
flake8
```

O Flake8 analisará os arquivos Python e informará os problemas encontrados.

---

# Pre-commit

O projeto utiliza o **pre-commit** para executar automaticamente o Linter antes de cada commit.

O objetivo é evitar que código com problemas identificados pelo Flake8 seja registrado no repositório.

A configuração do pre-commit está armazenada no arquivo:

```text
.pre-commit-config.yaml
```

O arquivo faz parte do repositório oficial da equipe e é compartilhado pelo Git.

---

## Configuração do pre-commit

Atualmente, o projeto utiliza o Flake8 como hook do pre-commit:

```yaml
repos:
  - repo: https://github.com/PyCQA/flake8
    rev: 7.3.0
    hooks:
      - id: flake8
```

Dessa forma, o Flake8 é executado automaticamente antes de um commit.

---

# Funcionamento do hook

O fluxo de execução é:

```text
Desenvolvedor altera o código
            ↓
         git add
            ↓
        git commit
            ↓
        pre-commit
            ↓
          Flake8
            ↓
      ┌─────┴─────┐
      ↓           ↓
 Sem erros     Com erros
      ↓           ↓
 Commit        Commit
 permitido     bloqueado
```

Quando o Flake8 não encontra problemas, o commit pode continuar.

Quando o Flake8 encontra problemas, o pre-commit interrompe o processo e o commit não é concluído.

O desenvolvedor deve corrigir os problemas identificados e tentar realizar o commit novamente.

---

# Configuração para novos integrantes da equipe

O arquivo `.pre-commit-config.yaml` já está versionado no repositório oficial da equipe.

Por isso, um novo integrante **não precisa criar esse arquivo manualmente**.

Cada integrante deve instalar o pre-commit na própria máquina e instalar o hook no seu clone local do projeto.

## 1. Clonar o projeto

```powershell
git clone https://github.com/miltonwagner/opstrack-api.git
```

Entrar na pasta:

```powershell
cd opstrack-api
```

---

## 2. Criar o ambiente virtual

```powershell
python -m venv venv
```

Ativar:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Instalar o Flask

```powershell
python -m pip install flask
```

---

## 4. Instalar o pre-commit

```powershell
python -m pip install pre-commit
```

Verificar a instalação:

```powershell
pre-commit --version
```

O comando deve apresentar a versão instalada do pre-commit.

---

## 5. Instalar o hook

Dentro da pasta do projeto:

```powershell
pre-commit install
```

O comando deverá apresentar uma mensagem semelhante a:

```text
pre-commit installed at .git\hooks\pre-commit
```

---

## 6. Testar o hook

Para executar a verificação em todos os arquivos do projeto:

```powershell
pre-commit run --all-files
```

Quando não houver problemas de lint, o resultado deverá apresentar:

```text
flake8...................................................................Passed
```

Depois dessa configuração, o pre-commit será executado automaticamente antes dos commits realizados nessa máquina.

---

# Teste do pre-commit com erro de lint

Para verificar o funcionamento do hook, pode ser realizado um teste com um erro de lint proposital.

Por exemplo, no arquivo Python, pode ser inserida uma linha com formatação inadequada:

```python
x=1
```

Depois da alteração, adicionar o arquivo:

```powershell
git add .
```

Tentar realizar um commit:

```powershell
git commit -m "test: verifica hook do pre-commit"
```

O pre-commit será executado automaticamente.

O Flake8 deverá identificar o problema e o processo de commit será interrompido.

Um resultado de falha poderá apresentar uma indicação semelhante a:

```text
flake8.................................................................Failed
```

Nesse caso, o problema deverá ser corrigido antes que o commit seja concluído.

Depois da correção:

```powershell
git add .
```

E executar novamente:

```powershell
git commit -m "test: verifica hook do pre-commit"
```

Com o código corrigido, o Flake8 deverá passar e o commit poderá ser concluído.

---

# Execução manual do pre-commit

Também é possível executar os hooks manualmente sem realizar um commit.

Para verificar todos os arquivos:

```powershell
pre-commit run --all-files
```

Esse comando é útil para verificar o estado do código antes de realizar um commit.

---

# Comandos úteis

### Verificar versão do pre-commit

```powershell
pre-commit --version
```

### Instalar o hook

```powershell
pre-commit install
```

### Executar o pre-commit em todos os arquivos

```powershell
pre-commit run --all-files
```

### Executar o Flake8 diretamente

```powershell
flake8
```

### Verificar o estado do Git

```powershell
git status
```

### Atualizar o projeto

```powershell
git pull origin main
```

---

# Controle de versão

O projeto utiliza **Git** para controle de versão e **GitHub** para armazenamento remoto do código.

Repositório:

https://github.com/miltonwagner/opstrack-api

---

# Conventional Commits

Os commits do projeto seguem o padrão **Conventional Commits**.

Cada commit deve representar uma única mudança lógica.

Exemplos de commits utilizados no projeto:

```text
feat: adiciona rota de status
```

```text
feat: adiciona rota de tickets
```

```text
feat: adiciona rota sobre
```

```text
docs: atualiza documentacao das rotas
```

```text
chore: adiciona pre-commit flake8
```

```text
feat: adiciona funcao saudacao
```

---

## Tipos de commit

| Tipo       | Utilização                                                      |
| ---------- | --------------------------------------------------------------- |
| `feat`     | Nova funcionalidade                                             |
| `fix`      | Correção de problema                                            |
| `docs`     | Alteração na documentação                                       |
| `style`    | Alteração de formatação                                         |
| `refactor` | Alteração na estrutura do código sem modificar a funcionalidade |
| `chore`    | Alteração de configuração ou manutenção                         |
| `test`     | Criação ou alteração de testes                                  |

---

# Regra de commits

Cada commit deve representar uma única mudança lógica.

Não devem ser misturadas diferentes alterações no mesmo commit.

### Exemplo

```text
feat: adiciona rota de status
```

Esse commit representa somente a criação da rota `/status`.

Outro exemplo:

```text
feat: adiciona rota de tickets
```

Esse commit representa somente a criação da rota `/tickets`.

A documentação deve ser atualizada separadamente:

```text
docs: atualiza documentacao das rotas
```

---

# .gitignore

O arquivo `.gitignore` evita que arquivos desnecessários sejam enviados para o GitHub.

Arquivos e diretórios ignorados incluem:

```text
venv/
__pycache__/
*.pyc
```

---

# Arquivos de configuração do Linter

O projeto possui dois arquivos importantes relacionados à qualidade do código:

### `.flake8`

Contém as configurações utilizadas pelo Flake8.

### `.pre-commit-config.yaml`

Define os hooks executados automaticamente pelo pre-commit.

Esses arquivos são versionados no repositório para que toda a equipe tenha acesso à mesma configuração.

O hook instalado em `.git/hooks/pre-commit` é criado localmente em cada máquina pelo comando:

```powershell
pre-commit install
```

Esse arquivo local não precisa ser enviado ao GitHub.

---

# Status do projeto

Projeto desenvolvido para fins acadêmicos na disciplina de **Integração e Entrega Contínua**.

**Status:** Em desenvolvimento.
