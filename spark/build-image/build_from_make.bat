@echo off
setlocal enabledelayedexpansion

set TAG=3.3.0-hadoop3.3

:build
set NAME=%1
set IMAGE=bde2020/spark-%NAME%:%TAG%
if "%2"=="" (
    set DIR=.\spark\build-image\%NAME%
) else (
    set DIR=%2
)
echo -------------------------- building %IMAGE% in %DIR%
cd %DIR%
docker build -t %IMAGE% .
cd - >nul
goto :eof

if "%~1"=="" (
    call :build base
    call :build master
    call :build worker
::    call :build history-server
::    call :build submit
::    call :build maven-template template\maven
::    call :build sbt-template template\sbt
::    call :build python-template template\python
::    call :build python-example examples\python
) else (
    call :build %1 %2
)
endlocal
