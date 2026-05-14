@echo off
chcp 65001 > nul
echo 正在启动博物馆管理系统...
cd /d "%~dp0"
python app.py
pause