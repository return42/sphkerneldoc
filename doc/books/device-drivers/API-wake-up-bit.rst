.. -*- coding: utf-8; mode: rst -*-

.. _API-wake-up-bit:

===========
wake_up_bit
===========

*man wake_up_bit(9)*

*4.6.0-rc5*

wake up a waiter on a bit


Synopsis
========

.. c:function:: void wake_up_bit( void * word, int bit )

Arguments
=========

``word``
    the word being waited on, a kernel virtual address

``bit``
    the bit of the word being waited on


Description
===========

There is a standard hashed waitqueue table for generic use. This is the
part of the hashtable's accessor API that wakes up waiters on a bit. For
instance, if one were to have waiters on a bitflag, one would call
``wake_up_bit`` after clearing the bit.

In order for this to function properly, as it uses ``waitqueue_active``
internally, some kind of memory barrier must be done prior to calling
this. Typically, this will be ``smp_mb__after_atomic``, but in some
cases where bitflags are manipulated non-atomically under a lock, one
may need to use a less regular barrier, such fs/inode.c's ``smp_mb``,
because ``spin_unlock`` does not guarantee a memory barrier.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
