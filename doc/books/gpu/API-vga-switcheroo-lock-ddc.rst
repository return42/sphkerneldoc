
.. _API-vga-switcheroo-lock-ddc:

=======================
vga_switcheroo_lock_ddc
=======================

*man vga_switcheroo_lock_ddc(9)*

*4.6.0-rc1*

temporarily switch DDC lines to a given client


Synopsis
========

.. c:function:: int vga_switcheroo_lock_ddc( struct pci_dev * pdev )

Arguments
=========

``pdev``
    client pci device


Description
===========

Temporarily switch DDC lines to the client identified by ``pdev`` (but leave the outputs otherwise switched to where they are). This allows the inactive client to probe EDID. The
DDC lines must afterwards be switched back by calling ``vga_switcheroo_unlock_ddc``, even if this function returns an error.


Return
======

Previous DDC owner on success or a negative int on error. Specifically, ``-ENODEV`` if no handler has registered or if the handler does not support switching the DDC lines. Also, a
negative value returned by the handler is propagated back to the caller. The return value has merely an informational purpose for any caller which might be interested in it. It is
acceptable to ignore the return value and simply rely on the result of the subsequent EDID probe, which will be ``NULL`` if DDC switching failed.
