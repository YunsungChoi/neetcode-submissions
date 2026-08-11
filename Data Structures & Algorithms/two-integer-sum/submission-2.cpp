class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> result;
        for (int i =0; i < nums.size(); i++){
            int res = target - nums[i];
            if (result.count(res)) return {result[res], i};
            result[nums[i]] = i;
        }
               
    }
};
