func coinChange(coins []int, amount int) int {
    if amount == 0{
        return 0
    }
    var dfs func(x int) int;
    dp := make(map[int]int)
    for _, elm := range coins{
        dp[elm] = 1
    }
    dfs = func (val int) int {
        if _, ok := dp[val]; ok{
            return dp[val]
        }
        var value = int(^uint(0) >> 1)/2
        for _, c:= range coins{
            if c <= val{
                value = int(math.Min(float64(value), float64(1+dfs(val-c))))
            }
        }
        dp[val] = value
        return dp[val]
    }
    // inc(0)
    ans := dfs(amount)
    if ans > int(^uint(0) >> 1)/10{ return -1}
    return ans
    
}