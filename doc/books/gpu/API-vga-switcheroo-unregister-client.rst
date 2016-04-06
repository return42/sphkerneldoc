
.. _API-vga-switcheroo-unregister-client:

================================
vga_switcheroo_unregister_client
================================

*man vga_switcheroo_unregister_client(9)*

*4.6.0-rc1*

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

Unregister client. Disable vga_switcheroo if this is a vga client (GPU).
