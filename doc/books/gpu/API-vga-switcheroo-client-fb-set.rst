.. -*- coding: utf-8; mode: rst -*-

.. _API-vga-switcheroo-client-fb-set:

============================
vga_switcheroo_client_fb_set
============================

*man vga_switcheroo_client_fb_set(9)*

*4.6.0-rc5*

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

Set framebuffer of a given client. The console will be remapped to this
on switching.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
