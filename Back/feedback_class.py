
class Feedback:
    __username = ""
    __comment = ""
    __rating = 0.0
    __list_of_rates = []

    def __init__ (self):
        self.__list_of_rates[0] = 0
        self.__list_of_rates[1] = 0
        self.__list_of_rates[2] = 0
        self.__list_of_rates[3] = 0
        self.__list_of_rates[4] = 0

    def check_feedback(self, comment):
        print("Aici va fi verificat comentariul pentru a fi unul civilizat.")

    def add_rating(self, new_rating):
        self.__list_of_rates[new_rating-1] += 1
        current_sum = 0
        current_count = 0
        for i in range(4):
            current_sum += self.__list_of_rates[i] * (i+1)
            current_count += self.__list_of_rates[i]
        self.__rating = current_sum / current_count


# lista de feedbackuri sau ceva de genul
list_feedback = []