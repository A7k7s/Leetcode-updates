// Last updated: 7/14/2026, 2:01:46 PM
class Solution {
    public int[][] transpose(int[][] matrix) {
        int row =matrix.length;
        int col=matrix[0].length;
        int[][]trans=new int[col][row];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                trans[j][i]=matrix[i][j];
            }
        }return trans;
    }
}