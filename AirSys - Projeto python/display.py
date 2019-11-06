import pymongo
import json


client = pymongo.MongoClient("mongodb+srv://uj8ul4pdodzhngd7pnmf:4VAoswiRLKEVAX4B@sensors-ihqei.mongodb.net/test?retryWrites=true&w=majority")

db = client.airsys

joao = {'nome': 'maria',
		'identidade': 12345,
		'cpf': 987654321}

resul = db.funcionarios.insert_one(joao)

#resul2 = db.funcionarios.find_one({'nome': 'joao'})

print(resul)