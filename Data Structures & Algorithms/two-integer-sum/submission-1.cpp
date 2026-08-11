class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> result;
        for (int i=0; i<nums.size(); i++){
            int diff = target - nums[i];
            if (result.count(diff)){
                return {result[diff], i};
            }
            result[nums[i]] = i;
        }
        //return {};
    }
};
