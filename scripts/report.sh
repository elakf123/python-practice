#!/bin/bash

report_file="report_$(date +%Y-%m-%d).txt"
python3 log_stats.py "$1" > "$report_file"
echo "Отчёт сохранен в $report_file"
