// TODO: Add logic here to enable/disable shortcuts temporarily




const { app, BrowserWindow, Tray, Menu } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let pyProc = null;
let tray = null;
let win = null;



function startPythonScript() {
  const scriptPath = 'C:\\Users\\Void\\Google_Drive\\QuickOpen\\python\\main.py';
  console.log(`Starting Python script: ${scriptPath}`);
  
  pyProc = spawn('python', [scriptPath]);

  pyProc.stdout.on('data', (data) => {
    console.log(`Python stdout: ${data.toString()}`);
  });
  
  pyProc.stderr.on('data', (data) => {
    console.error(`Python stderr: ${data.toString()}`);
  });
  
  pyProc.unref();
}


function createWindow() {
  win = new BrowserWindow({
    width: 800,
    height: 600,
  title: 'Quick Open GUI',
  icon: path.join(__dirname, 'icon.png'),
  show: true, // Start hidden
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });
  
  win.loadFile('webUI/index.html');
  
  win.on('closed', () => {
    win = null;
  });
}


function createTray() {
  tray = new Tray(path.join(__dirname, 'icon.png'));
  
  const contextMenu = Menu.buildFromTemplate([
      {
        label: 'Open Quick Open',
        click: () => {
            if (win) {
              win.show();
            } 
      else {
              createWindow();
            }
          }
      },
      {
        label: 'Quit',
        click: () => {
          if (pyProc) {
            pyProc.kill();
          }
          app.quit();
        }
      }
  ]);
  
  tray.setToolTip('Quick Open GUI');
  tray.setContextMenu(contextMenu);
  
  tray.on('click', () => {
    tray.popUpContextMenu();
    }
  );
} 


// Main entry point for the Quick Open GUI application

console.log('Starting Quick Open GUI...');
app.whenReady().then(() => 
  {
    console.log('App is ready');
    
    startPythonScript();
    console.log('Python script started');
    
    createWindow();
    console.log('Browser window created');
    
    createTray();
    console.log('Tray icon created');  
    pyProc.on('data', (data) => {
      console.log('Received data from Python script:', data.toString());
    });
});
app.on('window-all-closed', (e) => {
  e.preventDefault(); 
});
