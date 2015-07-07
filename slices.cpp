
#include <vector>
#include <map>
#include <string>
#include <iostream>


using namespace std;


const int MAX_SLICES = 1000000000;


int solution(vector<int>& a) {
    size_t size = a.size();

    vector<int> accum;

    map<int, int> memo;

    int from_memo = 0;
    int zero_cells_num = 0;
    int zero_slices_num = 0;

    int sum = 0;

    for (size_t i = 0; i < size; ++i) {
        sum += a[i];

        zero_cells_num += a[i] == 0;
        zero_slices_num += sum == 0;

        if (sum && a[i]) {
            if (memo.end() != memo.find(sum)) {
                memo[sum] += 1;
            }   
            else {
                memo[sum] = 1;
            }
        }
    }

    for (auto item : memo) {
        if (item.second > 1) {
            from_memo += (item.second * item.second - item.second) / 2;
        }
    }


    zero_slices_num += 1;
    zero_slices_num = (zero_slices_num * zero_slices_num - zero_slices_num) / 2;

    if (MAX_SLICES == (zero_cells_num + zero_slices_num + from_memo))
        return -1;

    return zero_cells_num + zero_slices_num + from_memo;
}



int main(int argc, const char* argv[]) {

    int N;
    cin >> N;
   
    vector<int> vec(N, 0);
    for (int i = 0; i < N; ++i)
        cin >> vec[i];

    cout << solution(vec) << endl;

    return 0;
}
