class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // A1: using hash map to track last seen *index* of a character
        // ex: zxyzxyz
        // if exist in storage, then move left to the next
        // time complexity: O(n)
        // space complexity: O(m) where m is # of unique characters in the string
        unordered_map<char, int> seen;
        int l = 0;
        int best =0;

        for (int r =0; r< s.size(); r++){
            char c = s[r];
            if(seen.count(c) && seen[c] >= l){
                l = seen[c] + 1; // not l++ ! last seen index + 1. At abcbc, when r reaches the second b, l will be 1+1 = 2
            }
            seen[c] = r;
            best = max(best, r-l+1);
            
        }
        return best;
    }
};
