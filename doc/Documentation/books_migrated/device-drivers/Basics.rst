.. -*- coding: utf-8; mode: rst -*-

.. _Basics:

*************
Driver Basics
*************


Driver Entry and Exit points
============================


.. kernel-doc:: include/linux/init.h
    :man-sect: 9
    :internal:


Atomic and pointer manipulation
===============================


.. kernel-doc:: arch/x86/include/asm/atomic.h
    :man-sect: 9
    :internal:


Delaying, scheduling, and timer routines
========================================


.. kernel-doc:: include/linux/sched.h
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/sched/core.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/sched/cpupri.c
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/sched/fair.c
    :man-sect: 9
    :internal:


.. kernel-doc:: include/linux/completion.h
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/time/timer.c
    :man-sect: 9
    :export:


Wait queues and Wake events
===========================


.. kernel-doc:: include/linux/wait.h
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/sched/wait.c
    :man-sect: 9
    :export:


High-resolution timers
======================


.. kernel-doc:: include/linux/ktime.h
    :man-sect: 9
    :internal:


.. kernel-doc:: include/linux/hrtimer.h
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/time/hrtimer.c
    :man-sect: 9
    :export:


Workqueues and Kevents
======================


.. kernel-doc:: include/linux/workqueue.h
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/workqueue.c
    :man-sect: 9
    :export:


Internal Functions
==================


.. kernel-doc:: kernel/exit.c
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/signal.c
    :man-sect: 9
    :internal:


.. kernel-doc:: include/linux/kthread.h
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/kthread.c
    :man-sect: 9
    :export:


Kernel objects manipulation
===========================


.. kernel-doc:: lib/kobject.c
    :man-sect: 9
    :export:


Kernel utility functions
========================


.. kernel-doc:: include/linux/kernel.h
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/printk/printk.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/panic.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/sys.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/rcu/srcu.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/rcu/tree.c
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/rcu/tree_plugin.h
    :man-sect: 9
    :export:


.. kernel-doc:: kernel/rcu/update.c
    :man-sect: 9
    :export:


Device Resource Management
==========================


.. kernel-doc:: drivers/base/devres.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
