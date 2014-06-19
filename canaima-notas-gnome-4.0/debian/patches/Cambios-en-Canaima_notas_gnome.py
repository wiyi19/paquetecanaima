Description: <short summary of the patch>
 TODO: Put a short summary on the line above and replace this paragraph
 with a longer explanation of this change. Complete the meta-information
 with other relevant fields (see below for details). To make it easier, the
 information below has been extracted from the changelog. Adjust it or drop
 it.
 .
 canaima-notas-gnome (4.0-13) stable; urgency=low
 .
   * [6e3044f] Comando lspci -nn , Todos los CheckButton True
Author: Carlos Espinoza <carlosarmikhael@gmail.com>

---
The information above should follow the Patch Tagging Guidelines, please
checkout http://dep.debian.net/deps/dep3/ to learn about the format. Here
are templates for supplementary fields that you might want to add:

Origin: <vendor|upstream|other>, <url of original patch>
Bug: <url in upstream bugtracker>
Bug-Debian: http://bugs.debian.org/<bugnumber>
Bug-Ubuntu: https://launchpad.net/bugs/<bugnumber>
Forwarded: <no|not-needed|url proving that it has been forwarded>
Reviewed-By: <name and email of someone who approved the patch>
Last-Update: <YYYY-MM-DD>

--- canaima-notas-gnome-4.0.orig/canaima_notas_gnome.py
+++ canaima-notas-gnome-4.0/canaima_notas_gnome.py
@@ -128,13 +128,13 @@ specific as possible):"))
         self.check_lsusb.set_active(True)
         self.check_ram = gtk.CheckButton("RAM/SWAP/Buffers")
         self.check_ram.set_active(True)
-        self.check_df = gtk.CheckButton(_("Disk Space"))
+        self.check_df = gtk.CheckButton(_("Espacio Discos"))
         self.check_df.set_active(True)
         self.check_cpu = gtk.CheckButton("CPU")
         self.check_cpu.set_active(True)
-        self.check_tm = gtk.CheckButton(_("Motherboard"))
+        self.check_tm = gtk.CheckButton(_("Tarjeta Madre"))
         self.check_tm.set_active(True)
-        self.check_all = gtk.CheckButton(_("Select All"))
+        self.check_all = gtk.CheckButton(_("Seleccionar todos"))
         self.check_all.connect("toggled", self.selectalldis, "Todos")
 
         self.check_all.set_active(False)
