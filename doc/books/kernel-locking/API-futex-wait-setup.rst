
.. _API-futex-wait-setup:

================
futex_wait_setup
================

*man futex_wait_setup(9)*

*4.6.0-rc1*

Prepare to wait on a futex


Synopsis
========

.. c:function:: int futex_wait_setup( u32 __user * uaddr, u32 val, unsigned int flags, struct futex_q * q, struct futex_hash_bucket ** hb )

Arguments
=========

``uaddr``
    the futex userspace address

``val``
    the expected value

``flags``
    futex flags (FLAGS_SHARED, etc.)

``q``
    the associated futex_q

``hb``
    storage for hash_bucket pointer to be returned to caller


Description
===========

Setup the futex_q and locate the hash_bucket. Get the futex value and compare it with the expected value. Handle atomic faults internally. Return with the hb lock held and a
q.key reference on success, and unlocked with no q.key reference on failure.


Return
======

0 - uaddr contains val and hb has been locked; <1 - -EFAULT or -EWOULDBLOCK (uaddr does not contain val) and hb is unlocked
