# Last updated: 7/14/2026, 2:02:03 PM
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mini = len(list1) + len(list2)  
        result = []
        for i in list1:
            if i in list2:
                current_sum = list1.index(i) + list2.index(i)
                if current_sum < mini:
                    mini = current_sum
                    result = [i]  
                elif current_sum == mini:
                    result.append(i)  
        return result

                
        
        