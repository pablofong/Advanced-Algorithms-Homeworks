#include <iostream>
#include <string>
#include <string_view>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<string, int>> suffixArray(const string_view &s)
{
    string t = {s.begin(), s.end()};
    t.append("$");

    auto n = t.length();

    vector<pair<string, int>> suffixes;
    for (size_t i = 0; i < n; i++)
        suffixes.emplace_back(t.substr(n - i - 1, i + 1), i);

    sort(suffixes.begin(), suffixes.end());

    vector<int> a(n);
    for (size_t i = 0; i < n; i++)
        a[i] = suffixes[i].second;

    return suffixes;
}

int main()
{
    string s = "ithenconsideredherasillylittle nuisance";
    vector<pair<string, int>>
        suffixArr = suffixArray(s);

    cout << "String: " << s << endl;
    cout << "Suffix     Position\n";
    for (const auto &pair : suffixArr)
    {
        cout << pair.first << "   " << pair.second << "\n";
    }

    return 0;
}
