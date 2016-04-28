.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-vga-switcheroo-state:

=========================
enum vga_switcheroo_state
=========================

*man enum vga_switcheroo_state(9)*

*4.6.0-rc5*

client power state


Synopsis
========

.. code-block:: c

    enum vga_switcheroo_state {
      VGA_SWITCHEROO_OFF,
      VGA_SWITCHEROO_ON,
      VGA_SWITCHEROO_NOT_FOUND
    };


Constants
=========

VGA_SWITCHEROO_OFF
    off

VGA_SWITCHEROO_ON
    on

VGA_SWITCHEROO_NOT_FOUND
    client has not registered with vga_switcheroo. Only used in
    ``vga_switcheroo_get_client_state`` which in turn is only called
    from hda_intel.c


Description
===========

Client power state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
