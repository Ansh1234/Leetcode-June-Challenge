class Solution:
  
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        cost_diff = [x[0]- x[1] for x in costs]
        
        sorted_costs = [y for x,y in sorted(zip(cost_diff, costs))]
        
        length = int(len(costs)/2)
                
        total_cost = sum([x[0] for x in sorted_costs[:length]]) + sum([x[1] for x in sorted_costs[length:]])
            
        return total_cost
      
      
