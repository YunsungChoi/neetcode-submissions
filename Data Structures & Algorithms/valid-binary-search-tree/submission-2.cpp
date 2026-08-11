/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    bool helper(TreeNode* root, int min, int max) {
        if (root == nullptr) {
            return true;
        }

        if (root -> val >= max) {
            return false;
        }

        if (root -> val <= min) {
            return false;
        }

        return helper(root -> left, min, root -> val) && helper(root -> right, root -> val, max);
    }

public:
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        return helper(root -> left, INT_MIN, root -> val) && helper(root -> right, root -> val, INT_MAX);
    }
};
