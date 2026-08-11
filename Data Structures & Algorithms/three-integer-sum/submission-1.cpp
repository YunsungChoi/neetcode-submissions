class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;

        // Edge case
        if(nums.size() < 3) {
            return result;
        }

        int n = nums.size();
        unordered_map<int, int> mp;

        // Sort the vector from smallest to largest
        sort(nums.begin(), nums.end());

        // Iterate the vector and store the number of value 
        for(auto& num: nums) {
            mp[num]++;
        }

        // Logic: Doing as 2sum, but we find if the negative value of the 2sum is available in map, 
        // then they can group as 3sum
        for(int i = 0; i < n; i++) {
            mp[nums[i]]--;

            // If the current index carries the same value as the previous one, skip to avoid duplicate
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            for(int j = i + 1; j < n; j++) {
                mp[nums[j]]--;

                // If the current index carries the same value as the previous one, skip to avoid duplicate
                if(j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                
                int target = (nums[i] + nums[j]) * -1;
                if(mp[target] > 0) {
                    result.push_back({nums[i], nums[j], target});
                }
            }

            // Put back the occurence for the next check
            for(int j = i + 1; j < n; j++) {
                mp[nums[j]]++;
            }
        }
        
        return result;
    }
};
