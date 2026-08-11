class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pair;
        for (int i =0; i< position.size(); i++){
            pair.push_back({position[i], speed[i]});
        }
        sort(pair.rbegin(), pair.rend());
        
        stack<double> stk;
        for (auto& p:pair){
            stk.push((double)(target-p.first)/p.second);
            if (stk.size() >= 2){
                double cur = stk.top(); stk.pop();
                if (cur <= stk.top()){
                    //do nothing
                } 
                else stk.push(cur);
            }
        }
        return stk.size();
    }
};
