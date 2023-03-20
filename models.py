from gerenciadorcontrato import db

#---------------------------------------------------------------------------------------------------------------------------------
#TABELA: USUÁRIOS
#ORIGEM: BANCO DE DADOS
#---------------------------------------------------------------------------------------------------------------------------------
class tb_user(db.Model):
    cod_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_user = db.Column(db.String(50), nullable=False)
    password_user = db.Column(db.String(50), nullable=False)
    status_user = db.Column(db.Integer, nullable=False)
    login_user = db.Column(db.String(50), nullable=False)
    cod_usertype = db.Column(db.Integer, nullable=False)
    email_user = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

#---------------------------------------------------------------------------------------------------------------------------------
#TABELA: TIPO USUÁRIOS
#ORIGEM: BANCO DE DADOS
#---------------------------------------------------------------------------------------------------------------------------------
class tb_usertype(db.Model):
    cod_usertype = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_usertype = db.Column(db.String(50), nullable=False)
    status_usertype = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name    
 
#---------------------------------------------------------------------------------------------------------------------------------
#TABELA: CLIENTES
#ORIGEM: BANCO DE DADOS
#---------------------------------------------------------------------------------------------------------------------------------
class tb_clientes(db.Model):
    cod_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomerazao_cliente = db.Column(db.String(50), nullable=False)
    nomefantasia_cliente = db.Column(db.String(50), nullable=False)
    end_cliente = db.Column(db.String(50), nullable=False)
    numend_cliente = db.Column(db.String(50), nullable=False)
    bairro_cliente = db.Column(db.String(50), nullable=False)
    cidade_cliente = db.Column(db.String(50), nullable=False)
    uf_cliente = db.Column(db.String(50), nullable=False)
    complemento_cliente = db.Column(db.String(50), nullable=False)
    cnpj_cliente = db.Column(db.String(50), nullable=False)
    status_cliente = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name    
