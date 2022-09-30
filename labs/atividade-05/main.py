def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    max_trocas = 0
   
    menor_qtd = figurinhas_da_maria if len(figurinhas_da_maria) <= len(figurinhas_do_joao) else figurinhas_do_joao
    maior_qtd  = figurinhas_da_maria if len(figurinhas_da_maria) >= len(figurinhas_do_joao) else figurinhas_do_joao

    for i, n_figurinha in enumerate(menor_qtd):
        if not n_figurinha in maior_qtd:
            for n in range(i, len(maior_qtd)):
                if n_figurinha != maior_qtd[n]:
                    aux = maior_qtd[n]
                    maior_qtd[n] = n_figurinha
                    menor_qtd[i] = aux
                    max_trocas = max_trocas + 1
                    break
    return max_trocas


if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
