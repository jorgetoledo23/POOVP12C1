import requests
r = requests.get("https://mindicador.cl/api")
data = r.json()
contador = 0
for d in data:
    if contador > 2:
        indicador = data[d]
        print(f"Valor {d} : {indicador['valor']}")
    contador += 1