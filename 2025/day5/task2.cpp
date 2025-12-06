#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>

struct Range{
    long long start;
    long long end;
};

std::pair<std::vector<Range>, std::vector<long>> input_parser(std::string filename){
    std::ifstream file{std::string(filename)};
    std::vector<Range> ranges;
    std::vector<long> ids;

    bool readRange = true;
    std::string line;
    while (std::getline(file, line)) {
        if(line.empty()){
            readRange = false;
            continue;
        }
        if(readRange){
            int start, end;
            Range range;
            range.start = std::stoll(line.substr(0, line.find("-")));;
            range.end = std::stoll(line.substr(line.find("-")+1, line.size()));;
            ranges.push_back(range);
        }
        else{
            ids.push_back(std::stoll(line));
        }
    }
    return {ranges, ids};
}


std::vector<Range> resolve_ranges(std::vector<Range> ranges){
    std::sort(ranges.begin(), ranges.end(), [](Range& a, Range& b){
        return a.start < b.start;
    });

    std::vector<Range> new_ranges;
    for(int i = 0; i < ranges.size(); i++){
        if(new_ranges.size() == 0){
            new_ranges.push_back(ranges[i]);
            continue;
        }
        Range& prev = new_ranges.back();
        if(ranges[i].start > prev.end){
            new_ranges.push_back(ranges[i]);
        }
        else{
            prev.end = std::max(ranges[i].end, prev.end);
        }
    }
    return new_ranges;
}

int count_range(std::vector<Range> ranges){
    int count = 0;
    for(Range& range: ranges){
        count += range.end - range.start + 1;
    }
    return count;
}


int main(){
    auto result = input_parser("data.txt");
    auto& ranges = result.first;
    auto& ids    = result.second;
    std::vector<Range> new_ranges = resolve_ranges(result.first);
    int count = count_range(new_ranges);
    std::cout << count << std::endl;
    return 0;
}
