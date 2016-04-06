
.. _API-wait-on-bit-lock-action:

=======================
wait_on_bit_lock_action
=======================

*man wait_on_bit_lock_action(9)*

*4.6.0-rc1*

wait for a bit to be cleared, when wanting to set it


Synopsis
========

.. c:function:: int wait_on_bit_lock_action( unsigned long * word, int bit, wait_bit_action_f * action, unsigned mode )

Arguments
=========

``word``
    the word being waited on, a kernel virtual address

``bit``
    the bit of the word being waited on

``action``
    the function used to sleep, which may take special actions

``mode``
    the task state to sleep in


Description
===========

Use the standard hashed waitqueue table to wait for a bit to be cleared and then to set it, and allow the waiting action to be specified. This is like ``wait_on_bit`` but allows
fine control of how the waiting is done.

Returns zero if the bit was (eventually) found to be clear and was set. Returns non-zero if a signal was delivered to the process and the ``mode`` allows that signal to wake the
process.
