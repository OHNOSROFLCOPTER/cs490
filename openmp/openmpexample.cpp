#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <omp.h>

using namespace std;

int main() {
    std::string fileNames[4] = {"productNames.txt", "description.txt", 
                        "skuNum.txt", "quantity.txt"};
    std::string data[4][100];
    omp_set_num_threads(4);
    #pragma omp parallel
    {
        int threadID = omp_get_thread_num();
        int nThrds = omp_get_num_threads();
        for (int i = threadID; i < 4; i += nThrds) {
            std::ifstream sourceFile;
            sourceFile.open(fileNames[omp_get_thread_num()]);
            std::string fromFile;
            for (int j = 0; j < 100; j++) {
                getline (sourceFile, data[i][j]);
            }
            sourceFile.close();
        }
           /* #pragma omp parallel for {
                for (i=0; i<CSV_LEN; i++) {
                    SHOULDN'T PARALLELIZE READING A FILE
                    NEED TO READ WHOLE FILE INTO BUFFER
                    AND PARALLELIZE THE BUFFER
                } */
    }
    std::ofstream destFile;
    destFile.open("destination.csv");
    for (int j = 0; j < 100; j++) {
        for (int i = 0; i < 4; i++) {
            destFile << data[i][j] << ',';
        }
        destFile << "\n";
    }
    destFile.close();
}