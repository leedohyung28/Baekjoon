import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);
        int cl = citations.length;
        
        if (cl < citations[0])
            return cl;
        
        int idx = 1;
        for (int i = citations[cl-1]; i >= citations[0]; i--) {
            // System.out.println(i);
            while (idx < cl && citations[cl-idx-1] >= i) {
                idx++;
                // System.out.printf("Hey : %d\n", idx);
            }
            if (i <= idx) {
                return i;
            }
        }
        
        return answer;
    }
}