
.. _API-enum-vga-switcheroo-state:

=========================
enum vga_switcheroo_state
=========================

*man enum vga_switcheroo_state(9)*

*4.6.0-rc1*

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
    client has not registered with vga_switcheroo. Only used in ``vga_switcheroo_get_client_state`` which in turn is only called from hda_intel.c


Description
===========

Client power state.
