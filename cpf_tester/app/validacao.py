import re

def validar_cpf(cpf: str) -> bool:
   
   
    if not re.match(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$', cpf):
        return False

    # Remover caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # Verificar se o CPF contém exatamente 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Verificar se todos os números são iguais (ex: 111.111.111-11, 000.000.000-00)
    if cpf == cpf[0] * 11:
        return False


    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = digito1 if digito1 < 10 else 0


    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = digito2 if digito2 < 10 else 0


    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
