'''
A lista ex é responsável por armazenar o saldo da conta do usuário
'''
ex=[]
cpf=[]
cartao=[]
card=[]
senha=[]
import random
def banco():
    while True:
        print('Bem-vindo ao banco Ivandro S.A!')
        n=input('Digite o seu nome completo:\t')
        a=int(input(f'Qual operação gostaria de realizar Sr.(a) {n}?\n[1] Login sem cartão [2] Login com cartão [3] Abrir conta\n'))
        if a==1:
            b=input('Digite o seu CPF:\t')
            c=len(str(b))
            if c!=11:
                print('CPF inválido tente novamente')
                break
            else:
                if b in cpf:
                    print(f'Bem-vindo Sr.{n}!')
                    d = int(input(f'Qual operação gostaria de realizar Sr.(a) {n}?\n[1] Depósito [2] Extrato\n'))
                    if d==1:
                        f=int(input('Qual a quantidade que deseja depositar?\n'))
                        ex.append(f)
                        if f==0:
                            print('Não é possível depositar nenhum valor!')
                            break
                        else:
                            s=int(input('Digite a sua senha de 6 dígitos:\n'))
                            if s in senha:
                                print('Depoósito realizado!')
                                return banco()
                    elif d==2:
                        s = int(input('Digite a sua senha de 6 dígitos:\n'))
                        if s in senha:
                            print(f'O Extrato da sua conta é: R$', sum(ex))
                            return banco()
                else:
                    print('CPF não cadastrado!')
                    break
        elif a==2:
            b=int(input('Digite o número do seu cartão:\t'))
            c=len(str(b))
            if c!=16:
                print('Cartão inválido!')
                break
            else:
                if b in cartao:
                    print(f'Bem-vindo Sr.{n}!')
                    d=int(input(f'Qual operação gostaria de realizar Sr.(a) {n}?\n[1] Depósito [2] Extrato\n'))
                    if d==1:
                        f=float(input('Qual a quantidade que deseja depositar?\n'))
                        if f==0:
                            print('Não é possível depositar nenhum valor!')
                            break
                        else:
                            ex.append(f)
                            q=int(input('Digite a sua senha:\t'))
                            if q in senha:
                                print('Depósito realizado!')
                                return banco()
                    elif d==2:
                        print('O Extrato da sua conta é:', sum(ex))
                        return banco()
                else:
                    print('Nº de cartão não registrado!')
                    break
        elif a==3:
            b = input('Digite o seu CPF:\t')
            c = len(str(b))
            if c!=11:
                print('CPF inválido!\nCadastro cancelado')
                break
            else:
                cpf.append(b)
                d=int(input(f'Sr.{n}, Qual o seu número de telefone?\n'))
                e=len(str(d))
                if e!=9:
                    print('Número inválido!\nCadastro cancelado')
                    break
                else:
                    f=int(input('Insira o seu CEP:\n'))
                    g=len(str(f))
                    if g!=8:
                        print('CEP inválido!\nCadastro cancelado')
                    else:
                        for i in range(16):
                            numcard=random.randint(1,9)
                            card.append(numcard)
                        strings = [str(card) for card in card]
                        a_string = "".join(strings) # O número do cartão é transformado em str para entrar na lista com 16 caracteres
                        an_integer = int(a_string)
                        senha_ind=int(input('Digite uma senha numérica de 6 dígitos:\n'))
                        op=len(str(senha_ind))
                        if op!=6:
                            print('Senha inválida!\nCadastro cancelado')
                        else:
                            cartao.append(an_integer)
                            senha.append(senha_ind)
                            print('O número do seu cartão é:',an_integer)
                            print('Cadastro realizado com sucesso!\nO seu cartão chegará em até 15 dias úteis\nObrigado por utilizar nossos serviços')
        else:
            print('Opção inválida!')
        return banco
while True:
    banco()
    z=int(input('Deseja realizar outra operação?\n[1] Sim [2] Não\n'))
    if z==1:
        banco()
    elif z==2:
        print('Encerrando programa...')
        break
    else:
        print('Opção inválida!\nEncerrando programa...')
        break