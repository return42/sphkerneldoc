.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-on-bit-io:

==============
wait_on_bit_io
==============

*man wait_on_bit_io(9)*

*4.6.0-rc5*

wait for a bit to be cleared


Synopsis
========

.. c:function:: int wait_on_bit_io( unsigned long * word, int bit, unsigned mode )

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

Use the standard hashed waitqueue table to wait for a bit to be cleared.
This is similar to ``wait_on_bit``, but calls ``io_schedule`` instead of
``schedule`` for the actual waiting.

Returned value will be zero if the bit was cleared, or non-zero if the
process received a signal and the mode permitted wakeup on that signal.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
