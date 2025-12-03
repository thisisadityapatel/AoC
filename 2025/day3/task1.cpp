#include <chrono>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <stdexcept>

std::vector<std::string> input_parser(const std::string& filename) {
    std::vector<std::string> banks;
    std::ifstream file(filename);
    if (!file) {
        throw std::runtime_error("Failed to open file.");
    }
    std::string line;
    while (std::getline(file, line)) {
        banks.push_back(line);
    }
    return banks;
}

int max_jolt(const std::string& bank) {
    if (bank.empty()) return 0;

    char max_left_val = bank[0];
    int max_left_idx = 0;

    for (size_t i = 1; i < bank.size() - 1; i++) {
        if (bank[i] > max_left_val) {
            max_left_val = bank[i];
            max_left_idx = i;
        }
    }

    size_t j = max_left_idx + 1;
    char max_right_val = bank[j];

    for (size_t i = j; i < bank.size(); i++) {
        if (bank[i] > max_right_val) {
            max_right_val = bank[i];
        }
    }

    return ((max_left_val - '0') * 10) + (max_right_val - '0');
}

int solve(const std::vector<std::string>& banks) {
    int total = 0;
    for (const auto& bank : banks) {
        total += max_jolt(bank);
    }
    return total;
}

int main() {
    try {
        auto start_time = std::chrono::high_resolution_clock::now();
        std::vector<std::string> banks = input_parser("data.txt");
        int result = solve(banks);
        auto end_time = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed = end_time - start_time;
        std::cout << result << std::endl;
        printf("Execution time: %.6f seconds\n", elapsed.count());
    }
    catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}
