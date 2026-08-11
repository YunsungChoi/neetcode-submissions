class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int mid = nums.size()/2;
        int right = nums.size() -1;

        while(left <= right){
            if (nums[mid] == target){
                return mid;
            }

            if (nums[mid] < target){
                left = mid + 1;
                mid = (left + right)/2;

            } else if (nums[mid] > target){
                right = mid -1;
                mid = (left + right)/2;
            }
        }
        return -1;
    }
};
