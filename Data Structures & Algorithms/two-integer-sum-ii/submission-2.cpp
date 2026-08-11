class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // hash map: O(n) time/space complexity
        // unordered_map<int, int> mp;
        // for (int i=0; i< numbers.size(); i++){
        //     int temp = target - numbers[i];
        //     if (mp.count(temp)){
        //         return { mp[temp], i+1 };
        //     }
        //     mp[numbers[i]] = i+1;
        // }
        // return {};

        // 2 pointers: Time Complexity: O(n), Space: O(1)
        int l = 0;
        int r = numbers.size()-1;

        while (l <= r){
            if (numbers[l] + numbers[r] == target){
                return {l+1, r+1};
            } else if (numbers[l] + numbers[r] > target){
                r--;
            } else if (numbers[l] + numbers[r] < target){
                l++;
            }
        }
        return {};

    }
};
