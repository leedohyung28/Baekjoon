import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int n, int[][] edge) {
        boolean[][] con = new boolean[20001][20001];
        int[] vis = new int[n+1];
        
        for(int[] e: edge) {
            con[e[0]][e[1]] = true;
            con[e[1]][e[0]] = true;
        }
        
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        vis[1] = 1;
        int max = 0;
        int cnt = 1;
        
        while(q.size()!=0) {
            int v = q.poll();
            for(int i=1; i<n+1; i++) {
                if(con[v][i] && vis[i]==0) {
                    if (max != vis[v] + 1) {
                        max = vis[v] + 1;
                        cnt = 1;
                    } else {
                        cnt += 1;
                    }
                    vis[i] = max;
                    q.offer(i);
                }
            }
            
        }
        
        return cnt;
    }
}