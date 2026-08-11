class Solution {
public:
    int maxArea(vector<int>& heights) {
        int resultArea =0;
        //A1:  brute force solution 
        // time complexity: O(n^2)
        // space complexity: O(1)
        // for( int i =0; i < heights.size()-1; i++){
        //     for (int j = heights.size()-1; j>i; j--){
        //         int area = (j-i) * min(heights[i], heights[j]);
        //         if (resultArea < area){
        //             resultArea = area;
        //         }
        //     }
        // }
        // return resultArea;

        //A2: two pointer
        // time complexity: O(n) 
        // space complexity: O(1)
        int l =0;
        int r = heights.size()-1;

        while (l <r){
            int area = (r-l) * min(heights[l], heights[r]);
            resultArea = max(resultArea, area);

            if (heights[l] < heights[r]){
                l++;
            }else{
                r--;
            } 
        }
        return resultArea;
        
    }
};
