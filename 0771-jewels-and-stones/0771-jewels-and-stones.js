/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    // Your code here
    let set=new Set(),c=0;
    for(let i=0;i<jewels.length;i++){
        let ch=jewels.charAt(i);
        set.add(ch);
    }
    for(i=0;i<stones.length;i++){
        if(set.has(stones.charAt(i))){
            c++;
        }
    }
        return c;
};