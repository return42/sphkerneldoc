.. -*- coding: utf-8; mode: rst -*-

.. _API-vga-switcheroo-get-client-state:

===============================
vga_switcheroo_get_client_state
===============================

*man vga_switcheroo_get_client_state(9)*

*4.6.0-rc5*

obtain power state of a given client


Synopsis
========

.. c:function:: enum vga_switcheroo_state vga_switcheroo_get_client_state( struct pci_dev * pdev )

Arguments
=========

``pdev``
    client pci device


Description
===========

Obtain power state of a given client as seen from vga_switcheroo. The
function is only called from hda_intel.c.


Return
======

Power state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
