#!/bin/sh

sudo gnuplot random_write_iops_conf.gp
sudo gnuplot sequential_write_iops_conf.gp
sudo gnuplot random_read_iops_conf.gp
sudo gnuplot sequential_read_iops_conf.gp
sudo gnuplot random_write_waf_conf.gp
sudo gnuplot sequential_write_waf_conf.gp


