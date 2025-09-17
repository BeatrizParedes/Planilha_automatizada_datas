# Gerenciador de Ofertas (CRUD com Excel)

Este projeto é um programa em **Python** que permite gerenciar ofertas promocionais com **datas de validade**. As informações ficam salvas em uma planilha Excel (`ofertas.xlsx`) e o sistema permite criar, ler, atualizar e excluir ofertas (CRUD). Além disso, o programa mostra diariamente quais ofertas já venceram e quais ainda estão ativas.

---

## Funcionalidades

1. **Adicionar oferta (Create)**

   * Permite cadastrar uma nova oferta com **descrição** e **data final**.

2. **Listar ofertas (Read)**

   * Mostra todas as ofertas cadastradas em formato de tabela.

3. **Atualizar oferta (Update)**

   * Permite editar a descrição e/ou data de validade de uma oferta existente.

4. **Excluir oferta (Delete)**

   * Remove uma oferta do Excel pelo ID.

5. **Checar ofertas vencidas**

   * Compara as datas com o dia atual e mostra quais ofertas já expiraram.

6. **Armazenamento persistente**

   * Todos os dados ficam salvos no Excel (`ofertas.xlsx`).

---

## Estrutura do Excel

| ID | Descricao          | Data\_Fim  | Expirada |
| -- | ------------------ | ---------- | -------- |
| 1  | Desconto em Camisa | 2025-09-20 | Nao      |
| 2  | Promoção de Ecobag | 2025-09-10 | Sim      |

* **ID** → número único de cada oferta.
* **Descricao** → texto da promoção.
* **Data\_Fim** → data de validade no formato `AAAA-MM-DD`.
* **Expirada** → indica se a oferta já venceu (`Sim` ou `Nao`).

---

## Instalação

1. Clone ou baixe este repositório.
2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv .venv
   ```
3. Ative o ambiente virtual:

   * Windows PowerShell:

     ```bash
     .venv\Scripts\Activate.ps1
     ```
   * Linux/Mac:

     ```bash
     source .venv/bin/activate
     ```
4. Instale as dependências:

   ```bash
   pip install pandas openpyxl
   ```

---

## Como usar

Execute o programa:

```bash
python gerenciar_ofertas.py
```

Você verá o seguinte menu:

```
--- MENU ---
1 - Adicionar nova oferta
2 - Listar ofertas
3 - Atualizar oferta
4 - Excluir oferta
5 - Verificar ofertas vencidas
6 - Sair
```

* **Adicionar oferta** → escolha a opção 1, informe a descrição e a data final.
* **Listar ofertas** → opção 2.
* **Atualizar oferta** → opção 3, informe o ID e os novos dados.
* **Excluir oferta** → opção 4, informe o ID.
* **Verificar vencidas** → opção 5, lista ofertas vencidas e ativas.

---

## Criando Executável

1. Instale o PyInstaller:

   ```bash
   pip install pyinstaller
   ```
2. Gere o `.exe`:

   ```bash
   pyinstaller --onefile gerenciar_ofertas.py
   ```
3. O executável estará na pasta `dist/gerenciar_ofertas.exe`.

---

## Automação diária (opcional)

Você pode configurar o **Agendador de Tarefas do Windows** para rodar o `.exe` todo dia em um horário fixo, garantindo que sempre terá o relatório atualizado de ofertas vencidas e ativas.

---

## Próximos passos

* Melhorar interface e adicionar filtros por data ou descrição.
* Integração com envio de alertas por e-mail ou WhatsApp.
