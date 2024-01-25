#!/usr/bin/env python3
"""
The DMTools (DM Tools) GUI interface. Let's see if we can create an all-in-one
world-management-and-randomizer-type application.
"""

import wx

class DMToolMainFrame(wx.Frame):
    """
    The first and central frame brought up for the app.
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(DMToolMainFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="DMTool v0.1")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT|wx.RIGHT, 25))
        pnl.SetSizer(sizer)

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Creatool!")

    def OnPublish(self, event):
        wx.MessageBox("Churn, churn, churn....",
                      "Publishing",
                      wx.OK|wx.ICON_INFORMATION)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is the DMTools interactive application",
                      "About",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = DMToolMainFrame(None, title='DMTool v0.1')
    frm.Show()
    app.MainLoop()
