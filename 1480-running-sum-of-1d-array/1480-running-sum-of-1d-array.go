func runningSum(nums []int) []int {
    var n int = len(nums)
    result := make([]int , n)
    for i, item:= range nums{
        if i != 0{
            result[i] = item + result[i-1]
        }else{
            result[i] = item
        }
        
    }
    return result
    
}