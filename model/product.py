class Product:
    def __init__(self,data):
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
        self.Nome = Lista[0]
        self.Sobrenome = Lista[1]
        self.Email = Lista[2]
        self.Titulo = Lista[3]
        self.Descricao = Lista[4]
        self.Placa = Lista[5]
        self.Cor = Lista[6]
        self.KM = Lista[7]
        self.Preco = Lista[8]
        self.Marca = Lista[9]
        self.Tipo = Lista[10]
        self.Ano = Lista[11]
        self.Cambio = Lista[12]
        self.Combustivel = Lista[13]
        self.Direcao = Lista[14]
        self.Estado = Lista[15]
        self.Foto = Lista[16]

    def getPlaca(self):
        return self.Placa
    
    def getEmail(self):
        return self.Email
    
    def requestPhoto(self):
        return self.Foto
