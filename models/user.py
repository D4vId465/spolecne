class User:
    def __init__(self, id, jmeno, prijmeni, password, email, nickname, role="Uzivatel"):
        self.id = id
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.password = password
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

    def over_heslo(self,heslo):
        return self.password == heslo