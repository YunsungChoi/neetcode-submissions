class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> stk;
        vector<int> result(temperatures.size(), 0);
        stk.push(temperatures.size()-1);
        for (int i = temperatures.size()-2; i>=0; i--){
            while(!stk.empty() && temperatures[stk.top()] <= temperatures[i]){
                stk.pop();
            }
            result[i] = stk.empty() ? 0 : stk.top() - i;
            stk.push(i);
        }
        return result;
    }
};
