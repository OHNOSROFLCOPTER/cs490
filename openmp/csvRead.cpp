#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main () {
    string filename, pattern = "";
    ofstream myfile;
    while (true) {
        cout << "Give the name of the file: ";
        cin >> filename;
        if (filename == "-1") return 0;
        cout << "Set the pattern: ";
        getchar();
        cin >> pattern;
        myfile.open (filename);
        getchar();
        for (int i = 0; i < 100; i++) {
            myfile << pattern << " " << to_string(i) << endl;
        }
        myfile.close();
    }

    
}