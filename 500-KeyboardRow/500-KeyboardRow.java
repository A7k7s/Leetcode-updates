// Last updated: 7/14/2026, 2:02:21 PM

class Solution {
    public String[] findWords(String[] words) {
        List<String> s = new ArrayList<>();
        String r1 = "qwertyuiop";
        String r2 = "asdfghjkl";
        String r3 = "zxcvbnm";
        
        for (String word : words) {
            String r = word.toLowerCase();
            String l;
            char t = r.charAt(0);
            
            if (r1.contains(String.valueOf(t))) {
                l = r1;
            } else if (r2.contains(String.valueOf(t))) {
                l = r2;
            } else {
                l = r3;
            }
            
            boolean valid = true; 
            for (int i = 1; i < r.length(); i++) {
                char v = r.charAt(i);
                if (!l.contains(String.valueOf(v))) {
                    valid = false; 
                    break; 
                }
            }
            
            if (valid) {
                s.add(word);
            }
        }
        
        return s.toArray(new String[0]);
    }
}
