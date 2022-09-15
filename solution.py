#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        cur_sum=0
        max_sum=-100000
        for i in range(N):
            cur_sum+=arr[i]
            max_sum=max(cur_sum,max_sum)
            if cur_sum<0:
                cur_sum=0
        return(max_sum)
