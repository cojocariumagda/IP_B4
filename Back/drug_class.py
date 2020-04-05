import prospectus_class
import feedback_class

class Drug:
    __name = ""
    __prospectus = prospectus_class.Prospectus()
    __price = 0
    __places = []
    __feedback = feedback_class.Feedback()

    def change_information(self, new_drug):
        print("Here i'll check that you are connected as a admin")
        print("Here i'll change the information")