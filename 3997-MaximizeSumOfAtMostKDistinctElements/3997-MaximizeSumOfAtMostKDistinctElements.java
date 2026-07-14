// Last updated: 7/14/2026, 2:00:38 PM
class Solution {
    public int[] maxKDistinct(int[] nums, int k) {
        Arrays.sort(nums);
        Set<Integer>s=new HashSet<>();
        for(int n:nums){
            s.add(n);
        }
        List<Integer>l=new ArrayList<>(s);
        l.sort(Collections.reverseOrder());
        int size=Math.min(l.size(),k);
        int []arr=new int [size];
        for(int m=0;m<size;m++){
            arr[m]=l.get(m);
        }return arr;
    }
}