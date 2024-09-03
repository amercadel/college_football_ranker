def iterate(parameter_vector, w_l_matrix):
  #p_i = Σ((w_ij * p_j) / (p_i + p_j)) / Σ((w_ji) / (p_i + p_j)) where j ≠ i
  for i in range(len(parameter_vector)):
    numerator = 0 # corresponds to Σ((w_ij * p_j) / (p_i + p_j))
    for j in range(len(parameter_vector)):
      if i != j:
        numerator += (w_l_matrix[i][j] * parameter_vector[j]) / (parameter_vector[j] + parameter_vector[i])
    denominator = 0 # corresponds to Σ((w_ji) / (p_i + p_j))
    for j in range(len(parameter_vector)):
      if i != j:
        denominator += (w_l_matrix[j][i]) / (parameter_vector[j] + parameter_vector[i])
    parameter_vector[i] = numerator / denominator
    
    geometric_mean = 1
    for _ in parameter_vector:
      geometric_mean *= _
    divisor = geometric_mean ** (1 / len(parameter_vector))
    for i in range(len(parameter_vector)):
      parameter_vector[i] = parameter_vector[i] / divisor

def createMatrix(schools):
  schools.sort()
  matrix = [[0 for i in range(len(schools) + 3)] for j in range(len(schools) + 3)]
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      if i >= len(matrix) - 3 or j >= len(matrix) - 3:
        matrix[i][j] = 0.5
      if i == j:
        matrix[i][j] = "-"
  
  return matrix

def createWinsDict(schedule_data, schools):
  wins_dict = {school: [] for school in schools}
  for school in schools:
    wins = schedule_data[(schedule_data.Winner == school)]["Loser"].tolist()
    wins_dict[school] = wins
  return wins_dict

def populateMatrix(matrix, wins_dict, index_dict, schools):
  for i in range(len(matrix) - 4):
    for j in range(len(matrix) - 4):
      school = schools[i]
      wins = wins_dict[school]
      for k in wins:
        idx = index_dict[k]
        matrix[i][idx] = 1
  return matrix