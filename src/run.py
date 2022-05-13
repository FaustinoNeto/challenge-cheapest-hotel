from datetime import datetime

import my_module


my_module.intro()
tipocliente = str(input('Cliente Regular ou Reward: ?')).strip().capitalize()
data = my_module.get_data()

saida = my_module.get_cheapest_hotel(tipocliente, data)
print(saida)

