.. -*- coding: utf-8; mode: rst -*-

.. _doirq:

********************
__do_IRQ entry point
********************

The original implementation __do_IRQ() was an alternative entry point
for all types of interrupts. It no longer exists.

This handler turned out to be not suitable for all interrupt hardware
and was therefore reimplemented with split functionality for
edge/level/simple/percpu interrupts. This is not only a functional
optimization. It also shortens code paths for interrupts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
