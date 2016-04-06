
.. _API-vga-switcheroo-handler-flags:

============================
vga_switcheroo_handler_flags
============================

*man vga_switcheroo_handler_flags(9)*

*4.6.0-rc1*

obtain handler flags


Synopsis
========

.. c:function:: enum vga_switcheroo_handler_flags_t vga_switcheroo_handler_flags( void )

Arguments
=========

``void``
    no arguments


Description
===========

Helper for clients to obtain the handler flags bitmask.


Return
======

Handler flags. A value of 0 means that no handler is registered or that the handler has no special capabilities.
