#!/usr/bin/python

import gtk

label = gtk.Label("Nice Label")

dialog = gtk.Dialog("My Dialog", None, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, 
                    (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT, gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
dialog.vbox.pack_start(label)
label.show()
checkbox = gtk.CheckButton("Useless ChecBox")
dialog.action_area.pack_end(checkbox)
checkbox.show()

response = dialog.run()
dialog.destroy()
