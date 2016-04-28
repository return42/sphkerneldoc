.. -*- coding: utf-8; mode: rst -*-

.. _hardirq-context:

================
Hard IRQ Context
================

Hardware interrupts usually communicate with a tasklet or softirq.
Frequently this involves putting work in a queue, which the softirq will
take out.


.. _hardirq-softirq:

Locking Between Hard IRQ and Softirqs/Tasklets
==============================================

If a hardware irq handler shares data with a softirq, you have two
concerns. Firstly, the softirq processing can be interrupted by a
hardware interrupt, and secondly, the critical region could be entered
by a hardware interrupt on another CPU. This is where
``spin_lock_irq()`` is used. It is defined to disable interrupts on that
cpu, then grab the lock. ``spin_unlock_irq()`` does the reverse.

The irq handler does not to use ``spin_lock_irq()``, because the softirq
cannot run while the irq handler is running: it can use ``spin_lock()``,
which is slightly faster. The only exception would be if a different
hardware irq handler uses the same lock: ``spin_lock_irq()`` will stop
that from interrupting us.

This works perfectly for UP as well: the spin lock vanishes, and this
macro simply becomes ``local_irq_disable()`` (``include/asm/smp.h``),
which protects you from the softirq/tasklet/BH being run.

``spin_lock_irqsave()`` (``include/linux/spinlock.h``) is a variant
which saves whether interrupts were on or off in a flags word, which is
passed to ``spin_unlock_irqrestore()``. This means that the same code
can be used inside an hard irq handler (where interrupts are already
off) and in softirqs (where the irq disabling is required).

Note that softirqs (and hence tasklets and timers) are run on return
from hardware interrupts, so ``spin_lock_irq()`` also stops these. In
that sense, ``spin_lock_irqsave()`` is the most general and powerful
locking function.


.. _hardirq-hardirq:

Locking Between Two Hard IRQ Handlers
=====================================

It is rare to have to share data between two IRQ handlers, but if you
do, ``spin_lock_irqsave()`` should be used: it is architecture-specific
whether all interrupts are disabled inside irq handlers themselves.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
