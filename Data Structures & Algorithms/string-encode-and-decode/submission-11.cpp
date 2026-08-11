class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";
        for (string& str: strs){
            encoded_string += str + 'Q';
        } 
        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> v;
        string word = "";

        for(char c: s) {
            if(c == 'Q') {
                v.push_back(word);
                word = "";
            } else {
                word += c;
            }
        }
        return v;
    }
};
