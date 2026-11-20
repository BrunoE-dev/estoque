# controle_acesso.py — a classe ControleAcesso guarda os usuários e cuida do login
# É a mesma ideia da Almoxarifado: uma classe que guarda uma lista de objetos.

import secrets

from usuarios.papeis import papeis_validos

# A mesma mensagem para matrícula que não existe e senha errada:
# se fossem diferentes, daria para descobrir quais matrículas existem.
CREDENCIAL_INVALIDA = "Matrícula ou senha inválida."

class ControleAcesso:
    # Construtor: começa sem usuários e sem ninguém logado
    def __init__(self):
        self.usuarios = []
        self.sessoes = {} # token → matrícula de quem está logado
 
 
 # Devolve o Usuario com essa matrícula, ou None
    def buscar(self, matricula):
        for u in self.usuarios:
            if u.matricula == matricula:
                return u
        return None

    # Guarda um usuário novo; False se a matrícula já existe
    def cadastrar(self, usuario):
        achado = self.buscar(usuario.matricula)
        if achado is not None:
            return False
        self.usuarios.append(usuario)
        return True

    
    def entrar(self, senha, matricula):
        s = self.buscar(matricula)
        if s is None or not s.conferir_senha(senha) or s.situacao != "ativo":
            return None
        
        token = secrets.token_hex(16)
        self.sessoes[token] = matricula
        return token


    def usuario_logado(self, token):
        matricula = self.sessoes(token)
        if matricula is None:
            return None
        return self.buscar(matricula)


    def sair(self, token):
        if token not in self.sessoes:
            return False
        del self.sessoes[token]
        return True

    def mudar_papeis(self, quem, matricula, papeis, papel):
        if not quem.pode("mudar_papeis"):
            return "Você não tem permissão."

        alvo = self.buscar(matricula)
        if alvo is None:
             return "Sócio não encontrado."

        if len(papeis) == 0:
            return "Escolha pelo menos um papel."

        for papeis in papeis:
            if papel not in papeis_validos():
                return "Papel Invalidos" + papel
        alvo.papeis = papeis
        return None

    def listar_usuarios(self):
        users = []
        for u in self.usuarios:
            users.append({
                "matricula":u.matricula,
                "nome":u.nome,
                "papeis": u.papeis,
                "surpervisor": u.supervisor,
                "situacao": u.situacao
            })
            return users

