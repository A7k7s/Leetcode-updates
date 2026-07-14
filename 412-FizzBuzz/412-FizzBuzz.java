// Last updated: 7/14/2026, 2:02:44 PM
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> l= new ArrayList<>();
        for(int i=1;i<n+1;i++){
            if(i%3==0 && i%5==0){
                l.add("FizzBuzz");
            }else if(i%3==0){
                l.add("Fizz");
            }else if(i%5==0){
                l.add("Buzz");
            }else{
                l.add(String.valueOf(i));
            }
        }return l;
    }
}