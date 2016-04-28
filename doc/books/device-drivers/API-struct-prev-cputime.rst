.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-prev-cputime:

===================
struct prev_cputime
===================

*man struct prev_cputime(9)*

*4.6.0-rc5*

snaphsot of system and user cputime


Synopsis
========

.. code-block:: c

    struct prev_cputime {
    #ifndef CONFIG_VIRT_CPU_ACCOUNTING_NATIVE
      cputime_t utime;
      cputime_t stime;
      raw_spinlock_t lock;
    #endif
    };


Members
=======

utime
    time spent in user mode

stime
    time spent in system mode

lock
    protects the above two fields


Description
===========

Stores previous user/system time values such that we can guarantee
monotonicity.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
