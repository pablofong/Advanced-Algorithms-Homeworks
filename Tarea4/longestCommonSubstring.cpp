#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
#include <vector>

using namespace std;

// REFERENCE
// https://www.geeksforgeeks.org/longest-common-substring-dp-29/
vector<string> LCSubStr(char *X, char *Y, int m, int n)
{
    int LCSuff[m + 1][n + 1];
    int result = 0;
    vector<string> longestSubstring = {};
    int endIndex = 0;
    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (i == 0 || j == 0)
                LCSuff[i][j] = 0;

            else if (X[i - 1] == Y[j - 1])
            {
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1;
                if (LCSuff[i][j] > result)
                {
                    result = LCSuff[i][j];
                    endIndex = i - 1;
                }
            }
            else
                LCSuff[i][j] = 0;
        }
    }
    if (result > 0)
    {
        for (int i = endIndex - result + 1; i <= endIndex; i++)
        {
            longestSubstring.push_back(string(1, X[i]));
        }
    }
    return longestSubstring;
}

char* readFileToCharArray(const char* fileName, int& fileSize)
{
    ifstream file(fileName, ios::in);
    if (!file)
    {
        cerr << "Error opening file: " << fileName << endl;
        return nullptr;
    }
    file.seekg(0, ios::end);
    fileSize = file.tellg();
    file.seekg(0, ios::beg);

    char* message = new char[fileSize + 1]; // +1 for null-terminator

    file.read(message, fileSize);
    message[fileSize] = '\0'; // Null-terminate the string
    file.close();
    return message;
}

int main()
{
    const char* fileName = "story.txt";
    int fileSize;
    char* X = readFileToCharArray(fileName, fileSize);
    
    const char* fileName2 = "comparador.txt";
    int fileSize2;
    char* Y = readFileToCharArray(fileName2, fileSize2);
    
    
    int m = strlen(X);
    int n = strlen(Y);
    vector<string> longestSubstrings = LCSubStr(X, Y, m, n);

    if (!longestSubstrings.empty())
    {
        int z = longestSubstrings.size();
        cout << "Length of Longest Common Substring: "<<z << endl;
        cout << "Longest Common Substring: ";
        for (string subStr : longestSubstrings)
        {
            cout << subStr;
        }
        cout << endl;
    }
    else
    {
        cout << "No common substring found." << endl;
    }

    return 0;
}