
.. _API-fixup-owner:

===========
fixup_owner
===========

*man fixup_owner(9)*

*4.6.0-rc1*

Post lock pi_state and corner case management


Synopsis
========

.. c:function:: int fixup_owner( u32 __user * uaddr, struct futex_q * q, int locked )

Arguments
=========

``uaddr``
    user address of the futex

``q``
    futex_q (contains pi_state and access to the rt_mutex)

``locked``
    if the attempt to take the rt_mutex succeeded (1) or not (0)


Description
===========

After attempting to lock an rt_mutex, this function is called to cleanup the pi_state owner as well as handle race conditions that may allow us to acquire the lock. Must be
called with the hb lock held.


Return
======

1 - success, lock taken; 0 - success, lock not taken; <0 - on error (-EFAULT)
