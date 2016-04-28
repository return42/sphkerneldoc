.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-vga-switcheroo-handler-flags-t:

===================================
enum vga_switcheroo_handler_flags_t
===================================

*man enum vga_switcheroo_handler_flags_t(9)*

*4.6.0-rc5*

handler flags bitmask


Synopsis
========

.. code-block:: c

    enum vga_switcheroo_handler_flags_t {
      VGA_SWITCHEROO_CAN_SWITCH_DDC,
      VGA_SWITCHEROO_NEEDS_EDP_CONFIG
    };


Constants
=========

VGA_SWITCHEROO_CAN_SWITCH_DDC
    whether the handler is able to switch the DDC lines separately. This
    signals to clients that they should call ``drm_get_edid_switcheroo``
    to probe the EDID

VGA_SWITCHEROO_NEEDS_EDP_CONFIG
    whether the handler is unable to switch the AUX channel separately.
    This signals to clients that the active GPU needs to train the link
    and communicate the link parameters to the inactive GPU (mediated by
    vga_switcheroo). The inactive GPU may then skip the AUX handshake
    and set up its output with these pre-calibrated values (DisplayPort
    specification v1.1a, section 2.5.3.3)


Description
===========

Handler flags bitmask. Used by handlers to declare their capabilities
upon registering with vga_switcheroo.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
