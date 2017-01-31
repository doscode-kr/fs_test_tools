set term png
set output "./graph/videoserver_mbs_graph.png"
set title "Videoserver MB/S Graph"

set style line 1 lc rgb "green"
set style line 2 lc rgb "red"
set style line 3 lc rgb "blue"

set boxwidth 0.5
set style fill solid 0.5

plot \
"videoserver_mbs_data.gp" every ::0::1 using 1:3:xtic(2) t "" w boxes ls 1, \
"videoserver_mbs_data.gp" every ::1::2 using 1:3:xtic(2) t "" w boxes ls 2, \
"videoserver_mbs_data.gp" every ::2::3 using 1:3:xtic(2) t "" w boxes ls 3
