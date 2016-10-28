.. -*- coding: utf-8; mode: rst -*-

.. _cheatsheet:

***********************
Cheat Sheet For Locking
***********************

Pete Zaitcev gives the following summary:

-  If you are in a process context (any syscall) and want to lock other
   process out, use a mutex. You can take a mutex and sleep
   (:c:func:`copy_from_user*(()` or
   :c:func:`kmalloc(x,GFP_KERNEL)`).

-  Otherwise (== data can be touched in an interrupt), use
   :c:func:`spin_lock_irqsave()` and
   :c:func:`spin_unlock_irqrestore()`.

-  Avoid holding spinlock for more than 5 lines of code and across any
   function call (except accessors like :c:func:`readb()`).


.. _minimum-lock-reqirements:

Table of Minimum Requirements
=============================

The following table lists the *minimum* locking requirements between
various contexts. In some cases, the same context can only be running on
one CPU at a time, so no locking is required for that context (eg. a
particular thread can only run on one CPU at a time, but if it needs
shares data with another thread, locking is required).

Remember the advice above: you can always use
:c:func:`spin_lock_irqsave()`, which is a superset of all other
spinlock primitives.



.. flat-table:: Table of Locking Requirements
    :header-rows:  0
    :stub-columns: 0


    -  .. table row

       -  
       -  IRQ Handler A

       -  IRQ Handler B

       -  Softirq A

       -  Softirq B

       -  Tasklet A

       -  Tasklet B

       -  Timer A

       -  Timer B

       -  User Context A

       -  User Context B

    -  .. table row

       -  IRQ Handler A

       -  None

    -  .. table row

       -  IRQ Handler B

       -  SLIS

       -  None

    -  .. table row

       -  Softirq A

       -  SLI

       -  SLI

       -  SL

    -  .. table row

       -  Softirq B

       -  SLI

       -  SLI

       -  SL

       -  SL

    -  .. table row

       -  Tasklet A

       -  SLI

       -  SLI

       -  SL

       -  SL

       -  None

    -  .. table row

       -  Tasklet B

       -  SLI

       -  SLI

       -  SL

       -  SL

       -  SL

       -  None

    -  .. table row

       -  Timer A

       -  SLI

       -  SLI

       -  SL

       -  SL

       -  SL

       -  SL

       -  None

    -  .. table row

       -  Timer B

       -  SLI

       -  SLI

       -  SL

       -  SL

       -  SL

       -  SL

       -  SL

       -  None

    -  .. table row

       -  User Context A

       -  SLI

       -  SLI

       -  SLBH

       -  SLBH

       -  SLBH

       -  SLBH

       -  SLBH

       -  SLBH

       -  None

    -  .. table row

       -  User Context B

       -  SLI

       -  SLI

       -  SLBH

       -  SLBH

       -  SLBH

       -  SLBH

       -  SLBH

       -  SLBH

       -  MLI

       -  None




.. flat-table:: Legend for Locking Requirements Table
    :header-rows:  0
    :stub-columns: 0


    -  .. table row

       -  SLIS

       -  spin_lock_irqsave

    -  .. table row

       -  SLI

       -  spin_lock_irq

    -  .. table row

       -  SL

       -  spin_lock

    -  .. table row

       -  SLBH

       -  spin_lock_bh

    -  .. table row

       -  MLI

       -  mutex_lock_interruptible




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
