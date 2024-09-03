import sys
from utils import *
from bradleyTerry import *

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
       iterate(parameter_vec, matrix)
    ranking_dict = {schools[i]: parameter_vec[i] for i in range(len(schools))}
    ranking_dict = sorted(ranking_dict.items(), key=lambda x:x[1], reverse = True)
    ranking = pd.DataFrame(ranking_dict, columns = ["school", "rank_val"])
    ranking["rank"] = ranking["rank_val"].rank(ascending=False).astype(int)
    print(ranking.head(25))
    return ranking

def main():
    n_iterations = sys.argv[1]
    bradleyTerryDriver(10)

if __name__ == "__main__":
    main()
