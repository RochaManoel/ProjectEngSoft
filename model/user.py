class User:
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
        self.Celular = Lista[3]
        self.Password = Lista[4]

    def getEmail(self):
        return self.Email
    
    def getPassword(self):
        return self.Password
    
    def setPassword(self,Password):
        self.Password = Password

    def getEmailRequest(self,data):
        size = len(data)
        data = data[1:size-1]
        data = data.split(':')[-1]
        s = len(data)
        data = data[1:s-1]
        return data
