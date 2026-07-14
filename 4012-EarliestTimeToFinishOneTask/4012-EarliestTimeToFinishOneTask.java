// Last updated: 7/14/2026, 2:00:32 PM
class Solution {
    public int earliestTime(int[][] tasks) {
        int maxtime=Integer.MAX_VALUE;
        int n=tasks.length;
        int m=tasks[0].length;
        for(int i=0;i<n;i++){
            int sum=0;
            for(int j=0;j<m;j++){
                sum+=tasks[i][j];
            }
            maxtime=Math.min(maxtime,sum);
        }return maxtime;
    }
}