from utils import *
from bradleyTerry import *

option_map = {"1": "(1) Display Alex's Top 25 Rankings",
                      "2": "(2) Display the predictions for this week's games",
                      "3": "(3) Display the prediction for a hypothetical game",
                      "q": "(q) Exit"}

def bradleyTerryDriver(n_iterations):
    CURRENT_WEEK = getCurrentWeek()
    schedule_data = getScheduleData(CURRENT_WEEK)
    schools = list(set(schedule_data.Winner.tolist() + schedule_data.Loser.tolist())) 
    matrix = createMatrix(schools)
    wins_dict = createWinsDict(schedule_data=schedule_data, schools=schools)
    index_dict = {}
    for i in range(len(schools)):
       index_dict[schools[i]] = i
    matrix = populateMatrix(matrix, wins_dict, index_dict, schools)
    parameter_vec = [1 for x in range(len(schools) + 3)]
    
    for i in range(n_iterations):
       parameter_vec = iterate(parameter_vec, matrix)
    ranking_dict = {schools[i]: parameter_vec[i] for i in range(len(schools))}
    ranking_dict = sorted(ranking_dict.items(), key=lambda x:x[1], reverse = True)
    ranking = pd.DataFrame(ranking_dict, columns = ["school", "rank_val"])
    ranking["rank"] = ranking["rank_val"].rank(ascending=False).astype(int)
    disp = ranking.head(25).reset_index().rename({"index": "ranking"}, axis = 'columns')
    disp['ranking'] = disp['ranking'] + 1
    print(disp.to_markdown(index = False))
    return ranking

def displayOptions():
    for key in option_map.keys():
            print(option_map[key])
    


def main():
    
    while True:
        
        print("Welcome to Alex's College Football Info Hub")
        displayOptions()
        command = input("Make a selection: ")
        if command == "1":
            bradleyTerryDriver(1)
        elif command == "2":
            pass
        elif command == "3":
            pass
        elif command == "q":
            break
        else:
            print("That selection is not recognized. Please make an appropriate selection")


if __name__ == "__main__":
    main()
