
def intro():
    import emoji
    print(f'A rede de \033[1;34mHotel SYNGENTA \033[m conta com:', end='')
    print(emoji.emojize("""
    Ridgewood   \033[33m:star: :star: :star: :star: :star:\033[m Estrelas
    Bridgewood \033[33m :star: :star: :star: :star:\033[m   Estrelas
    lakewood    \033[33m:star: :star: :star: \033[m    Estrelas
            """))


def get_data():
    from datetime import datetime
    from time import sleep
    datalista = list()
    while True:
        str_data = str(input('\033[33mDigite a data da reserva\033[m [formato -> 01/01/2022]:')).strip()
        dataf = datetime.strptime(str_data, '%d/%m/%Y').date()
        b = str(input('Deseja adicionar mais data? [S/N]')).strip()
        datalista.append(dataf)
        if b in 'Nn':
            break
        elif b in 'sS':
            print('Data adicionada')
    print('\033[33mDATAS COLETADAS PARA ANÁLISE\033[m')
    sleep(2)
    return datalista


def get_cheapest_hotel(tipocliente, datalista):
    result = 0
    ok = False
    while True:
        n = tipocliente.strip().capitalize()
        if n == 'Regular' or n == 'Reward':
            ok = True
        else:
            tipocliente = str(input('Cliente incorreto ->  Regular ou Reward: ')).strip().capitalize()

        if ok:
            break
    print(f'Obrigado pela confirmação \033[1;31mCliente {n} \033[m')

    if n == 'Regular':
        c_dia_de_semana = c_fim_de_semana = 0
        for d in datalista:
            if d.isoweekday() <= 5:
                c_dia_de_semana += 1
            else:
                c_fim_de_semana += 1
        g = dict()
        g['lakewood'] = (c_dia_de_semana * 110) + (c_fim_de_semana * 90)
        g['bridgewood'] = (c_dia_de_semana * 160) + (c_fim_de_semana * 60)
        g['ridgewood'] = (c_dia_de_semana * 220) + (c_fim_de_semana * 150)
        print(f'Os orçamentos em cada Hotel: \033[1;34m {g}  \033[m')
        if g['lakewood'] == g['bridgewood'] and g['lakewood'] < g['ridgewood']:
            result = 'Lakewood'
        elif g['bridgewood'] == g['ridgewood'] and g['bridgewood'] < g['lakewood']:
            result = 'Ridgewood'
        elif g['ridgewood'] == g['lakewood'] and g['ridgewood'] < g['bridgewood']:
            result = 'Ridgewood'
        elif g['lakewood'] < g['bridgewood'] and g['lakewood'] < g['ridgewood']:
            result = 'Lakewood'
        elif g['bridgewood'] < g['lakewood'] and g['bridgewood'] < g['ridgewood']:
            result = 'Bridgewood'
        elif g['ridgewood'] < g['bridgewood'] and g['ridgewood'] < g['lakewood']:
            result = 'Ridgewood'

        return result

    else:
        c_dia_de_semana = c_fim_de_semana = 0
        for d in datalista:
            if d.isoweekday() <= 5:
                c_dia_de_semana += 1
            else:
                c_fim_de_semana += 1

        g = dict()
        g['lakewood'] = (c_dia_de_semana * 80) + (c_fim_de_semana * 80)
        g['bridgewood'] = (c_dia_de_semana * 110) + (c_fim_de_semana * 50)
        g['ridgewood'] = (c_dia_de_semana * 100) + (c_fim_de_semana * 40)
        print(f'Os orçamentos em cada Hotel: \033[1;34m {g}  \033[m')
        if g['lakewood'] == g['bridgewood'] and g['lakewood'] < g['ridgewood']:
            result = 'Lakewood'
        elif g['bridgewood'] == g['ridgewood'] and g['bridgewood'] < g['lakewood']:
            result = 'Ridgewood'
        elif g['ridgewood'] == g['lakewood'] and g['ridgewood'] < g['bridgewood']:
            result = 'Ridgewood'
        elif g['lakewood'] < g['bridgewood'] and g['lakewood'] < g['ridgewood']:
            result = 'Lakewood'
        elif g['bridgewood'] < g['lakewood'] and g['bridgewood'] < g['ridgewood']:
            result = 'Bridgewood'
        elif g['ridgewood'] < g['bridgewood'] and g['ridgewood'] < g['lakewood']:
            result = 'Ridgewood'

        return result
