const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  callPythonFunction: (functionName, params) => 
    ipcRenderer.invoke('python-function', { functionName, params })
});
