function solution(bandage, health, attacks) {
    const N = attacks.length
    const max_time = attacks[N-1][0];
    const max_health = health;
    
    var attacks_pointer = 0
    var successive = 0
    
    for (var i = 0; i <= max_time; i++) {
        
        if (i == attacks[attacks_pointer][0]) {
            health -= attacks[attacks_pointer][1];
            attacks_pointer += 1;
            successive = 0;
            if (health <= 0)
                return -1
            else if (attacks_pointer == N)
                return health
        }
        
        else if (health < max_health) {
            successive += 1;
            health += bandage[1];
            if (successive == bandage[0]) {
                health += bandage[2];
                successive = 0;
            }
            if (health >= max_health) {
                health = max_health;
                successive = 0;
            }
        }
        
        console.log(i, health, successive)
    }
    
    
    return health
}