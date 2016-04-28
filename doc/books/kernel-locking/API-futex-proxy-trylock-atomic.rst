.. -*- coding: utf-8; mode: rst -*-

.. _API-futex-proxy-trylock-atomic:

==========================
futex_proxy_trylock_atomic
==========================

*man futex_proxy_trylock_atomic(9)*

*4.6.0-rc5*

Attempt an atomic lock for the top waiter


Synopsis
========

.. c:function:: int futex_proxy_trylock_atomic( u32 __user * pifutex, struct futex_hash_bucket * hb1, struct futex_hash_bucket * hb2, union futex_key * key1, union futex_key * key2, struct futex_pi_state ** ps, int set_waiters )

Arguments
=========

``pifutex``
    the user address of the to futex

``hb1``
    the from futex hash bucket, must be locked by the caller

``hb2``
    the to futex hash bucket, must be locked by the caller

``key1``
    the from futex key

``key2``
    the to futex key

``ps``
    address to store the pi_state pointer

``set_waiters``
    force setting the FUTEX_WAITERS bit (1) or not (0)


Description
===========

Try and get the lock on behalf of the top waiter if we can do it
atomically. Wake the top waiter if we succeed. If the caller specified
set_waiters, then direct ``futex_lock_pi_atomic`` to force setting the
FUTEX_WAITERS bit. hb1 and hb2 must be held by the caller.


Return
======

0 - failed to acquire the lock atomically; >0 - acquired the lock,
return value is vpid of the top_waiter <0 - error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
