.. -*- coding: utf-8; mode: rst -*-

.. _API-arch-phys-wc-add:

================
arch_phys_wc_add
================

*man arch_phys_wc_add(9)*

*4.6.0-rc5*

add a WC MTRR and handle errors if PAT is unavailable


Synopsis
========

.. c:function:: int arch_phys_wc_add( unsigned long base, unsigned long size )

Arguments
=========

``base``
    Physical base address

``size``
    Size of region


Description
===========

If PAT is available, this does nothing. If PAT is unavailable, it
attempts to add a WC MTRR covering size bytes starting at base and logs
an error if this fails.

The called should provide a power of two size on an equivalent power of
two boundary.

Drivers must store the return value to pass to
mtrr_del_wc_if_needed, but drivers should not try to interpret that
return value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
