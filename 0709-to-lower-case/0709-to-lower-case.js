/**
 * @param {string} s
 * @return {string}
 */
var toLowerCase = function(s) {
    let t='';
    for (let i=0;i<s.length;i++){
        let c=s[i];
        t+=c.toLowerCase();
    }
    return t;
};