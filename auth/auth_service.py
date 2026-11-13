class AuthService:
    def __init__(self, uzivatele):
        self.uzivatele = uzivatele

    def najdi_uzivatele(self, email):
        for uzivatel in self.uzivatele:
            if uzivatel.email == email:
                return uzivatel

        return None

    def prihlas(self, email, heslo):
        uzivatel = self.najdi_uzivatele(email)

        if uzivatel is None:
            return None

        if uzivatel.over_heslo(heslo):
            return uzivatel

        return None

    def najdi_uzivatele_id(self, id):
        for uzivatel in self.uzivatele:
            if uzivatel.id == id:
                return uzivatel
        return None