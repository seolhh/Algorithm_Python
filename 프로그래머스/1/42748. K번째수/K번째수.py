def solution(array, commands):
    answer = []
    for t in range(len(commands)):
        i = commands[t][0]-1
        j = commands[t][1]-1
        k = commands[t][2]-1
        
        new_array=array[i:j+1]
        ans = sorted(new_array)
        
        answer.append(ans[k])
    return answer