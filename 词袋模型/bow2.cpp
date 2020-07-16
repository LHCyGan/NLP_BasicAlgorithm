#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;


vector<string> split(const string &str, const string &pattern)
{
    vector<string> res;
    if(str == "")
        return res;
    //在字符串末尾也加入分隔符，方便截取最后一段
    string strs = str + pattern;
    size_t pos = strs.find(pattern);

    while(pos != strs.npos)
    {
        string temp = strs.substr(0, pos);
        res.push_back(temp);
        //去掉已分割的字符串,在剩下的字符串中进行分割
        strs = strs.substr(pos+1, strs.size());
        pos = strs.find(pattern);
    }

    return res;
}


int main()
{
    string sentence = "Bob likes to play basketball, Jim likes too. to";
    string dlim = " ";
    vector<string> p = split(sentence, dlim);
    for(int i=0;i<p.size();i++){
        cout<< p[i] << endl;
    }
    map<string, int> str2num;
    for(int i=0;i<p.size();i++){
        if(str2num.count(p[i]) == 0)
            str2num[p[i]] = 1;
        else
            str2num[p[i]] += 1;
    }
    // map<string, int>::iterator iter;
    // for(iter = str2num.begin();iter < str2num.end();iter++){
    //     cout<<iter->first<<": "<<iter->second<<endl;
    // }
    // cout<<endl;
    for(auto &v : str2num)
        cout<<v.first<<": "<<v.second<<endl;

    return 0;
}