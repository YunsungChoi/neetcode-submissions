class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> group;
        for (int num: nums){
            group[num]++;
        }
        vector<pair<int,int>> result;
        for (auto& ele: group){
            result.push_back(ele);
        }
        sort(result.begin(), result.end(), 
        [&](pair<int, int> p1, pair<int, int> p2){
            return p1.second > p2.second;});// lambda function
        
        vector<int> solution;
        for (int i = 0; i < k; i++){
            solution.push_back(result[i].first); 
        }
        return solution;

    }
};
