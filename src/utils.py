import pandas as pd
import datetime

team_dict = {0: ["Air Force"], 1: ["Akron"], 2: ["Alabama"], 3: ["Appalachian State", "App State", "Appalachian St", "App St"], 4: ["Arizona"], 5: ["Arizona State", "Arizona St"], 6: ["Arkansas"], 7: ["Arkansas State", "Arkansas St"], 8: ["Army"], 9: ["Auburn"], 
             10: ["Ball State", "Ball St"], 11: ["Baylor"], 12: ["Boise State", "Boise St"], 13: ["Boston College", "BC"], 14: ["Bowling Green"], 15: ["Buffalo"], 16: ["BYU", "Brigham Young"], 17: ["California", "Cal", "UC Berkeley"], 18: ["Central Michigan", "CMU"], 19: ["Charlotte", "UNC-Charlotte"], 
             20: ["Cincinnati", "UC"], 21: ["Clemson"], 22: ["Coastal Carolina"], 23: ["Colorado"], 24: ["Colorado State", "Colorado St"], 25: ["Duke"], 26: ["East Carolina"], 27: ["Eastern Michigan", "EMU"], 28: ["FIU", "Florida International", "Florida Int'l"], 29: ["Florida"], 
             30: ["Florida Atlantic", "FAU"], 31: ["Florida St", "Florida State"], 32: ["Fresno State", "Fresno St"], 33: ["Georgia"], 34: ["Georgia Southern"], 35: ["Georgia State", "Georgia St"], 36: ["Georgia Tech"], 37: ["Hawaii", "Hawai'i", "Hawai`i"], 38: ["Houston", "UH"], 39: ["Illinois"], 
             40: ["Indiana"], 41: ["Iowa"], 42: ["Iowa State", "Iowa St"], 43: ["Kansas", "KU"], 44: ["Kansas State", "Kansas St", "KSU"], 45: ["Kent State", "Kent St"], 46: ["Kentucky"], 47: ["Liberty"], 48: ["Louisiana-Lafayette", "Louisiana"], 49: ["Louisiana-Monroe", "ULM"], 
             50: ["Louisiana Tech"], 51: ["Louisville"], 52: ["LSU", "Louisiana St", "Louisiana State"], 53: ["Marshall"], 54: ["Maryland"], 55: ["Memphis"], 56: ["Miami (FL)", "Miami FL", "Miami"], 57: ["Miami OH", "Miami (OH)"], 58: ["Michigan"], 59: ["Michigan State", "Michigan St"], 
             60: ["Middle Tennessee State", "Middle Tennessee St", "MTSU"], 61: ["Minnesota"], 62: ["Mississippi", "Ole Miss"], 63: ["Mississippi State", "Mississippi St"], 64: ["Missouri"], 65: ["Navy"], 66: ["NC State", "NCST", "North Carolina State", "North Carolina St"], 67: ["Nebraska"], 68: ["Nevada"], 69: ["New Mexico"], 
             70: ["New Mexico State", "New Mexico St", "NMSU"], 71: ["North Carolina", "UNC"], 72: ["North Texas", "UNT"], 73: ["Northern Illinois", "NIU"], 74: ["Northwestern"], 75: ["Notre Dame", "ND"], 76: ["Ohio", "Ohio U."], 77: ["Ohio State", "Ohio St"], 78: ["Oklahoma", "OU"], 79: ["Oklahoma State", "Oklahoma St"], 
             80: ["Old Dominion", "ODU"], 81: ["Oregon"], 82: ["Oregon State", "Oregon St"], 83: ["Penn State", "Penn St"], 84: ["Pittsburgh", "Pitt"], 85: ["Purdue"], 86: ["Rice"], 87: ["Rutgers"], 88: ["San Diego State", "San Diego St", "SDSU"], 89: ["San Jose State", "San Jose St", "SJSU"], 
             90: ["SMU", "Southern Methodist"], 91: ["South Alabama"], 92: ["South Carolina", "SCAR"], 93: ["South Florida", "USF"], 94: ["Southern Miss", "Southern Mississippi"], 95: ["Stanford"], 96: ["Syracuse"], 97: ["Texas Christian", "TCU"], 98: ["Temple"], 99: ["Tennessee", "Tenn"], 
             100: ["Texas", "UT-Austin"], 101: ["Texas A&M", "TAMU"], 102: ["Texas St", "Texas State", "Texas St-San Marcos"], 103: ["Texas Tech"], 104: ["Toledo"], 105: ["Troy"], 106: ["Tulane"], 107: ["Tulsa"], 108: ["UAB", "Alabama-Birmingham"], 109: ["UCF", "Central Florida"], 
             110: ["UCLA"], 111: ["UConn", "Connecticut", "UCONN"], 112: ["UMass", "Massachusetts", "UMASS"], 113: ["UNLV", "Nevada-Las Vegas"], 114: ["USC", "Southern California"], 115: ["UTEP", "Texas-El Paso"], 116: ["UTSA", "Texas-San Antonio"], 117: ["Utah"], 118: ["Utah State", "Utah St"], 119: ["Vanderbilt", "Vandy"], 
             120: ["Virginia", "UVA"], 121: ["Virginia Tech"], 122: ["Wake Forest", "WFU"], 123: ["Washington", "UW"], 124: ["Washington State", "Washington St"], 125: ["West Virginia", "WVU"], 126: ["Western Kentucky", "WKU"], 127: ["Western Michigan", "WMU"], 128: ["Wisconsin"], 129: ["Wyoming"], 
             130: ["James Madison", "JMU"], 131: ["Jacksonville State", "Jacksonville St"], 132: ["Sam Houston State", "Sam Houston St", "SHSU", "Sam Houston"]}


date_dict = {
   1: (datetime.date(2024, 8, 24), datetime.date(2024, 8, 28)),
   2: (datetime.date(2024, 8, 29), datetime.date(2024, 9, 5)),
   3: (datetime.date(2024, 9, 6), datetime.date(2024, 9, 11)),
   4: (datetime.date(2024, 9, 12), datetime.date(2024, 9, 18)),
   5: (datetime.date(2024, 9, 19), datetime.date(2024, 9, 25)),
   6: (datetime.date(2024, 9, 26), datetime.date(2024, 10, 2)),
   7: (datetime.date(2024, 10, 3), datetime.date(2024, 10, 7)),
   8: (datetime.date(2024, 10, 8), datetime.date(2024, 10, 14)),
   9: (datetime.date(2024, 10, 15), datetime.date(2024, 10, 21)),
   10: (datetime.date(2024, 10, 22), datetime.date(2024, 10, 28)),
   11: (datetime.date(2024, 10, 29), datetime.date(2024, 11, 4)),
   12: (datetime.date(2024, 11, 5), datetime.date(2024, 11, 11)),
   13: (datetime.date(2024, 11, 12), datetime.date(2024, 11, 18)),
   14: (datetime.date(2024, 11, 19), datetime.date(2024, 11, 25)),
   15: (datetime.date(2024, 11, 26), datetime.date(2024, 11, 30))
}

def getCurrentWeek():
     today = datetime.date.today()
     for k in date_dict.keys():
         if date_dict[k][0] <= today <= date_dict[k][1]:
              return k
         elif today > datetime.date(2024, 12, 14):
             return 16
     else:
         return -1
   



def getScheduleData(current_week):
   """Scrapes schedule data used to populate the matrix with pairwise wins/losses for each team, contains data up to the specified week
   Args:
      current_week (int): the current week in college football

   Returns:
      schedule_data (Pandas DataFrame): cleaned schedule data containing the winner, loser, and score for each game involving a DI-FBS team
  """
   schedule_data = pd.read_html("https://www.sports-reference.com/cfb/years/2024-schedule.html")[0]
   schedule_data = schedule_data[schedule_data["Wk"] != "Wk"] # gets rid of spacer lines sports reference uses
   schedule_data = schedule_data[["Wk", "Winner", "Pts", "Loser", "Pts.1"]]
   schedule_data["Wk"] = schedule_data["Wk"].astype(int)
   schedule_data = schedule_data[schedule_data.Wk <= current_week]
   schedule_data["Pts"] = schedule_data["Pts"].astype(int)
   schedule_data["Pts.1"] = schedule_data["Pts.1"].astype(int)
   #strip ranking for consistency
   schedule_data["Winner"] = schedule_data['Winner'].str.replace(r'\(\d+\)', '').str.strip()
   schedule_data["Loser"] = schedule_data['Loser'].str.replace(r'\(\d+\)', '').str.strip()
   return schedule_data
