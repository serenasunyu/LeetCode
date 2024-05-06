/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    let l1 = [];
    let l2 = [];

    let dfs = function(root, l){
        if(root) {
            dfs(root.left, l);
            if(!root.left && !root.right) {
                l.push(root.val);
            }
            dfs(root.right, l);
        }
    }
    dfs(root1, l1);
    dfs(root2, l2);

    return JSON.stringify(l1) === JSON.stringify(l2);
};
