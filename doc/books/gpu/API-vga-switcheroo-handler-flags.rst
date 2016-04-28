.. -*- coding: utf-8; mode: rst -*-

.. _API-vga-switcheroo-handler-flags:

============================
vga_switcheroo_handler_flags
============================

*man vga_switcheroo_handler_flags(9)*

*4.6.0-rc5*

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

Handler flags. A value of 0 means that no handler is registered or that
the handler has no special capabilities.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
