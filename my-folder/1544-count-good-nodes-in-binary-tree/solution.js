/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function(root) {
    let counter = 0;

    const dfs = (node, maxValue) => {
        if(!node) return;

        if(node.val >= maxValue) {
            counter++;
            maxValue = node.val;
        }

        dfs(node.left, maxValue);
        dfs(node.right, maxValue);
    }
    dfs(root, -Number.MAX_VALUE);
    return counter;
};
