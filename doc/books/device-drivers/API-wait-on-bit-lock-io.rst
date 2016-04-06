
.. _API-wait-on-bit-lock-io:

===================
wait_on_bit_lock_io
===================

*man wait_on_bit_lock_io(9)*

*4.6.0-rc1*

wait for a bit to be cleared, when wanting to set it


Synopsis
========

.. c:function:: int wait_on_bit_lock_io( unsigned long * word, int bit, unsigned mode )

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

Use the standard hashed waitqueue table to wait for a bit to be cleared and then to atomically set it. This is similar to ``wait_on_bit``, but calls ``io_schedule`` instead of
``schedule`` for the actual waiting.

Returns zero if the bit was (eventually) found to be clear and was set. Returns non-zero if a signal was delivered to the process and the ``mode`` allows that signal to wake the
process.
