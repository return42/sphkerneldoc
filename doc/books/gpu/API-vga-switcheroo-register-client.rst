
.. _API-vga-switcheroo-register-client:

==============================
vga_switcheroo_register_client
==============================

*man vga_switcheroo_register_client(9)*

*4.6.0-rc1*

register vga client


Synopsis
========

.. c:function:: int vga_switcheroo_register_client( struct pci_dev * pdev, const struct vga_switcheroo_client_ops * ops, bool driver_power_control )

Arguments
=========

``pdev``
    client pci device

``ops``
    client callbacks

``driver_power_control``
    whether power state is controlled by the driver's runtime pm


Description
===========

Register vga client (GPU). Enable vga_switcheroo if another GPU and a handler have already registered. The power state of the client is assumed to be ON.


Return
======

0 on success, -ENOMEM on memory allocation error.
