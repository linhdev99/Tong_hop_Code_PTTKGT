// Example program
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int *sort(int arr[])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = i + 1; j < 4; j++)
        {
            if (arr[i] > arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    return arr;
}
int Split(int arr[])
{
    if (arr[0] == arr[1] || arr[1] == arr[2] || arr[2] == arr[3])
    {
        return 1;
    }
    int newArr[] = {0, 0, 0, 0};
    for (int id = 0; id < 4; id++)
    {
        if (arr[id] > 0)
        {
            int temp[] = {0, 0, 0, 0};
            copy(arr, arr, temp);
            temp[id] -= 1;
            newArr[id] = -1 * Split(temp);
        }
    }
    for (int i = 0; i < 4; i++)
    {
        if (newArr[i] == 1)
        {
            return 1;
        }
    }
    return -1;
}
int SplitChocolate(int arr[4])
{
    arr = sort(arr);
    for (int i = 0; i < 4; i++)
    {
        cout << arr[i] << ", ";
    }
    cout << endl;

    if (arr[0] == arr[1] && arr[2] == arr[3])
    {
        return -1;
    }
    return Split(arr);
}
void CreateChocolate(int x, int y, int w, int h)
{
    cout << "Chocolate:" << endl;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (x == j && y == i)
            {
                cout << " X ";
            }
            else
            {
                cout << " O ";
            }
        }
        cout << "\n";
    }
}
void Game()
{
    system("CLS");
    int w, h, x, y, win, state;
    cout << "Width: ";
    cin >> w;
    cout << "Height: ";
    cin >> h;
    cout << "X: ";
    cin >> x;
    cout << "Y: ";
    cin >> y;
    int arr[] = {x, y, w - x - 1, h - y - 1};
    CreateChocolate(x, y, w, h);
    win = SplitChocolate(arr);
    cout << "-----------------" << endl;
    cout << "Player " << ((win == -1) ? 2 : 1) << " win!" << endl;
    cout << "-----------------" << endl;
    cout << "1: Start Game\n";
    cout << "2: Exit\n";
    cout << "Enter number: ";
    cin >> state;
    if (state == 1)
    {
        Game();
    }
}
int main()
{
    Game();
    return 0;
}
