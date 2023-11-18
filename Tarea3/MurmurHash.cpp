
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <vector>
#include <cstdint>
#include <cstring>  
using namespace std;

uint32_t MurmurHash3(const void *key, size_t len, uint32_t seed)
{
    const uint32_t c1 = 0xcc9e2d51;
    const uint32_t c2 = 0x1b873593;
    const uint32_t r1 = 15;
    const uint32_t r2 = 13;
    const uint32_t m = 5;
    const uint32_t n = 0xe6546b64;

    uint32_t hash = seed;

    const int nblocks = len / 4;
    const uint32_t *blocks = static_cast<const uint32_t *>(key);

    for (int i = 0; i < nblocks; i++)
    {
        uint32_t k = blocks[i];
        k *= c1;
        k = (k << r1) | (k >> (32 - r1));
        k *= c2;

        hash ^= k;
        hash = ((hash << r2) | (hash >> (32 - r2))) * m + n;
    }

    const uint8_t *tail = static_cast<const uint8_t *>(key) + nblocks * 4;
    uint32_t k1 = 0;

    switch (len & 3)
    {
    case 3:
        k1 ^= tail[2] << 16;
    case 2:
        k1 ^= tail[1] << 8;
    case 1:
        k1 ^= tail[0];
        k1 *= c1;
        k1 = (k1 << r1) | (k1 >> (32 - r1));
        k1 *= c2;
        hash ^= k1;
    }

    hash ^= len;
    hash ^= (hash >> 16);
    hash *= 0x85ebca6b;
    hash ^= (hash >> 13);
    hash *= 0xc2b2ae35;
    hash ^= (hash >> 16);

    return hash;
}

int main() {
    ifstream inputFile("story.txt");
    if (!inputFile.is_open()) {
        cerr << "No se pudo abrir el archivo 'story.txt'" << endl;
        return 1;
    }

    unordered_map<uint32_t, pair<string, int>> wordCounts; // Store word and count as a pair
    string word;

    while (inputFile >> word) {
        uint32_t hash = MurmurHash3(word.c_str(), word.length(), 0);

        wordCounts[hash].first = word;
        wordCounts[hash].second++;
    }

    inputFile.close();

    vector<pair<string, int>> sortedWords(wordCounts.size());
    int i = 0;
    for (const auto& entry : wordCounts) {
        sortedWords[i] = entry.second;
        i++;
    }

    sort(sortedWords.begin(), sortedWords.end(),
        [](const pair<string, int>& a, const pair<string, int>& b) {
            return a.second > b.second;
        });

    int K = 20; 
    cout << "The top " << K << " frequent words with Murmur3" << endl;
    for (int i = 0; i < min(K, static_cast<int>(sortedWords.size())); i++) {
        cout << sortedWords[i].first << endl;
    }

    return 0;
}
