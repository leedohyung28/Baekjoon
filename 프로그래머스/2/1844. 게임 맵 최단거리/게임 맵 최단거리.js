function solution(maps) {
    const m = maps.length;
    const n = maps[0].length;
    var vis = Array.from({length: m}, () => Array(n).fill(n*m));
    
    const dx = [0,1,-1,0];
    const dy = [1,0,0,-1];
    var dfs = [];
    dfs.push([0,0]);
    vis[0][0] = 1;
    var new_dfs = [];
    
    while (dfs.length > 0) {        
        const v = dfs.pop();
        const x = v[0];
        const y = v[1];
        const bf = vis[y][x];
        
        for (var i=0; i<4; i++) {
            var nx = dx[i] + x;
            var ny = dy[i] + y;
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[ny][nx] == 1 && vis[ny][nx]== n*m) {
                if (ny == m-1 && nx == n-1) {
                    return bf + 1;
                }
                new_dfs.push([nx, ny]);
                vis[ny][nx] = bf + 1;   
            }
        }
        if (dfs.length == 0) {
            dfs = [...new_dfs];
            new_dfs = [];
        }            
    }
    
    return -1;
}