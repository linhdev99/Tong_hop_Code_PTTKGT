// Example program
#include <iostream>
#include <string>
using namespace std;

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
    // win = SplitChocolate(arr);
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
