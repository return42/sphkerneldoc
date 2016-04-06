
.. _API-wait-on-bit-timeout:

===================
wait_on_bit_timeout
===================

*man wait_on_bit_timeout(9)*

*4.6.0-rc1*

wait for a bit to be cleared or a timeout elapses


Synopsis
========

.. c:function:: int wait_on_bit_timeout( unsigned long * word, int bit, unsigned mode, unsigned long timeout )

Arguments
=========

``word``
    the word being waited on, a kernel virtual address

``bit``
    the bit of the word being waited on

``mode``
    the task state to sleep in

``timeout``
    timeout, in jiffies


Description
===========

Use the standard hashed waitqueue table to wait for a bit to be cleared. This is similar to ``wait_on_bit``, except also takes a timeout parameter.

Returned value will be zero if the bit was cleared before the ``timeout`` elapsed, or non-zero if the ``timeout`` elapsed or process received a signal and the mode permitted wakeup
on that signal.
