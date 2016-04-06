
.. _API-vga-switcheroo-client-fb-set:

============================
vga_switcheroo_client_fb_set
============================

*man vga_switcheroo_client_fb_set(9)*

*4.6.0-rc1*

set framebuffer of a given client


Synopsis
========

.. c:function:: void vga_switcheroo_client_fb_set( struct pci_dev * pdev, struct fb_info * info )

Arguments
=========

``pdev``
    client pci device

``info``
    framebuffer


Description
===========

Set framebuffer of a given client. The console will be remapped to this on switching.
