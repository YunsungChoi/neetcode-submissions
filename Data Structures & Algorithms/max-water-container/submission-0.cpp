class Solution {
public:
    int maxArea(vector<int>& heights) {
        int resultArea =0;
        //A1:  brute force solution 
        for( int i =0; i < heights.size()-1; i++){
            for (int j = heights.size()-1; j>i; j--){
                int area = (j-i) * min(heights[i], heights[j]);
                if (resultArea < area){
                    resultArea = area;
                }
            }
        }
        return resultArea;

        //A2: 
        
    }
};
