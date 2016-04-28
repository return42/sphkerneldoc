.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-on-bit-action:

==================
wait_on_bit_action
==================

*man wait_on_bit_action(9)*

*4.6.0-rc5*

wait for a bit to be cleared


Synopsis
========

.. c:function:: int wait_on_bit_action( unsigned long * word, int bit, wait_bit_action_f * action, unsigned mode )

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

Use the standard hashed waitqueue table to wait for a bit to be cleared,
and allow the waiting action to be specified. This is like
``wait_on_bit`` but allows fine control of how the waiting is done.

Returned value will be zero if the bit was cleared, or non-zero if the
process received a signal and the mode permitted wakeup on that signal.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
