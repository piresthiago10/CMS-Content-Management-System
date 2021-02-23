def data_publicacao_valida(data_publicacao, data_criacao):
    if data_publicacao > data_criacao or data_publicacao == data_criacao:
        return True
    else:
        return False
