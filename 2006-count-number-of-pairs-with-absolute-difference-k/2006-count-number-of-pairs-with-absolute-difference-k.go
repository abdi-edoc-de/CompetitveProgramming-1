func countKDifference(nums []int, k int) int {
    dict, count := make(map[int]int), 0
    for _, num := range nums{
        _,ok1 := dict[num-k]
        _, ok2 := dict[num+k]
        if _, ok := dict[num]; !ok{
            dict[num] = 0
        }
        if  ok1{
            count = count + dict[num-k]
        }
        if  ok2{
            count = count + dict[num+k]
        }
        dict[num]++
        
        
    }
    return count
}