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
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
