import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int[][] routes) {
        int answer = 1;
        
        Arrays.sort(routes, new Comparator<int[]>() {
            
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });
        
        int standard = routes[0][1];
        
        for(int y=0; y<routes.length; y++) {
            int start = routes[y][0];
            
            if (standard < start) {
                standard = routes[y][1];
                answer += 1;
            }
        }
        
        return answer;
    }
}