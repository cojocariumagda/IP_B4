import drug_class


class Recomandation:
    __list_symptoms = []
    __list_drugs = []
    # cred ca nu mai trebuie sa am userul pentru ca doar un user o sa fie conectat pe un thread

    def get_alternative_drug(self, get_recomandation):
        print("Aici vor fi medicamente alternative")

    def get_symptoms(self, baza_de_date):
        print("Aici voi extrage simptomele userului si le voi salva in list_symptoms")

    def give_recomandation(self, baza_de_date):
        print("Pe baza informatiilor oferite de catre client, voi face un algoritm de oferire a unei recomandari")
