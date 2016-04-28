.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-on-bit-lock:

================
wait_on_bit_lock
================

*man wait_on_bit_lock(9)*

*4.6.0-rc5*

wait for a bit to be cleared, when wanting to set it


Synopsis
========

.. c:function:: int wait_on_bit_lock( unsigned long * word, int bit, unsigned mode )

Arguments
=========

``word``
    the word being waited on, a kernel virtual address

``bit``
    the bit of the word being waited on

``mode``
    the task state to sleep in


Description
===========

There is a standard hashed waitqueue table for generic use. This is the
part of the hashtable's accessor API that waits on a bit when one
intends to set it, for instance, trying to lock bitflags. For instance,
if one were to have waiters trying to set bitflag and waiting for it to
clear before setting it, one would call ``wait_on_bit`` in threads
waiting to be able to set the bit. One uses ``wait_on_bit_lock`` where
one is waiting for the bit to clear with the intention of setting it,
and when done, clearing it.

Returns zero if the bit was (eventually) found to be clear and was set.
Returns non-zero if a signal was delivered to the process and the
``mode`` allows that signal to wake the process.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
