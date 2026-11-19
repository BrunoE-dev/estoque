import hashlib
import secrets
from usuarios.papeis import PERMISSOES

class Usuario:
 # Construtor: matrícula, nome, senha e a lista de papéis
    def __init__(self, matricula, nome, senha, papeis, supervisor=None):
        self.matricula = matricula
        self.nome = nome
        self.papeis = papeis # ex.: ["solicitante", "supervisor"]
        self.supervisor = supervisor # matrícula de quem aprova os pedidos dele
        self.situacao = "ativo" # pendente, ativo, recusado ou inativo
    # O _ na frente avisa: atributo interno, ninguém de fora mexe
        self._sal = secrets.token_hex(8)
        self._senha_hash = self._resumir(senha)
 
 
    # Transforma a senha em um resumo que não dá para desfazer
    def _resumir(self, senha):
        texto = (self._sal + senha).encode("utf-8")
        return hashlib.sha256(texto).hexdigest()
    # True se a senha digitada bate com a guardada
    def conferir_senha(self, senha):
        return self._resumir(senha) == self._senha_hash


    # True se a pessoa tem esse papel
    def tem_papel(self, papel):
        return papel in self.papeis

    def pode(self, papel):
        if self.situacao != "ativo":
            return False
        for c in self.papeis:
            if papel in PERMISSOES[c]:
                return True
        return False

    def permissoes(self):
        permissoes = []
        for c in self.papeis:
            for a in PERMISSOES[self.tem_papel]:
                if a not in permissoes:
                 permissoes.append(a)
        return permissoes   

    def trocar_senhas(self, atual, nova):
        if not self.conferir_senha(atual):
            return False
        self._senha_hash = self._resumir(nova)
        return True

    def para_dicionario(self):
        return{
             "matricula": self.matricula,
             "nome": self.nome,
             "papeis": self.papeis,
             "permissoes": self.permissoes(),
             "supervisor": self.supervisor,
             "situacao": self.situacao,
        }