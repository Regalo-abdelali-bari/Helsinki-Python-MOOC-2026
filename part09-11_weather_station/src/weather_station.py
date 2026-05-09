# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__ (self,name : str):
        self.__name = name
        self.__entry = []

    def add_observation(self,observation: str):
        self.__entry.append(observation)

    def latest_observation(self):
        return self.__entry[-1] if len(self.__entry) > 0 else ""

    def number_of_observations(self):
        return len(self.__entry)

    def __str__(self):
        return f"{self.__name}, {len(self.__entry)} observations"

