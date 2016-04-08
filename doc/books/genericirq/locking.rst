
.. _locking:

==============
Locking on SMP
==============

The locking of chip registers is up to the architecture that defines the chip primitives. The per-irq structure is protected via desc->lock, by the generic layer.
