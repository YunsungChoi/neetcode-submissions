class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int length = s1.size();
        if (s1.size() > s2.size()) return false;

        vector<int> s1Count(26,0);
        vector<int> windowCount(26,0);

        for (char c : s1){
            s1Count[c - 'a'] +=1;
        }

        for (int i = 0; i < length; i++){
            windowCount[s2[i]-'a'] += 1;
        }

        if (s1Count == windowCount) return true;

        for (int j = length; j < s2.size(); j++){
            windowCount[s2[j] - 'a'] ++;
            windowCount[s2[j - s1.size()] - 'a'] --;

            if (s1Count == windowCount) return true;
        }

        

        return false;

    }
};
