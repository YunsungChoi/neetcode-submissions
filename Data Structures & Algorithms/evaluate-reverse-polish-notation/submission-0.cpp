class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        unordered_map<string, function<int(int, int)>> ops = {
            {"+", [](int a, int b){return a + b;}},
            {"-", [](int a, int b){return a - b;}},
            {"*", [](int a, int b){return a * b;}},
            {"/", [](int a, int b){return a / b;}}
        };

        for (auto& token : tokens){
            if (ops.count(token)){
                int b = stk.top(); stk.pop();
                int a = stk.top(); stk.pop();
                stk.push(ops[token](a, b));
            }else{
                stk.push(stoi(token));
            }
        }
        return stk.top();
    }
};
