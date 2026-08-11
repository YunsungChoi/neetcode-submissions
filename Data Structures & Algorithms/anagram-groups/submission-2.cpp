class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> tmp;
        vector<vector<string>> result;

        for (const string& s: strs){ 
            string sortedW = s;
            sort(sortedW.begin(), sortedW.end());
            tmp[sortedW].push_back(s);
        }

        for (auto& [key, value]: tmp){
            result.push_back(move(value));
        }
        return result;
    }
};
