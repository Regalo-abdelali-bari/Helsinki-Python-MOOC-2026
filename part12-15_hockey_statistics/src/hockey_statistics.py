# Write your solution here
import json
class Nhl:
    def _open_file(self,file):
        with open(file) as f:
            data = f.read()
        data_nhl = json.loads(data)
        return data_nhl

    def search_player(self ,file,name):
        data_nhl = self._open_file(file)
        for item in data_nhl:
            if item["name"] == name:
                return f"{item['name']:<21}"f"{item['team']} "f"{item['goals']:>3} + "f"{item['assists']:>2} = "f"{item['goals'] + item['assists']:>3}"
                break
    
        
    def teams(self,file):
        data_nhl = self._open_file(file)
        return sorted(set([item["team"] for item in data_nhl]))

    def countries(self,file):
        data_nhl = self._open_file(file)
        return sorted(set([item["nationality"] for item in data_nhl]))

    def player_by_team(self,file ,team):
        data_nhl = self._open_file(file)
        my_list = [(item["name"],item["goals"] + item["assists"]) for item in data_nhl if item["team"] == team]
        return sorted(my_list , key=lambda items: items[1], reverse = True)

    def player_by_country(self,file,country):
        data_nhl = self._open_file(file)
        my_list = [(item["name"],item["goals"] + item["assists"]) for item in data_nhl if item["nationality"] == country]
        return sorted(my_list , key=lambda items: items[1],reverse = True)

    def players_points(self,file,times):
        data_nhl = self._open_file(file)
        my_list = [(item["goals"] + item["assists"],item["goals"],item["name"]) for item in data_nhl]
        return sorted(my_list,reverse=True)[:times]
        
    def players_goals(self,file,times):
        data_nhl = self._open_file(file)
        return sorted([(item["goals"],-item["games"],item["name"]) for item in data_nhl],reverse=True)[:times]

       

class UserInterface:
    def __init__(self):
        self.__data = Nhl()

    def search_player(self,file):
        name = input("name: ")
        print("")
        print(self.__data.search_player(file,name))

    def teams(self,file):
        for team in self.__data.teams(file):
            print(team)
        
    def countries(self,file):
        for team in self.__data.countries(file):
            print(team)

    def players_team(self,file):
        team = input("team: ")
        for item in self.__data.player_by_team(file ,team):
            print(self.__data.search_player(file , item[0]))

    def players_country(self,file):
        country = input("country: ")
        for item in self.__data.player_by_country(file ,country):
            print(self.__data.search_player(file , item[0]))

    def players_points(self,file):
        times = int(input("how many: "))
        for item in self.__data.players_points(file,times):
            print(self.__data.search_player(file , item[2]))

    def players_goals(self,file):
        times = int(input("how many: "))
        for item in self.__data.players_goals(file,times):
            print(self.__data.search_player(file , item[2]))

    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
        
    def search(self):
        file = input("file name: ")
        print(f"read the data of {len(self.__data._open_file(file))} players")
        print()
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_player(file)
            elif command == "2":
                self.teams(file)
            elif command == "3":
                self.countries(file)
            elif command == "4":
                self.players_team(file)
            elif command == "5":
                self.players_country(file)
            elif command == "6":
                self.players_points(file)
            elif command == "7":
                self.players_goals(file)

                
ecran = UserInterface()
ecran.search()






