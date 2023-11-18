// José Pablo Fong Coronado A01252402

#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <ctime>
#include <random>
#include <cstdlib>
#include <set>
#include <cmath>
#include <limits>
#include <algorithm>

using namespace std;

// MERGE SORT
vector<int> merge(vector<int> &l1, vector<int> &l2)
{
    if (l1.empty())
    {
        return l2;
    }
    if (l2.empty())
    {
        return l1;
    }

    vector<int> sorted;
    int i = 0;
    int j = 0;

    while (i < l1.size() && j < l2.size())
    {
        if (l1[i] <= l2[j])
        {
            sorted.push_back(l1[i]);
            i++;
        }
        else
        {
            sorted.push_back(l2[j]);
            j++;
        }
    }

    while (i < l1.size())
    {
        sorted.push_back(l1[i]);
        i++;
    }

    while (j < l2.size())
    {
        sorted.push_back(l2[j]);
        j++;
    }

    return sorted;
}

vector<int> merge_sort(vector<int> &divided)
{
    if (divided.size() <= 1)
    {
        return divided;
    }

    int half = divided.size() / 2;

    vector<int> l1(divided.begin(), divided.begin() + half);
    vector<int> l2(divided.begin() + half, divided.end());

    l1 = merge_sort(l1);
    l2 = merge_sort(l2);

    return merge(l1, l2);
}

vector<int> randomVector()
{
    vector<int> input;
    int N = 100;

    srand(time(0));

    int size = rand() % 1000;
    for (int i = 0; i < size; i++)
    {
        input.push_back(rand() % N);
    }
    return input;
}

void print(vector<int> &input)
{
    for (int num : input)
    {
        cout << num << " ";
    }
    cout << endl;
}

// 8 REINAS
bool checkSquare(const vector<vector<string>> &board, int row, int col)
{
    int rows = board.size();
    int columns = board[0].size();

    for (int i = max(row - 1, 0); i <= min(row + 1, rows - 1); i++)
    {
        for (int j = max(col - 1, 0); j <= min(col + 1, columns - 1); j++)
        {
            if (i != row || j != col)
            {
                if (board[i][j] == "Q")
                {
                    return false;
                }
            }
        }
    }
    return true;
}

bool checkBoard(const vector<vector<string>> &board)
{
    set<int> rowsUsed;
    set<int> columnsUsed;
    int rows = board.size();
    int columns = board[0].size();

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (board[i][j] == "Q")
            {
                if (!checkSquare(board, i, j))
                {
                    return false;
                }

                if (rowsUsed.find(i) != rowsUsed.end() || columnsUsed.find(j) != columnsUsed.end())
                {
                    return false;
                }

                rowsUsed.insert(i);
                columnsUsed.insert(j);
            }
        }
    }

    return true;
}

void printBoard(const vector<vector<string>> &board)
{
    for (int i = 0; i < board.size(); i++)
    {
        for (int j = 0; j < board[0].size(); j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// MEJOR RUTA

double calculateDistance(vector<int> &c1, vector<int> &c2)
{
    double distance = sqrt(pow(c2[0] - c1[0], 2) + pow(c2[1] - c1[1], 2));
    return distance;
}
vector<int> closestCoordinate(vector<int> &currentCoordinate, vector<vector<int>> &unvisitedCoordinates)
{
    vector<int> nextCoordinate;
    double min_distance = numeric_limits<double>::infinity();

    for (vector<int> &coordinate : unvisitedCoordinates)
    {
        double distance = calculateDistance(currentCoordinate, coordinate);
        if (distance < min_distance)
        {
            min_distance = distance;
            nextCoordinate = coordinate;
        }
    }
    return nextCoordinate;
}

vector<vector<int>> shortestRoute(vector<vector<int>> &coordinates)
{
    vector<vector<int>> route;
    vector<vector<int>> unvisitedCoordinates = coordinates;

    vector<int> currentCoordinate = unvisitedCoordinates[0];
    route.push_back(currentCoordinate);
    unvisitedCoordinates.erase(unvisitedCoordinates.begin());

    while (!unvisitedCoordinates.empty())
    {
        vector<int> nextCoordinate = closestCoordinate(currentCoordinate, unvisitedCoordinates);
        currentCoordinate = nextCoordinate;
        unvisitedCoordinates.erase(remove(unvisitedCoordinates.begin(), unvisitedCoordinates.end(), currentCoordinate), unvisitedCoordinates.end());
        route.push_back(currentCoordinate);
    }

    return route;
}

void printRoute(const vector<vector<int>> &route)
{
    for (const vector<int> &coord : route)
    {
        cout << "(" << coord[0] << ", " << coord[1] << ") , ";
    }
    cout << endl;
}

int main()
{
    // MERGE SORT
    vector<int> input = randomVector();
    // vector<int> input = {1, 5, 6, 4, 7, 8, 11, 3};
    // vector<int> input = {11, 13, 15, 9, 2, 8, 6, 20, 21, 23, 11};
    // vector<int> input = {2, 3, 1, 4, 5, 6, 1, 2, 8, 9, 10, 10};
    // vector<int> input = {5, 7, 1, 2, 3, 4, 5, 9, 11, 12, 7, 13, 0};
    // vector<int> input = {43, 17, 89, 32, 56, 12, 98, 23, 74, 5, 61, 28, 49, 82, 37, 65, 9, 51, 20, 70};
    // vector<int> input = {83, 27, 59, 36, 71, 14, 92, 48, 67, 8, 53, 31, 42, 79, 24, 62, 4, 99, 19, 76, 10, 56, 88, 17, 38, 72, 3, 64, 91, 29};

    clock_t t0, t1;
    t0 = clock();

    vector<int> answer = merge_sort(input);

    t1 = clock();
    double time = static_cast<double>(t1 - t0) / CLOCKS_PER_SEC;
    cout << "Execution Time: " << time << " seconds" << endl;

    cout << "Size: ";
    cout << input.size() << endl;

    cout << "Original Array: ";
    print(input);

    cout << "Merge Sort: ";
    print(answer);

    // 8 REINAS
    vector<vector<string>> board = {{".", ".", ".", ".", ".", ".", ".", "Q"},
                                    {".", ".", "Q", ".", ".", ".", ".", "."},
                                    {".", ".", ".", ".", ".", ".", "Q", "."},
                                    {".", "Q", ".", ".", ".", ".", ".", "."},
                                    {".", ".", ".", ".", "Q", ".", ".", "."},
                                    {"Q", ".", ".", ".", ".", ".", ".", "."},
                                    {".", ".", ".", ".", ".", "Q", ".", "."},
                                    {".", ".", ".", "Q", ".", ".", ".", "."}};

    printBoard(board);

    if (checkBoard(board))
    {
        cout << "Tablero valido" << endl;
    }
    else
    {
        cout << "Tablero no valido" << endl;
    }

    // Mejor Ruta
    vector<vector<int>> coordinates = {{20, 20}, {20, 40}, {20, 160}, {30, 120}, {40, 140}, {40, 150}, {50, 20}, {60, 40}, {60, 80}, {60, 200}, {70, 200}, {80, 150}, {90, 170}, {90, 170}, {100, 50}, {100, 40}, {100, 130}, {100, 150}, {110, 10}, {110, 70}, {120, 80}, {130, 70}, {130, 170}, {140, 140}, {140, 180}, {150, 50}, {160, 20}, {170, 100}, {180, 70}, {180, 200}, {200, 30}, {200, 70}, {200, 100}};
    // vector<vector<int>> coordinates = {{10, 10}, {30, 30},{20, 20}, {60, 60}, {40, 40}, {50, 50}};
    // vector<vector<int>> coordinates = {{1, 2}, {3, 4}, {5, 8}, {1, 0}, {4, 9}, {2, 7}, {1, 8}, {8, 5}};

    vector<vector<int>> route = shortestRoute(coordinates);
    printRoute(route);

    return 0;
}