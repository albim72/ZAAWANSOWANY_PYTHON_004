class OldResistor:
    def __init__(self,ohms):
        self._ohms = ohms

    def __repr__(self):
        return f"to jest obiekt klasy OldResistor, opornik: {self._ohms}"

    def get_ohms(self):
        return self._ohms

    def set_ohms(self,ohms):
        self._ohms = ohms
