.. -*- coding: utf-8; mode: rst -*-

.. _API-futex-lock-pi-atomic:

====================
futex_lock_pi_atomic
====================

*man futex_lock_pi_atomic(9)*

*4.6.0-rc5*

Atomic work required to acquire a pi aware futex


Synopsis
========

.. c:function:: int futex_lock_pi_atomic( u32 __user * uaddr, struct futex_hash_bucket * hb, union futex_key * key, struct futex_pi_state ** ps, struct task_struct * task, int set_waiters )

Arguments
=========

``uaddr``
    the pi futex user address

``hb``
    the pi futex hash bucket

``key``
    the futex key associated with uaddr and hb

``ps``
    the pi_state pointer where we store the result of the lookup

``task``
    the task to perform the atomic lock work for. This will be “current”
    except in the case of requeue pi.

``set_waiters``
    force setting the FUTEX_WAITERS bit (1) or not (0)


Return
======

0 - ready to wait; 1 - acquired the lock; <0 - error

The hb->lock and futex_key refs shall be held by the caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
