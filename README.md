# OpsTrack API

A OpsTrack API é uma API em Python com Flask para acompanhamento de chamados (tickets) de suporte técnico. Ela informa se o serviço está online e lista os chamados com seu status (aberto, em andamento etc.). Projeto da disciplina de Integração e Entrega Contínua.

O projeto usa **flake8** para análise estática de código e **pre-commit** para barrar automaticamente commits com erros de lint.

---

## 1. Pré-requisitos

Antes de começar, tenha instalado na sua máquina:

- **Python 3.12** ou superior — confira com `python --version`
- **Git** — confira com `git --version`
- Acesso à internet (o pre-commit baixa o flake8 no primeiro commit)

---

## 2. Configurando o ambiente

Siga os passos **na ordem**. Os comandos são executados no terminal.

### Passo 1 — Clonar o repositório

```bash
git clone https://github.com/miltonwagner/opstrack-api.git
cd opstrack-api
```

### Passo 2 — Criar o ambiente virtual

```bash
python -m venv venv
```

> **Windows:** se aparecer "Python não foi encontrado", use `py` no lugar de `python`: `py -m venv venv`

### Passo 3 — Ativar o ambiente virtual

Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

Windows (Prompt de Comando / cmd):

```cmd
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

O prompt do terminal passa a mostrar `(venv)`. **Todos os passos seguintes precisam ser feitos com o venv ativo.**

> Se o PowerShell bloquear a ativação com um erro de "execução de scripts", rode uma vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e tente de novo.

### Passo 4 — Instalar as dependências

```bash
pip install -r requirements-dev.txt
```

Esse arquivo inclui as dependências da aplicação (`requirements.txt`) e as ferramentas de desenvolvimento (flake8 e pre-commit).

### Passo 5 — Ativar o hook do pre-commit

```bash
pre-commit install
```

Você deve ver:

```
pre-commit installed at .git/hooks/pre-commit
```

> **Atenção:** este passo é obrigatório em **cada clone**, em cada máquina. O arquivo `.pre-commit-config.yaml` vem junto com o repositório, mas o hook ativo fica na pasta `.git/hooks/`, que não é versionada. Sem o `pre-commit install`, commits com erro passam sem aviso.

### Passo 6 — Conferir se está tudo certo

```bash
pre-commit run --all-files
```

Resultado esperado:

```
flake8...................................................................Passed
```

Na primeira execução aparecem linhas `[INFO]` enquanto o flake8 é baixado. Isso é normal e pode levar alguns minutos.

---

## 3. Executando a aplicação

Com o venv ativo, na raiz do projeto:

```bash
flask --app hello run
```

O terminal mostra `Running on http://127.0.0.1:5000`. Abra no navegador:

| Endereço                      | O que retorna                           |
| ----------------------------- | --------------------------------------- |
| http://127.0.0.1:5000/        | Mensagem de boas-vindas ("Hello World") |
| http://127.0.0.1:5000/status  | `{"status": "online"}`                  |
| http://127.0.0.1:5000/tickets | Lista de chamados em JSON               |

Para parar a API, pressione `Ctrl+C` no terminal.

---

## 4. Qualidade de código

### Rodando o flake8 manualmente

```bash
flake8 .
```

Se o comando terminar **sem exibir nenhuma linha**, o código está dentro do padrão. Cada apontamento segue o formato:

```
arquivo:linha:coluna: CÓDIGO mensagem
```

Exemplo: `utils.py:3:5: F841 local variable 'sobra' is assigned to but never used`

- Códigos **E** e **W**: estilo (PEP 8), como linhas em branco ou linhas longas.
- Códigos **F**: erros lógicos prováveis, como imports ou variáveis não usados.

A configuração fica no arquivo `.flake8`, que ignora pastas que não são código da equipe (`venv`, `__pycache__`, `.git`).

### O que o hook faz a cada commit

Ao rodar `git commit`, o pre-commit executa o flake8 nos arquivos `.py` que estão na área de staging:

- **Sem apontamentos** → `Passed` e o commit é criado.
- **Com apontamentos** → `Failed`, o commit é **bloqueado** e os erros aparecem no terminal.

Para corrigir um commit bloqueado:

1. Abra o arquivo na linha indicada e corrija o problema.
2. Salve o arquivo (`Ctrl+S`).
3. Rode `git add <arquivo>` de novo (o hook analisa a versão que está no staging).
4. Rode o `git commit` novamente.

### Testando se o hook está funcionando

Crie um arquivo `teste_hook.py` com uma variável não usada:

```python
def teste():
    sobra = 42
    return 1
```

```bash
git add teste_hook.py
git commit -m "teste: hook deve barrar"
```

O resultado deve ser `Failed` com o código `F841`. Depois desfaça o teste:

```bash
git restore --staged teste_hook.py
```

E apague o arquivo `teste_hook.py`.

> Se o commit passar mesmo com o erro, o hook não está ativo: volte ao **Passo 5** com o venv ativo.

---

## 5. Como contribuir

A branch `main` é protegida: nenhuma alteração vai direto para ela. O fluxo da equipe é:

1. Atualize a `main` local:

```bash
   git checkout main
   git pull
```

2. Crie uma branch para a sua tarefa:

```bash
   git checkout -b feature/nome-da-tarefa
```

3. Faça as alterações e commite (o hook roda o flake8 automaticamente):

```bash
   git add .
   git commit -m "feat: descreve a alteração"
```

Use prefixos nas mensagens: `feat:` (nova funcionalidade), `fix:` (correção), `chore:` (configuração/manutenção), `docs:` (documentação).

4. Envie a branch para o GitHub:

```bash
   git push -u origin feature/nome-da-tarefa
```

5. No GitHub, abra um **Pull Request** para a `main`, peça revisão de um colega e faça o merge após a aprovação.

### Observações

- Não use `git commit --no-verify` para pular o hook, exceto em emergência combinada com a equipe.
- Não gere o `requirements.txt` com `pip freeze`: ele passaria a incluir o flake8, o pre-commit e as dependências deles. Ferramentas de desenvolvimento vão no `requirements-dev.txt`.
