from faker import Faker


def gerar_nome():
    fake = Faker()
    nome = fake.name()
    return nome


def gerar_email():
    fake = Faker()
    email = fake.email()
    return email


def gerar_senha():
    fake = Faker()
    senha = fake.password()
    return senha


def gerar_dados_registro():
    nome = gerar_nome()
    email = gerar_email()
    senha = gerar_senha()

    return email, nome, senha
