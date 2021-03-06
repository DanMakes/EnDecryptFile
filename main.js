const {app, BrowserWindow} = require('electron')

let win

function createWindow() {
  win = new BrowserWindow({
    width: 600,
    height: 450,
    title: `InCrypt (${process.env.npm_package_version})`,
    maximizable: false,
    fullscreen: false,
    resizable: false,
    frame: false
  })
  win.loadURL(`file://${__dirname}/app/index.html`)
  win.setMenu(null)

	win.on('closed', () => {
		win = null
	})
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  app.quit()
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})
