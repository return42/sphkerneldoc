.. -*- coding: utf-8; mode: rst -*-

.. _sleeping-things:

================================================
What Functions Are Safe To Call From Interrupts?
================================================

Many functions in the kernel sleep (ie. call schedule()) directly or
indirectly: you can never call them while holding a spinlock, or with
preemption disabled. This also means you need to be in user context:
calling them from an interrupt is illegal.


.. _sleeping:

Some Functions Which Sleep
==========================

The most common ones are listed below, but you usually have to read the
code to find out if other calls are safe. If everyone else who calls it
can sleep, you probably need to be able to sleep, too. In particular,
registration and deregistration functions usually expect to be called
from user context, and can sleep.

-  Accesses to userspace:

   -  ``copy_from_user()``

   -  ``copy_to_user()``

   -  ``get_user()``

   -  ``put_user()``

-  ``kmalloc(GFP_KERNEL)``

-  ``mutex_lock_interruptible()`` and ``mutex_lock()``

   There is a ``mutex_trylock()`` which does not sleep. Still, it must
   not be used inside interrupt context since its implementation is not
   safe for that. ``mutex_unlock()`` will also never sleep. It cannot be
   used in interrupt context either since a mutex must be released by
   the same task that acquired it.


.. _dont-sleep:

Some Functions Which Don't Sleep
================================

Some functions are safe to call from any context, or holding almost any
lock.

-  ``printk()``

-  ``kfree()``

-  ``add_timer()`` and ``del_timer()``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
