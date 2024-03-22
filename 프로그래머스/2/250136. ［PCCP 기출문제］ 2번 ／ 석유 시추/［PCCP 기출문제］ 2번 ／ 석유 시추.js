function solution(land) {
    var answer = 0;
    const W = land[0].length;
    const H = land.length;
    
    var vis = Array.from(Array(H), () => Array(W).fill(0))
    var vis_num = 1;
    var vis_dict = {};
    
    for (var x = 0; x < W; x++) {
        var oil = 0;
        var oil_vis = [];
        
        for (var y = 0; y < H; y++) {
            if (land[y][x]==1 && vis[y][x]==0) {
                var cnt = search(land, vis_num, vis, W, H, [[x,y]]);
                if (cnt==0) cnt += 1;
                vis_dict[vis_num] = cnt;
                oil += cnt;
                oil_vis.push(vis_num);
                vis_num += 1;
            }
            else if (vis[y][x] != 0 && oil_vis.includes(vis[y][x]) == false) {
                oil += vis_dict[vis[y][x]];
                oil_vis.push(vis[y][x])
            }
        }
        
        answer = Math.max(oil, answer);
    }
    
    return answer;
}

function search(land, vis_num, vis, W, H, arr) {
    var cnt = 0;
    const dx = [-1,0,1,0];
    const dy = [0,-1,0,1];
    
    while (arr.length > 0) {
        let [x, y] = arr.shift();
        vis[y][x] = vis_num;
        cnt += 1;

        for (var i = 0; i < 4; i++) {
            var nx = x + dx[i];
            var ny = y + dy[i];

            if (0<=nx&&nx<W&&0<=ny&&ny<H&&vis[ny][nx]==0&&land[ny][nx]==1) {
                vis[ny][nx] = vis_num
                arr.push([nx, ny])
            }
        }
    }
    return cnt
}