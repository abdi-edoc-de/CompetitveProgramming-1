func twoSum(nums []int, target int) []int {
    
    dict := make(map[int]int)
    
    for index, num := range nums{
        if val, ok := dict[target-num]; ok{
            return []int{val, index}
        }
        dict[num] = index
        
    }
    return []int{}
}
