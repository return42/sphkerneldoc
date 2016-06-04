.. -*- coding: utf-8; mode: rst -*-

.. _api:

===
API
===


Public functions
================


.. kernel-doc:: drivers/gpu/vga/vga_switcheroo.c
    :export:

Public structures
=================


.. kernel-doc:: include/linux/vga_switcheroo.h
    :functions: vga_switcheroo_handler

.. kernel-doc:: include/linux/vga_switcheroo.h
    :functions: vga_switcheroo_client_ops

Public constants
================


.. kernel-doc:: include/linux/vga_switcheroo.h
    :functions: vga_switcheroo_handler_flags_t

.. kernel-doc:: include/linux/vga_switcheroo.h
    :functions: vga_switcheroo_client_id

.. kernel-doc:: include/linux/vga_switcheroo.h
    :functions: vga_switcheroo_state

Private structures
==================


.. kernel-doc:: drivers/gpu/vga/vga_switcheroo.c
    :functions: vgasr_priv

.. kernel-doc:: drivers/gpu/vga/vga_switcheroo.c
    :functions: vga_switcheroo_client



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
