/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        inorder(root);
        return result;
    }
private:
    vector<int> result;
    int maxCount = 0, currentVal, tempCount = 0;
    void inorder(TreeNode* root) {
        if (root == NULL) return;
        inorder(root->left);
        tempCount++;
        if (root->val != currentVal) {
            currentVal = root->val;
            tempCount = 1;
        }
        if (tempCount > maxCount) {
            maxCount = tempCount;
            result.clear();
            result.push_back(root->val);
        } else if (tempCount == maxCount) {
            result.push_back(root->val);
        }
        inorder(root->right);
    }
};
