import sys

N = int(sys.stdin.readline())

win = 0
start_time = 0
team_one = 0
team_two = 0
lead = 'N'

for _ in range(N) :
    team, time = sys.stdin.readline().split()
    
    if team == '1' : win += 1
    else : win-= 1
    
    m, s = map(int, time.split(':'))
    t = m + s/60
    if win == 0 : 
        if lead == '1' :
            team_one += t - start_time
            lead = 'N'
        elif lead == '2' :
            team_two += t - start_time
            lead = 'N'
            
    elif lead == 'N' :
        if win > 0 :
            lead = '1'
            start_time = t
        else :
            lead = '2'
            start_time = t
            
if win != 0 :
    if lead == '1' :
        team_one += 48 - start_time
    else :
        team_two += 48 - start_time

h_one = str(int(team_one // 1)).rjust(2,'0')
m_one = str(int(round((team_one % 1) * 60))).rjust(2,'0')
h_two = str(int(team_two // 1)).rjust(2,'0')
m_two = str(int(round((team_two % 1) * 60))).rjust(2,'0')

print(h_one,':',m_one , sep='')
print(h_two,':',m_two , sep='')