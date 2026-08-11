class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group;
        for (int i=0; i<strs.size(); i++){
            string sortedWord = strs[i];
            sort(sortedWord.begin(), sortedWord.end());
            group[sortedWord].push_back(strs[i]);
        }
        vector<vector<string>> result;
        for(auto& [key, value]: group){
            result.push_back(value);
        }
        return result;
    }
};
