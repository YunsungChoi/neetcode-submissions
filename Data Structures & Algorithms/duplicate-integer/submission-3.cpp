class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        sort(nums.begin(), nums.end());
        for (int x : nums){
            if (seen.count(x)) return true;
            seen.insert(x);
        }
        return false;
    }
};