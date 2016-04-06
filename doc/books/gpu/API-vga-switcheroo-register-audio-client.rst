
.. _API-vga-switcheroo-register-audio-client:

====================================
vga_switcheroo_register_audio_client
====================================

*man vga_switcheroo_register_audio_client(9)*

*4.6.0-rc1*

register audio client


Synopsis
========

.. c:function:: int vga_switcheroo_register_audio_client( struct pci_dev * pdev, const struct vga_switcheroo_client_ops * ops, enum vga_switcheroo_client_id id )

Arguments
=========

``pdev``
    client pci device

``ops``
    client callbacks

``id``
    client identifier


Description
===========

Register audio client (audio device on a GPU). The power state of the client is assumed to be ON.


Return
======

0 on success, -ENOMEM on memory allocation error.
