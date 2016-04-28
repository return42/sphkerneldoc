.. -*- coding: utf-8; mode: rst -*-

.. _API-vga-switcheroo-unlock-ddc:

=========================
vga_switcheroo_unlock_ddc
=========================

*man vga_switcheroo_unlock_ddc(9)*

*4.6.0-rc5*

switch DDC lines back to previous owner


Synopsis
========

.. c:function:: int vga_switcheroo_unlock_ddc( struct pci_dev * pdev )

Arguments
=========

``pdev``
    client pci device


Description
===========

Switch DDC lines back to the previous owner after calling
``vga_switcheroo_lock_ddc``. This must be called even if
``vga_switcheroo_lock_ddc`` returned an error.


Return
======

Previous DDC owner on success (i.e. the client identifier of ``pdev``)
or a negative int on error. Specifically, ``-ENODEV`` if no handler has
registered or if the handler does not support switching the DDC lines.
Also, a negative value returned by the handler is propagated back to the
caller. Finally, invoking this function without calling
``vga_switcheroo_lock_ddc`` first is not allowed and will result in
``-EINVAL``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
