/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    let set = new Set();
    
    for (let char of sentence.toLowerCase()) {
        if (char >= 'a' && char <= 'z') {
            set.add(char);
        }
    }
    
    return set.size === 26;
};