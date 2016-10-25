.. -*- coding: utf-8; mode: rst -*-

.. _genericchip:

**********************
Generic interrupt chip
**********************

To avoid copies of identical implementations of IRQ chips the core
provides a configurable generic interrupt chip implementation.
Developers should check carefully whether the generic chip fits their
needs before implementing the same functionality slightly differently
themselves.


.. kernel-doc:: kernel/irq/generic-chip.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
