// Author: Prashnat //
#include <bits/stdc++.h>
using namespace std;

//---------------------------Macros----------------------//

#define int long long
#define fast                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout << setprecision(12) << fixed;
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
// __builtin_ffs(x) it return least significant digit index
#define f(i, a, b) for (int i = a; i < b; i++)

//---------------------------Constants taken----------------------//

const int N = 1e5 + 1;
const int mod = 1e9 + 7;
const int inf = 2e18;

//---------------------------Formatter----------------------//

template <typename t1, typename t2>
istream &operator>>(istream &istream, pair<t1, t2> &p)
{
    return (istream >> p.first >> p.second);
}

template <typename t>
istream &operator>>(istream &istream, vector<t> &v)
{
    for (auto &it : v)
    {
        cin >> it;
    }
    return istream;
}

template <typename t1, typename t2>
ostream &operator<<(ostream &ostream, const pair<t1, t2> &p)
{
    return (ostream << p.first << " " << p.second);
}

template <typename t>
ostream &operator<<(ostream &ostream, const vector<t> &c)
{
    for (auto &it : c)
        cout << it << " ";
    return ostream;
}

//-----------------------------Code begins----------------------------------//
int32_t main(){
    vector<pair<int, int>> pq;
    pq.push_back({1, 2});
    pq.push_back({3, 2});
    for(auto [i, j] : pq){
        cout<<i<<endl;
    }

}