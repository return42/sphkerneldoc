
.. _API-wait-on-bit:

===========
wait_on_bit
===========

*man wait_on_bit(9)*

*4.6.0-rc1*

wait for a bit to be cleared


Synopsis
========

.. c:function:: int wait_on_bit( unsigned long * word, int bit, unsigned mode )

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

There is a standard hashed waitqueue table for generic use. This is the part of the hashtable's accessor API that waits on a bit. For instance, if one were to have waiters on a
bitflag, one would call ``wait_on_bit`` in threads waiting for the bit to clear. One uses ``wait_on_bit`` where one is waiting for the bit to clear, but has no intention of setting
it. Returned value will be zero if the bit was cleared, or non-zero if the process received a signal and the mode permitted wakeup on that signal.
