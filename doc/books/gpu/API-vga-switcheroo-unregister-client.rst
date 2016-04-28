.. -*- coding: utf-8; mode: rst -*-

.. _API-vga-switcheroo-unregister-client:

================================
vga_switcheroo_unregister_client
================================

*man vga_switcheroo_unregister_client(9)*

*4.6.0-rc5*

unregister client


Synopsis
========

.. c:function:: void vga_switcheroo_unregister_client( struct pci_dev * pdev )

Arguments
=========

``pdev``
    client pci device


Description
===========

Unregister client. Disable vga_switcheroo if this is a vga client
(GPU).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
