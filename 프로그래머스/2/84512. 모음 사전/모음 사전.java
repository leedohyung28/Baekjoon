class Solution {
    public int solution(String word) {
        int answer = 0;
        
        String alpha = "AEIOU";
        int[] hun = {781, 156, 31, 6, 1};
        
        for (int i=0; i<word.length(); i++) {
            answer += 1;
            char c = word.charAt(i);
            int aIdx = alpha.indexOf(c);
            int hunNum = hun[i];
            answer += aIdx * hunNum;
        }
        
        return answer;
    }
}