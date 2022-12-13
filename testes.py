'''window.disappear()
window.reappear()'''
from datetime import datetime



nascimento = "13/12/202"

formato = "%d/%m/%Y"

print(type(datetime.strptime(nascimento, formato)))