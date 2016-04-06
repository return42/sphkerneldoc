
.. _API-vga-switcheroo-register-handler:

===============================
vga_switcheroo_register_handler
===============================

*man vga_switcheroo_register_handler(9)*

*4.6.0-rc1*

register handler


Synopsis
========

.. c:function:: int vga_switcheroo_register_handler( const struct vga_switcheroo_handler * handler, enum vga_switcheroo_handler_flags_t handler_flags )

Arguments
=========

``handler``
    handler callbacks

``handler_flags``
    handler flags


Description
===========

Register handler. Enable vga_switcheroo if two vga clients have already registered.


Return
======

0 on success, -EINVAL if a handler was already registered.
