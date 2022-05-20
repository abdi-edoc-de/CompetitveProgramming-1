func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    if obstacleGrid[0][0] == 1 {return 0}
    for r := 0; r < len(obstacleGrid); r++{
        for c:= 0; c < len(obstacleGrid[r]); c++{
            if obstacleGrid[r][c] == 1{
                obstacleGrid[r][c] = 0
            }else if r == 0 && c == 0{
                obstacleGrid[r][c] = 1
            }else if r == 0{
                obstacleGrid[r][c] = obstacleGrid[r][c-1]
            }else if c == 0{
                obstacleGrid[r][c] = obstacleGrid[r-1][c]
            }else{
                obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
            }
        }
    }
    return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
}
