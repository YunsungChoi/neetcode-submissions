class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        //edge case
        if (nums.size() < 3) return {};

        // just like two sum II problem
        for (int i = 0; i< nums.size()-2; i++){
            int l = i+1;
            int r = nums.size()-1;

            if (i > 0 && nums[i] == nums[i-1]) continue;

            while (l<r){
                int target = -nums[i];
                if (target == nums[l] + nums[r]){
                    result.push_back({nums[i], nums[l], nums[r]});
                    int lastL = nums[l];
                    int lastR = nums[r];
                    while (l < r && nums[l] == lastL) l++;
                    while (l < r && nums[r] == lastR) r--;
                } else if (target > nums[l] + nums[r]){
                    l++;
                }else{
                    r--;
                }
            }
        }
        return result;
    }
};
