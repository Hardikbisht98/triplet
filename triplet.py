class Solution:
	def countTriplet(self, arr, n):
	    
	    arr.sort()
	    for i in range(n,1,-1):
	        
	        
	    
	    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)
