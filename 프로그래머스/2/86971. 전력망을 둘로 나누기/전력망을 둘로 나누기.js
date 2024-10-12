function solution(n, wires) {
    var answer = n;
    const l = wires.length;
    var con = Array.from({length: n}, () => Array(n).fill(false));
    
    for (const w of wires) {
        con[w[0]-1][w[1]-1] = true;
        con[w[1]-1][w[0]-1] = true;
    }
    
    var n_con = [];
    
    for (var i=0; i<l; i++) {
        n_con = [...con];
        var vis = Array(n).fill(false);
        const a = wires[i][0] - 1;
        const b = wires[i][1] - 1;
        con[a][b] = false;
        con[b][a] = false;
        
        var first = [0];
        var n_first = 1;
        vis[0] = true;
        while (first.length > 0) {
            const v = first.pop();
            for (var k=0; k<n; k++) {
                if (con[v][k] && !vis[k]) {
                    vis[k] = true;
                    first.push(k);
                    n_first += 1;
                }
            }
        }
        if (n_first * 2 == n) {
            return 0;
        }
        answer = Math.min(answer, Math.abs(n-n_first*2));
        con[a][b] = true;
        con[b][a] = true;
    }
    
    return answer;
}