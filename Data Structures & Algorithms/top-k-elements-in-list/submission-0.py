class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        # 1. Count frequencies
        for n in nums:
            # If n is in counts, add 1. If not, start at 0 and add 1.
            counts[n] = counts.get(n, 0) + 1
        
        # 2. Sort the dictionary items by their values (the counts)
        # We sort the pairs (key, value) based on value (x[1])
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # 3. Extract the first k keys from those sorted pairs
        output = [item[0] for item in sorted_items[:k]]
        
        return output


    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=sorted(nums)
        topk={}
        output=[]

        count=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i-1]:
                count+=1
                topk[i]+=count

            else:
                count=0


        top_k_values = sorted(topk.values(), reverse=True)[:k]
        output = [k for i in top_k_values for k, v in topk.items() if v == i]

        return output
"""