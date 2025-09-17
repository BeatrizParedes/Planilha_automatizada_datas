import pandas as pd
import datetime
import os

ARQUIVO = "ofertas.xlsx"

def criar_excel():
    """Cria o arquivo Excel se não existir"""
    if not os.path.exists(ARQUIVO):
        df = pd.DataFrame(columns=["ID", "Descricao", "Data_Fim", "Expirada"])
        df.to_excel(ARQUIVO, index=False)
        print("📂 Arquivo 'ofertas.xlsx' criado com sucesso!")

def carregar_ofertas():
    """Carrega ofertas do Excel"""
    return pd.read_excel(ARQUIVO)

def salvar_ofertas(df):
    """Salva o DataFrame no Excel"""
    df.to_excel(ARQUIVO, index=False)

# ---------------- CRUD ----------------

def adicionar_oferta(descricao, data_fim):
    """CREATE"""
    df = carregar_ofertas()
    novo_id = 1 if df.empty else df["ID"].max() + 1
    nova_oferta = {"ID": novo_id, "Descricao": descricao, "Data_Fim": data_fim, "Expirada": "Nao"}
    df = pd.concat([df, pd.DataFrame([nova_oferta])], ignore_index=True)
    salvar_ofertas(df)
    print(f"✅ Oferta adicionada: {descricao} (até {data_fim})")

def listar_ofertas():
    """READ"""
    df = carregar_ofertas()
    if df.empty:
        print("⚠️ Nenhuma oferta cadastrada.")
        return
    print("\n📋 Ofertas cadastradas:")
    print(df.to_string(index=False))

def atualizar_oferta(oferta_id, nova_desc=None, nova_data=None):
    """UPDATE"""
    df = carregar_ofertas()
    if oferta_id not in df["ID"].values:
        print("❌ Oferta não encontrada.")
        return
    if nova_desc:
        df.loc[df["ID"] == oferta_id, "Descricao"] = nova_desc
    if nova_data:
        df.loc[df["ID"] == oferta_id, "Data_Fim"] = nova_data
    salvar_ofertas(df)
    print("✏️ Oferta atualizada com sucesso!")

def excluir_oferta(oferta_id):
    """DELETE"""
    df = carregar_ofertas()
    if oferta_id not in df["ID"].values:
        print("❌ Oferta não encontrada.")
        return
    df = df[df["ID"] != oferta_id]
    salvar_ofertas(df)
    print("🗑️ Oferta excluída com sucesso!")

def verificar_ofertas():
    """Verifica e atualiza status das ofertas"""
    hoje = datetime.date.today()
    df = carregar_ofertas()
    expiradas = []

    for i, row in df.iterrows():
        data_fim = pd.to_datetime(row["Data_Fim"]).date()
        if data_fim < hoje:
            df.at[i, "Expirada"] = "Sim"
            expiradas.append((row["Descricao"], row["Data_Fim"]))
        else:
            df.at[i, "Expirada"] = "Nao"

    salvar_ofertas(df)

    print(f"\n📅 Hoje é {hoje}\n")
    if expiradas:
        print("❌ Ofertas vencidas:")
        for desc, data in expiradas:
            print(f"- {desc} (expirou em {data})")
    else:
        print("✅ Nenhuma oferta vencida hoje.")

if __name__ == "__main__":
    criar_excel()

    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar nova oferta")
        print("2 - Listar ofertas")
        print("3 - Atualizar oferta")
        print("4 - Excluir oferta")
        print("5 - Verificar ofertas vencidas")
        print("6 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            desc = input("Descrição da oferta: ")
            data = input("Data final (AAAA-MM-DD): ")
            adicionar_oferta(desc, data)
        elif escolha == "2":
            listar_ofertas()
        elif escolha == "3":
            listar_ofertas()
            try:
                oferta_id = int(input("Digite o ID da oferta a atualizar: "))
                nova_desc = input("Nova descrição (ou deixe vazio): ")
                nova_data = input("Nova data (AAAA-MM-DD) (ou deixe vazio): ")
                atualizar_oferta(oferta_id, nova_desc if nova_desc else None, nova_data if nova_data else None)
            except ValueError:
                print("⚠️ ID inválido.")
        elif escolha == "4":
            listar_ofertas()
            try:
                oferta_id = int(input("Digite o ID da oferta a excluir: "))
                excluir_oferta(oferta_id)
            except ValueError:
                print("⚠️ ID inválido.")
        elif escolha == "5":
            verificar_ofertas()
        elif escolha == "6":
            print("👋 Saindo...")
            break
        else:
            print("⚠️ Opção inválida.")
