import re


def nome_valido(nome):
    return nome.replace(' ', '').isalpha()


def telefone_valido(telefone):
    """ Esse método verifica atravez de um regex se o telefone informado pelo usuário é valido ou não.

    Args:
        telefone (string): numero de telefone informado pelo usuário no endpoint de contato

    Returns:
        boolean: verdadeiro ou falso
    """
    modelo = '(\(\d{2}\)\s)(\d{4,5}\-\d{4})'
    resposta = re.findall(modelo, telefone)
    return resposta
