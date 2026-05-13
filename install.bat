@echo off
echo Creating command wrapper...
echo @echo off > TasksCLI.bat
echo python "%%~dp0TasksCLI.py" %%* >> TasksCLI.bat
echo.
echo SUCCESS: 'TasksCLI.bat' created. 
echo IMPORTANT: Add this folder (%cd%) to your System PATH to use 'tasks' anywhere.
pause
