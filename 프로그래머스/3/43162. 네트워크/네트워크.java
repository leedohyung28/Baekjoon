import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int n, int[][] computers) {
        int len = computers.length;
        
        boolean[] vis = new boolean[len];
        
        int answer = 0;
        
        for(int i=0; i<len; i++) {
            if (!vis[i]) {
                answer += 1;
                vis[i] = true;
                Queue<Integer> q = new LinkedList<>();
                q.offer(i);
                while(q.size()!=0) {
                    int k = q.poll();
                    for (int j=0; j<len; j++) {
                        if (computers[k][j] == 1 && !vis[j]) {
                            vis[j] = true;
                            q.offer(j);
                        }
                    }
                }
            }
        }
        
        
        return answer;
    }
}