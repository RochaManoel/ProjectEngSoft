import json
import smtplib
from email.message import EmailMessage
from model.user import User

class DataBaseUser:
    def __init__(self):
        self.path = "dataBase\\users\\UserData.json"
        self.addressEmail = "projetosoft24@gmail.com"
        self.passwordEmail = "tblgioxnsitoeaig"

    def setUser(self,data):
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
        Obj = {
            "Nome": Lista[0], 
            "Sobrenome": Lista[1], 
            "Email": Lista[2], 
            "Celular": Lista[3], 
            "Password": Lista[4]
        }
        return Obj
    
    def sendEmail(self, data):
        Lista = []
        size = len(data)
        data = data[1:size-1]
        data = data.split(',')
        for dt in data:
            dt = dt.split(':')[-1]
            Lista.append(dt)
        s = len(Lista[0])
        Lista[0] = Lista[0][1:s-1]
        msg = EmailMessage()
        msg['Subject'] = "Recuperação de senha."
        msg['From'] = self.addressEmail
        msg['To'] = Lista[0]
        msg.set_content(Lista[1])
        with smtplib.SMTP_SSL('smtp.gmail.com: 465') as smtp:
            smtp.login(self.addressEmail, self.passwordEmail)
            smtp.send_message(msg)
        return
    
    def setPassword(self, data):
        Lista = []
        size = len(data)
        data = data[1:size-1]
        data = data.split(',')
        for dt in data:
            dt = dt.split(':')[-1]
            s = len(dt)
            dt = dt[1:s-1]
            Lista.append(dt)
        with open(self.path) as file:
            listFile = json.load(file)
        for user in listFile:
            if user['Email'] == Lista[0]:
                user['Password'] = Lista[1]
        with open(self.path,"w") as file:
            json.dump(listFile, file)

    def sendMessage(self, data):
        Lista = []
        size = len(data)
        data = data[1:size-1]
        data = data.split(',')
        for dt in data:
            dt = dt.split(':')[-1]
            Lista.append(dt)
        s = len(Lista[0])
        Lista[0] = Lista[0][1:s-1]
        print(Lista)
        msg = EmailMessage()
        msg['Subject'] = "Interesse no seu anúncio!"
        msg['From'] = self.addressEmail
        msg['To'] = Lista[0]
        msg.set_content('Encontramos alguem com interesse em seu carro.\nEntre em contato com o seguinte Email: ' + Lista[1] + '\nE boas vendas!')
        with smtplib.SMTP_SSL('smtp.gmail.com: 465') as smtp:
            smtp.login(self.addressEmail, self.passwordEmail)
            smtp.send_message(msg)
        return
    