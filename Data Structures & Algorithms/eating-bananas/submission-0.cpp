class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int result_rate;
        int left = 1;
        int max_val;

        for (auto& p : piles){
            max_val = max(p, max_val);
        }      

        int right = max_val;
        int total_time;

        while( left <= right){
            int mid = ( left + right ) / 2;
            total_time = 0;
            for (auto& p: piles){
                total_time += ceil((double)p / mid);
            }
            if (total_time <= h){
                result_rate = mid;
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return result_rate;
    }
};
