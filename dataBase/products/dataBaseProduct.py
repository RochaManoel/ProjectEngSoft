import json
from model.product import Product

class DataBaseProduct:
    def __init__(self):
        self.path = "dataBase\\products\\productData.json"

    def setProduct(self, data):
        with open(self.path) as file:
            listFile = json.load(file)
        listFile.append(self.setJson(data))
        with open(self.path,"w") as file:
            json.dump(listFile, file)

    def setJson(self,data):
        Lista = []
        size = len(data)
        data = data[1:size-1]
        data = data.split(',')
        for dt in data:
            dt = dt.split(':')[-1]
            s = len(dt)
            dt = dt[1:s-1]
            Lista.append(dt)
        print(Lista)
        Obj = {
                "Nome": Lista[0],
                "Sobrenome": Lista[1],
                "Email": Lista[2],
                "Titulo": Lista[3],
                "Descricao": Lista[4],
                "Placa": Lista[5],
                "Cor": Lista[6],
                "KM": Lista[7],
                "Preco": Lista[8],
                "Marca": Lista[9],
                "Tipo": Lista[10],
                "Ano": Lista[11],
                "Cambio": Lista[12],
                "Combustivel": Lista[13],
                "Direcao": Lista[14],
                "Potencia": Lista[15],
                "Estado": Lista[16],
                "FotoCapa": Lista[17]
        }
        return Obj
    