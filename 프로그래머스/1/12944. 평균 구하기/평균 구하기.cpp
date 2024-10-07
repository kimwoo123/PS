#include <string>
#include <vector>

using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    for (auto a = arr.begin(); a < arr.end(); ++a) {
        answer += *a;
    }
    
    answer = answer / arr.size();
    return answer;
}