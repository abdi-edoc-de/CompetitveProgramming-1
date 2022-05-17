func countPairs(nums []int, k int) int {
    dict, count:= make(map[int][]int), 0
    for index, num := range nums{
        if val, ok := dict[num]; ok{
            for _, i := range val{
                if (i * index) % k == 0{
                    count++
                }
            }
        }
        dict[num] = append(dict[num],index)
    }
    return count
    
}