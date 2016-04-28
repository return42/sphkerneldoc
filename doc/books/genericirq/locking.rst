.. -*- coding: utf-8; mode: rst -*-

.. _locking:

==============
Locking on SMP
==============

The locking of chip registers is up to the architecture that defines the
chip primitives. The per-irq structure is protected via desc->lock, by
the generic layer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
