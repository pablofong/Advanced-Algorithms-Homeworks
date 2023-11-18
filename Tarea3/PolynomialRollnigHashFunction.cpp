#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

unsigned long long calculateHash(string word) {
    int p = 31;
    int m = 1e9 + 9;

    unsigned long long hashValue = 0;
    unsigned long long p_pow = 1;

    for (char c : word) {
        hashValue = (hashValue + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }
    return hashValue;
}

bool compareWordFreq(const pair<string, int>& a, const pair<string, int>& b) {
    return a.second > b.second;
}

vector<string> topKFrequent(map<unsigned long long, pair<string, int>> mapWords, int k) {
    vector<string> answer;
    vector<pair<string, int>> wordFreqPairs;

    for (const auto& entry : mapWords) {
        wordFreqPairs.push_back({entry.second.first, entry.second.second});
    }

    sort(wordFreqPairs.begin(), wordFreqPairs.end(), compareWordFreq);

    for (int i = 0; i < k; ++i) {
        answer.push_back(wordFreqPairs[i].first);
    }

    return answer;
}


int main() {
    ifstream archivo("story.txt");
    if (!archivo) {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    map<unsigned long long, pair<string, int>> mapWords;

    string word;

    while (archivo >> word) {
        unsigned long long hashValue = calculateHash(word);
        if (mapWords.find(hashValue) != mapWords.end()) {
            mapWords[hashValue].second++;
        } else {
            mapWords[hashValue] = {word, 1};
        }
    }

    archivo.close();

    vector<string> answer = topKFrequent(mapWords, 20);

    cout << "Top 20 frequent words with Polynomial Rolling Hash Function:" << endl;
    for (const string& word : answer) {
        cout << word << endl;
    }

    return 0;
}
