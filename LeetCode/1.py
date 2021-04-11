#nums = [-1,0,3,5,9,12]
#target = 9
nums = [-1,0,3,5,9,12]
target = 2
#nums = [5]
#target = 5
#nums = [2, 5]
#target = 5
address = "1.1.1.1"
def defangIPaddr(address: str) -> str:
    li = list(map(str, address.split('.')))
    answer = ""
    answer.append(li[0])
    for _ in li:
        answer.append("[.]")
        answer.append(_)
    return answer

print(defangIPaddr(nums,target))
