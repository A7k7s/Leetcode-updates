// Last updated: 7/14/2026, 2:02:31 PM
class Solution {
    public String frequencySort(String s) {
        Map<Character,Integer> m=new HashMap<>();
        for( char c:s.toCharArray()){
            m.put(c,m.getOrDefault(c,0)+1);
        }
        List<Map.Entry<Character, Integer>> l = new ArrayList<>(m.entrySet());
        l.sort((a,b)->b.getValue()-a.getValue());
        StringBuilder sn=new StringBuilder();
        for(Map.Entry<Character,Integer> e:l){
            char ch=e.getKey();
            int count=e.getValue();
            for(int i=0;i<count;i++){
                sn.append(ch);
            }
        }return sn.toString();
    }
}