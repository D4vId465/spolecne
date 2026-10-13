class User:
    def __init__(self, id, jmeno, prijmeni, email, nickname, role):
        self.id = id
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.email = email
        self.nickname = nickname
        self.role = role
        self.__aktivni = True
def cele_jmeno(self):
    return f"{self.jmeno} {self.prijmeni}"

def je_admin(self):
    return self.role == "admin"

def je_aktivni(self):
    return self.__aktivni

def deaktivni(self):
    self.__aktivni = False