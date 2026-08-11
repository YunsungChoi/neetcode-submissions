class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> first_v(nums.size(), 1);
        vector<int> second_v(nums.size(), 1);
        vector<int> result;

        for (int i = nums.size()-1; i>0; i--){
            first_v[i-1] = first_v[i] * nums[i];
        }
        for (int j = 1; j < nums.size(); j++){
            second_v[j] = second_v[j-1] * nums[j-1];
        }
        for (int k = 0; k < nums.size(); k++){
            result.push_back(first_v[k] * second_v[k]);
        }
        return result;
    }
};
