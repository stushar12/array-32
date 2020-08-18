def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        correctPos = nums[i]-1 
        while ((1 <= nums[i] <= n) and (nums[i] != nums[correctPos])):
            nums[i], nums[correctPos] = nums[correctPos], nums[i]
            correctPos = nums[i]-1 
                


    for i in range(n):
        if i+1 != nums[i]:
            return i+1
    return n+1

n=int(input("Enter number of elements "))
print("Enter elements :")
arr=[]
for i in range(0,n):
        z=int(input())
        arr.append(z)
a=firstMissingPositive(arr)
print("Missing number is ",a)
