set term png
set output "./graph/random_write_iops_graph.png"
set title "Random Write IOPS Graph"

# set xlab "x label"
# set ylab "y label"
# set yrange [0:4]

set style line 1 lc rgb "green"
set style line 2 lc rgb "red"
set style line 3 lc rgb "blue"

set boxwidth 0.5
set style fill solid 0.5

plot \
"random_write_iops_data.gp" every ::0::1 using 1:3:xtic(2) t "" w boxes ls 1, \
"random_write_iops_data.gp" every ::1::2 using 1:3:xtic(2) t "" w boxes ls 2, \
"random_write_iops_data.gp" every ::2::3 using 1:3:xtic(2) t "" w boxes ls 3


