#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <chrono>

std::vector<std::string> parsefile(std::string filename){
    std::ifstream file(filename);
    std::vector<std::string> data;
    std::string line;
    while (std::getline(file, line)){
        data.push_back(line);
    }
    return data;
}

int solve(const std::vector<std::string>& data){
    int counter = 0;
    int position = 50;
    for(const std::string& input : data){
        char direction = input[0];
        int value = std::stoi(input.substr(1));
        if(direction == 'L'){
            position = (position - value) % 100;
            if(position < 0){
                position += 100;
            }
        }
        else{
            position = (position + value) % 100;
        }
        if(position == 0){
            counter += 1;
        }
    }
    return counter;
}

int main(){
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<std::string> data = parsefile("data.txt");
    int result = solve(data);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << result << std::endl;
    printf("Execution time: %.6f seconds\n", elapsed.count());
    return 0;
}
