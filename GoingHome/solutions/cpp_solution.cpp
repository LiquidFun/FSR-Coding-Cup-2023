# Author: Marian Zuska

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,m;
    string end;
    map<string, vector<int>> adj_map;
    vector<pair<pair<string,int>,vector<int>>> connections;
    int whole_day = 24*60;

    // input
    cin >> n >> m;
    cin >> end;

    for(int i = 0; i<m; i++) {
        string c1, c2;
        int duration, num_trains;

        cin >> c1 >> c2 >> duration >> num_trains;
        vector<int> times(num_trains);
        for(auto& it: times) {
            int hour, min;
            scanf("%d:%d", &hour , &min);
            it = whole_day - hour*60 - min;
        }
        sort(times.begin(), times.end());

        if(adj_map.find(c1) == adj_map.end()) {
            adj_map[c1] = vector<int>();
        }
        connections.push_back({{c2, duration}, times});
        adj_map[c1].push_back(connections.size()-1);
    }

    set<string> visited;

    // solution
    int time_finished = -1;
    priority_queue<pair<int, string>> q;
    q.push({whole_day, "rostock"});

    while(!q.empty()) {
        auto cur = q.top();
        q.pop();

        int time = cur.first;
        string city = cur.second;

        if(city == end) {
            time_finished = whole_day - time;
            break;
        }

        if(visited.find(city) != visited.end()) continue;
        visited.insert(city);

        for(int connection_id : adj_map[city]) {
            auto connection = connections[connection_id];
            string to = connection.first.first;
            int duration = connection.first.second;
            vector<int> times = connection.second;
            auto found = upper_bound(times.begin(), times.end(), time);
            found--;
            if(*found <= time) {
                q.push({*found - duration, to});
            }
        }
    }
    int hours = time_finished/60;
    int mins = time_finished - hours*60;
    printf("%02d:%02d\n", hours, mins);

    return 0;
}
