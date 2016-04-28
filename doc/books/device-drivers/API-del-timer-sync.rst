.. -*- coding: utf-8; mode: rst -*-

.. _API-del-timer-sync:

==============
del_timer_sync
==============

*man del_timer_sync(9)*

*4.6.0-rc5*

deactivate a timer and wait for the handler to finish.


Synopsis
========

.. c:function:: int del_timer_sync( struct timer_list * timer )

Arguments
=========

``timer``
    the timer to be deactivated


Description
===========

This function only differs from ``del_timer`` on SMP: besides
deactivating the timer it also makes sure the handler has finished
executing on other CPUs.


Synchronization rules
=====================

Callers must prevent restarting of the timer, otherwise this function is
meaningless. It must not be called from interrupt contexts unless the
timer is an irqsafe one. The caller must not hold locks which would
prevent completion of the timer's handler. The timer's handler must not
call ``add_timer_on``. Upon exit the timer is not queued and the handler
is not running on any CPU.


Note
====

For !irqsafe timers, you must not hold locks that are held in interrupt
context while calling this function. Even if the lock has nothing to do
with the timer in question. Here's why:

CPU0 CPU1 ---- ---- <SOFTIRQ> ``call_timer_fn``; base->running_timer =
mytimer; spin_lock_irq(somelock); <IRQ> spin_lock(somelock);
del_timer_sync(mytimer); while (base->running_timer == mytimer);

Now ``del_timer_sync`` will never return and never release somelock. The
interrupt on the other CPU is waiting to grab somelock but it has
interrupted the softirq that CPU0 is waiting to finish.

The function returns whether it has deactivated a pending timer or not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
