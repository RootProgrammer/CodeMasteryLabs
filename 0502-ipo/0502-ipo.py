class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = []  # heap for profits we can afford
        min_capital = [(capital_requirement, profit) for capital_requirement, profit in zip(capital, profits)]  # heap for capital requirements

        heapq.heapify(min_capital)  # create a min-heap based on capital requirements

        for _ in range(k):
            # Push all projects that can be afforded into the max_profit heap
            while min_capital and min_capital[0][0] <= w:
                capital_requirement, profit = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -profit)  # use negative to simulate max-heap in python

            if not max_profit:
                break
            
            # Pop the most profitable project
            w += -heapq.heappop(max_profit)

        return w
