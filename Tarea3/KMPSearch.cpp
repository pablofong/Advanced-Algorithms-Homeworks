#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <chrono>
#include <ctime>
#include <random>
#include <cstdlib>
using namespace std;

vector<int> KMPSearch(string text, string pattern)
{
    vector<int> positions;
    int n = text.length();
    int m = pattern.length();

    vector<int> lps(m, 0);

    int j = 0;
    for (int i = 1; i < m;)
    {
        if (pattern[i] == pattern[j])
        {
            lps[i] = j + 1;
            j++;
            i++;
        }
        else
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                lps[i] = 0;
                i++;
            }
        }
    }

    int i = 0;
    j = 0;

    while (i < n)
    {
        if (pattern[j] == text[i])
        {
            j++;
            i++;
        }

        if (j == m)
        {
            positions.push_back(i - j);
            j = lps[j - 1];
        }
        else if (i < n && pattern[j] != text[i])
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                i++;
            }
        }
    }

    return positions;
}

int main()
{
    ifstream archivo("story.txt");
    if (!archivo)
    {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    string pattern = "the";
    string linea;

    int wordsFound = 0;
    clock_t t0, t1;
    t0 = clock();
    while (getline(archivo, linea))
    {
        stringstream ss(linea);
        string word;

        while (ss >> word)
        {
            if (KMPSearch(word, pattern).size() > 0)
            {
                cout << word << " ";
                wordsFound++;

                if (wordsFound >= 50)
                {
                    break;
                }
            }
        }

        if (wordsFound >= 50)
        {
            break;
        }
    }
    t1 = clock();
    double time = static_cast<double>(t1 - t0) / CLOCKS_PER_SEC;
    cout << "Execution Time: " << time << " seconds" << endl;

    archivo.close();

    return 0;
}