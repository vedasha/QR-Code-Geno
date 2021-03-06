""" __main__.py
This file runs aotumatically when running th OS command "python py" form "Main.py"
 
Subclass of MainFrame, which is generated by wxFormBuilder."""

import wx
import UI_Base
import pyqrcode
# Implementing MainFrame
class MainFrame( UI_Base.MainFrame ):
	def __init__( self, parent ):
		UI_Base.MainFrame.__init__( self, parent )
		# Disable Maximize box.
		style = self.GetWindowStyle()
		self.SetWindowStyle(style & (~wx.MAXIMIZE_BOX))
		self.Refresh()
	
	# Handlers for MainFrame events.

	# Generates QR code and displays it.
	def GenQR( self, event ):
		text = self.txtBox.GetValue()
		code = pyqrcode.create(text)
		code.png('QR.png', scale=3)
		self.imgQR.SetBitmap(wx.Bitmap("QR.png"))
		self.Layout()

	# Exits the app.
	def Exit(self, event ):
		self.Close()
	

# Creates the main window and start the app.
app = wx.App(False) 
frame = MainFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop()
