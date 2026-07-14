// Last updated: 7/14/2026, 2:05:34 PM
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String,List<String>> hash=new HashMap<>();
        for(String s:strs){
            char[] x=s.toCharArray();
            Arrays.sort(x);
            String key=new String(x);
            if(!hash.containsKey(key)){
                hash.put(key, new ArrayList<>());
            }hash.get(key).add(s);
        }
        return new ArrayList<>(hash.values());
    }
}