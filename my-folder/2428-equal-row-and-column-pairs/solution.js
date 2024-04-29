/**
 * @param {number[][]} grid
 * @return {number}
 */
var equalPairs = function(grid) {
    let count = 0;

    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid.length; j++) {
            if(grid[i].join(',') === grid.map(row => row[j]).join(',')) {
                count++;
            };
        }
    }

    return count;
    
};
