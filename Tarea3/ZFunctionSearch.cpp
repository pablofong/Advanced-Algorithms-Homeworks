#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <cstdlib>

using namespace std;

void getZarr(string str, int Z[]);

void search(string text, string pattern, int &wordCount)
{
    string concat = pattern + "$" + text;
    int l = concat.length();

    int Z[l];
    getZarr(concat, Z);

    int wordStart = -1;

    for (int i = pattern.length() + 1; i < l && wordCount < 10000; ++i)
    {
        if (Z[i] == pattern.length())
        {
            if (wordStart == -1)
            {
                wordStart = i - pattern.length() - 1;
            }
        }
        if (concat[i] == ' ')
        {
            if (wordStart != -1)
            {
                for (int j = wordStart + 1; j < i; j++)
                {
                    cout << concat[j];
                }
                cout << " ";
                wordCount++;
                wordStart = -1;
            }
        }
    }
}

void getZarr(string str, int Z[])
{
    int n = str.length();
    int L, R, k;
    L = R = 0;
    for (int i = 1; i < n; ++i)
    {
        if (i > R)
        {
            L = R = i;
            while (R < n && str[R - L] == str[R])
                R++;
            Z[i] = R - L;
            R--;
        }
        else
        {
            k = i - L;
            if (Z[k] < R - i + 1)
                Z[i] = Z[k];

            else
            {
                L = i;
                while (R < n && str[R - L] == str[R])
                    R++;
                Z[i] = R - L;
                R--;
            }
        }
    }
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
    string text;
    int wordCount = 0;

    clock_t t0, t1;
    t0 = clock();
    while (wordCount < 10000 && getline(archivo, text))
    {
        search(text, pattern, wordCount);
    }
    t1 = clock();
    double time = static_cast<double>(t1 - t0) / CLOCKS_PER_SEC;
    cout << "Execution Time: " << time << " seconds" << endl;

    archivo.close();
    return 0;
}
