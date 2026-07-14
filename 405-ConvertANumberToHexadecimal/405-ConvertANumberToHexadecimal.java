// Last updated: 7/14/2026, 2:02:46 PM
class Solution {
    public String toHex(int num) {
        if (num == 0) return "0"; 

        int[] arr = new int[8]; 
        int i = 0;
        StringBuilder s = new StringBuilder();

        while (num != 0 && i < 8) { 
            arr[i] = num & 15; 
            num >>>= 4; 
            i++;
        }

        for (int j = i - 1; j >= 0; j--) { 
            if (arr[j] < 10) {
                s.append(arr[j]);
            } else {
                s.append((char) ('a' + (arr[j] - 10)));
            }
        }

        return s.toString(); 
    }
}
