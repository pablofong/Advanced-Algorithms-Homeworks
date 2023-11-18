#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;
string Manacher(string S) {
  int i;
  string T = "";
  for (i = 0; i < S.length(); i++) {
    T += "|";
    T += S[i];
  }
  T += "|";
  int n = T.length();
  vector<int> L(n, 0);
  int center = 0;
  int right = 0;
  int maxPalindrome = 0;
  int centerIdx = 0;
  for (i = 1; i < n - 1; i++) {
    int iMirror = (2 * center) - i;
    if (right > i)
      L[i] = min(right - i, L[iMirror]);
    while ((i - 1 - L[i] >= 0) && (i + 1 + L[i] < n) && (T[i + 1 + L[i]] == T[i - 1 - L[i]])) {
      L[i]++;
    }

    if (i + L[i] > right) {
      center = i;
      right = i + L[i];
    }
    
    if (L[i] > maxPalindrome) {
      maxPalindrome = L[i];
      centerIdx = i;
    }
  }
  
  int startIdx = (centerIdx - maxPalindrome) / 2;
  string longestPalindrome = S.substr(startIdx, maxPalindrome);
  return longestPalindrome;
}


int main()
{
string filename = "story.txt";

  ifstream inputFile(filename);
  if (!inputFile.is_open()) {
    cerr << "No se pudo abrir el archivo " << filename << endl;
    return 1;
  }

  string line;
  string content;

  while (getline(inputFile, line)) {
    content += line;
  }

  inputFile.close();
  string result = Manacher(content);
  cout << "Longest Palindrome: " << result << endl;
  return 0;
}
