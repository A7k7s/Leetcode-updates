// Last updated: 7/14/2026, 2:03:57 PM
class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length()!=t.length()) return false;
        Map<Character,Character> ms=new HashMap<>();
        Map<Character,Character> mt=new HashMap<>();
        for(int i=0;i<s.length();i++){
            char chs=s.charAt(i);
            char cht=t.charAt(i);
            if(ms.containsKey(chs)&&ms.get(chs)!=cht) return false;
            if(mt.containsKey(cht)&&mt.get(cht)!=chs) return false;
            ms.put(chs,cht);
            mt.put(cht,chs);
        }return true;
    }
}