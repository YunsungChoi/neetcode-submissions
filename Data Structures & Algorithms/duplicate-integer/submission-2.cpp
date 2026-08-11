class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++){
            int current = i;
            int next = current +1;
            sort(nums.begin(), nums.end());
            if (nums[current] == nums[next]){
                return true;
            }
        }
    }
};