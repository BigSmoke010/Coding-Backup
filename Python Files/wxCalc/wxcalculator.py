import wx
import math

class Frame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.panel = wx.Panel(self)
        self.numbs = []
        self.operation = 'add'
        boxsizr = wx.BoxSizer(wx.VERTICAL)
        self.numberentry = wx.TextCtrl(self.panel, size=(258, 30), style=wx.CB_READONLY)
        boxsizr.Add(self.numberentry)
        gridsizr = wx.GridSizer(6,3,1,1)
        gridsizr.AddMany([(wx.Button(self.panel,-1,'1', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'2', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'3', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'4', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'5', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'6', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'7', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'8', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'9', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel, -1, '+', size=(100, 600)), 0, wx.EXPAND),(wx.Button(self.panel,-1,'0', size=(100, 600)), 0, wx.EXPAND)])
        gridsizr.AddMany([(wx.Button(self.panel, -1, '=', size=(100, 600)), 0, wx.EXPAND), (wx.Button(self.panel, -1, 'rm', size=(100, 600)), 0, wx.EXPAND), (wx.Button(self.panel, -1, '-', size=(100, 600)), 0, wx.EXPAND), (wx.Button(self.panel, -1, '/', size=(100, 600)), 0, wx.EXPAND), (wx.Button(self.panel, -1, '*', size=(100, 600)), 0, wx.EXPAND), (wx.Button(self.panel, -1, 'sqrt', size=(100, 600)), 0, wx.EXPAND)])
        boxsizr.Add(gridsizr)
        self.panel.SetSizer(boxsizr)
        self.panel.Bind(wx.EVT_BUTTON, self.insertnum)
    def insertnum(self, event):
        pressednum = event.GetEventObject().GetLabel()
        if pressednum == '+':
            self.numbs.append(str(self.numberentry.GetValue()))
            self.numbs.append('+')
            self.operation = 'add'
            self.numberentry.Clear()
        elif pressednum == '-':
            self.numbs.append(str(self.numberentry.GetValue()))
            self.numbs.append('-')
            self.operation = 'min'
            self.numberentry.Clear()
        elif pressednum == '/':
            self.numbs.append(str(self.numberentry.GetValue()))
            self.numbs.append('/')
            self.operation = 'div'
            self.numberentry.Clear()
        elif pressednum == '*':
            self.numbs.append(str(self.numberentry.GetValue()))
            self.numbs.append('*')
            self.operation = 'mult'
            self.numberentry.Clear()
        elif pressednum == 'sqrt':
            self.numbs.append('math.sqrt('+str(self.numberentry.GetValue()+')'))
            self.numberentry.Clear()
        elif pressednum == 'rm':
            x = self.numberentry.GetValue()[:-1]
            self.numberentry.Clear()
            self.numberentry.AppendText(x)
        elif pressednum == '=':
            self.numbs.append(self.numberentry.GetValue())
            self.numberentry.Clear()
            self.numberentry.AppendText(str(eval(''.join(self.numbs))))
            self.numbs.clear()
        else:
            self.numberentry.AppendText(pressednum)
class MyApp(wx.App):
    def OnInit(self):
        self.Frame = Frame(parent=None, title='Calculator', size=(259,405))
        self.Frame.Show()

        return True

app = MyApp()
app.MainLoop()
