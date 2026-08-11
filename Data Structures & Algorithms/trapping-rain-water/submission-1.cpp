class Solution {
public:
    int trap(vector<int>& height) {
        // Time: O(n)
        // Space: O(1)

        if (height.size() <= 1) {
            return 0;
        }

        // Processing: find the shorter side on both of left and right, and compute the value then add them up to res

        int res = 0;
        int left = 0, right = height.size() - 1;
        int leftValue = height[left], rightValue = height[right];

        while (left < right) {
            if (leftValue < rightValue) {
                left++;
                leftValue = max(leftValue, height[left]);
                res += leftValue - height[left];
            } else {
                right--;
                rightValue = max(rightValue, height[right]);
                res += rightValue - height[right];
            }
        }

        return res;
    }
};
