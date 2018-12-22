#!/usr/bin/python
#!coding:utf-8
import gtk
import sys
class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("发现可用更新")
        self.set_size_request(500, 350)
        self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_resizable(False)

        table = gtk.Table(8, 4, False)
        table.set_col_spacings(3)

        title = gtk.Label("Windows")
        title.set_markup("<b>"+("为了确保您能有更好的使用体验，我们强烈建议您更新到最新版本")+"</b>")
	
	scrolledWindow = gtk.ScrolledWindow()
        scrolledWindow.set_shadow_type(gtk.SHADOW_IN)
        scrolledWindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        treeview = gtk.TreeView()
        column1 = gtk.TreeViewColumn("", gtk.CellRendererText(), text=0)
        column1.set_sort_column_id(0)
        column1.set_resizable(True)
        treeview.append_column(column1)
        treeview.set_headers_clickable(False)
        treeview.set_reorderable(False)
        treeview.set_headers_visible(False)
        model = gtk.TreeStore(str)
        with open(r'/usr/lib/linuxmint/mintUpdate/mintUpdate.py','r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n')
                iter = model.insert_before(None,None)
                model.set_value(iter,0,line)
        treeview.set_model(model)
        treeview.show()
        scrolledWindow.add(treeview)	

        try:
           self.icon = gtk.gdk.pixbuf_new_from_file("warning.png")
        except Exception, e:
            print e.message
       
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 3)
        halign1 = gtk.Alignment(0,0,0,1)
        halign1.add(title)
        vbox.pack_start(scrolledWindow)
        ok = gtk.Button("现在更新")
        close = gtk.Button("稍后更新")
        hbox.add(ok)
        hbox.add(close)
        halign = gtk.Alignment(1,0,0,0)
        halign.add(hbox)
        ok.set_size_request(20,20)
        vbox.pack_end(halign,False,False,0)
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
    def hello(self):
        print "Hello, World!"

PyApp()
gtk.main()
