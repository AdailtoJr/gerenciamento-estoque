from app import db

# ####################
# Cada classe é uma tabela no banco de dados
# ####################

#Casa herda todas as características de db.Model
class Casa(db.Model):

    #Propriedades de Casa
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qtdQuartos = db.Column(db.Integer)
    qtdBanheiros = db.Column(db.Integer)
    rua = db.Column(db.String(100))

    #Construtor, recebendo os parâmetros para adicionar ao objeto
    def __init__(self, qtdQuartos, qtdBanheiros, rua):
        self.qtdQuartos = qtdQuartos
        self.qtdBanheiros = qtdBanheiros
        self.rua = rua


###################################  Projeto  ###############################################

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    documento = db.Column(db.String(16), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

    def __init__(self, nome, tipo, documento, endereco, telefone, data_nascimento):
        self.nome = nome
        self.tipo = tipo
        self.documento = documento
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento


class Produtos(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(40))
    qtd = db.Column(db.Integer)
    tipo = db.Column(db.String(15))
    preco = db.Column(db.Float)
    descricao = db.Column(db.String(100))


    def __init__(self, nome, qtd, tipo, preco, descricao):
        self.nome = nome
        self.qtd = qtd
        self.tipo = tipo
        self.preco = preco
        self.descricao = descricao
