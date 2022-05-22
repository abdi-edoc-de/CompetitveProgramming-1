func countSubstrings(s string) int {
    var n int = len(s)
    var isPalidrome func(left, right int) int = func(left, right int) int {
        var count int= 0
        for left >=0 && right < n && s[left] == s[right]{
            count++
            right++
            left--
        }
        return count
    }
    var result int = 0
    for i,_ := range s{
        result += isPalidrome(i,i)
        result += isPalidrome(i,i+1)
        
    }
    return result
}