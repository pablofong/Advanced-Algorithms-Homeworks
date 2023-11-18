// Jose Pablo Fong Coronado
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <map>
#include <ctime>

using namespace std;

// PROBLEMA DE LA VARILLA

// DYNAMIC SIZING
vector<int> randomVector()
{
    vector<int> input;
    int N = 100000;

    srand(time(0));

    int size = rand() % 1000;
    for (int i = 0; i < size; i++)
    {
        input.push_back(rand() % N);
    }
    return input;
}

map<int, int> generateRandomPrices(int numItems)
{
    map<int, int> prices;
    vector<int> randomValues = randomVector();

    for (int i = 1; i <= numItems; i++)
    {
        if (i <= randomValues.size())
        {
            prices[i] = randomValues[i - 1];
        }
        else
        {
            prices[i] = 0;
        }
    }

    return prices;
}

// map<int, int> prices{
//     {1, 1},
//     {2, 5},
//     {3, 8},
//     {4, 9},
//     {5, 10},
//     {6, 17},
//     {7, 17},
//     {8, 20},
//     {9, 24},
//     {10, 30}};

// Dynamic Programming

int bestPriceDynamicProgramming(int n, map<int, int> &prices)
{
    vector<int> dynamicPrices(n + 1, 0);
    for (int i = 1; i <= n; i++)
    {
        int max_price = 0;
        for (int j = 1; j <= min(i, static_cast<int>(prices.size())); j++)
        {
            max_price = max(max_price, prices.at(j) + dynamicPrices[i - j]);
        }
        dynamicPrices[i] = max_price;
    }
    return dynamicPrices[n];
}

// Recursive Programming

int bestPriceRecursive(int n, int max_value, map<int, int> &prices)
{
    int maxPrice = 0;
    for (int i = 1; i <= min(n, max_value); i++)
    {
        maxPrice = max(maxPrice, prices.at(i) + bestPriceRecursive(n - i, max_value, prices));
    }
    return maxPrice;
}

// Map Color Problem
// REFERENCES FOR THIS ALGORITHM ATTACHED IN THE DOCUMENT
// BACKTRACKING TO CHECK WITH NEIGHBOR COLORED
bool isSafe(map<string, vector<string>> neighbors, string v, string c, map<string, string> color)
{
    for (int i = 0; i < neighbors[v].size(); i++)
    {
        string neighbor = neighbors[v][i];
        if (color[neighbor] == c)
        {
            return false;
        }
    }
    return true;
}

// ADD COLOR AND START THE CONSECUENT VALIDATION WITH FOLLOWING PAIRS
bool graphColoringUtil(map<string, vector<string>> neighbors, vector<string> colors, map<string, string> color, string v)
{
    if (v == "")
    {
        for (pair<string, string> vertexColorPair : color)
        {
            cout << vertexColorPair.first << " is color " << vertexColorPair.second << endl;
        }
        cout << "-----------------------------" << endl;
        return true;
    }
    for (int i = 0; i < colors.size(); i++)
    {
        string c = colors[i];
        if (isSafe(neighbors, v, c, color))
        {
            color[v] = c;
            string nextVertex = "";
            for (int j = 0; j < neighbors.at(v).size(); j++)
            {
                string neighbor = neighbors.at(v)[j];
                if (color[neighbor] == "")
                {
                    nextVertex = neighbor;
                    break;
                }
            }
            if (graphColoringUtil(neighbors, colors, color, nextVertex))
            {
                color[v] = "";
            }
        }
    }
    return false;
}

// START COLORING GRAPH OVERALL
void graphColoring(map<string, vector<string>> &neighbors, vector<string> &colors)
{
    map<string, string> color;
    bool solutionExists = false;

    vector<pair<string, vector<string>>> neighborPairs(neighbors.begin(), neighbors.end());

    for (int i = 0; i < neighborPairs.size(); i++)
    {
        string v = neighborPairs[i].first;
        if (!solutionExists && color.find(v) == color.end())
        {
            if (graphColoringUtil(neighbors, colors, color, v))
            {
                solutionExists = true;
            }
        }
    }
    if (!solutionExists)
    {
        cout << "No solution exists" << endl;
    }
}


int main()
{
    int n = 13;
    int max_value = 10;
    map<int, int> prices = generateRandomPrices(10000000);

    clock_t t0, t1;
    t0 = clock();
    int result = bestPriceRecursive(n, max_value, prices);
    t1 = clock();
    double time = static_cast<double>(t1 - t0) / CLOCKS_PER_SEC;

    clock_t t2, t3;
    t2 = clock();
    int result2 = bestPriceDynamicProgramming(n, prices);
    t3 = clock();
    double time2 = static_cast<double>(t3 - t2) / CLOCKS_PER_SEC;

    cout << "Recursive Result: " << result << endl;
    cout << "Execution Time: " << time << " seconds" << endl;

    cout << "Dynamic Programming Result: " << result2 << endl;
    cout << "Execution Time: " << time2 << " seconds" << endl;

    map<string, vector<string>> neighbors;
    neighbors["Mark"] = {"Julia", "Steve"};
    neighbors["Steve"] = {"Mark", "Julia", "Amanda", "Allan", "Michelle"};
    neighbors["Allan"] = {"Steve", "Michelle"};
    neighbors["Julia"] = {"Mark", "Steve", "Amanda", "Derek", "Brian"};
    neighbors["Amanda"] = {"Steve", "Julia", "Derek", "Michelle", "Joanne"};
    neighbors["Michelle"] = {"Steve", "Allan", "Amanda", "Joanne"};
    neighbors["Derek"] = {"Julia", "Amanda", "Joanne", "Kelly", "Chris"};
    neighbors["Joanne"] = {"Michelle", "Amanda", "Derek", "Chris"};
    neighbors["Brian"] = {"Julia","Derek","Kelly",};
    neighbors["Kelly"] = {"Brian","Derek","Chris",};
    neighbors["Chris"] = {"Joanne","Derek","Kelly",};
    vector<string> colors;
    colors = {"Red", "Green", "Blue", "Gray"};
    graphColoring(neighbors, colors);
    return 0;
}
