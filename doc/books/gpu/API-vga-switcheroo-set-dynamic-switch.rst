.. -*- coding: utf-8; mode: rst -*-

.. _API-vga-switcheroo-set-dynamic-switch:

=================================
vga_switcheroo_set_dynamic_switch
=================================

*man vga_switcheroo_set_dynamic_switch(9)*

*4.6.0-rc5*

helper for driver power control


Synopsis
========

.. c:function:: void vga_switcheroo_set_dynamic_switch( struct pci_dev * pdev, enum vga_switcheroo_state dynamic )

Arguments
=========

``pdev``
    client pci device

``dynamic``
    new power state


Description
===========

Helper for GPUs whose power state is controlled by the driver's runtime
pm. When the driver decides to power up or down, it notifies
vga_switcheroo thereof using this helper so that it can (a) power the
audio device on the GPU up or down, and (b) update its internal power
state representation for the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
