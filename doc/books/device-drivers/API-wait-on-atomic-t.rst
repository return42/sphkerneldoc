.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-on-atomic-t:

================
wait_on_atomic_t
================

*man wait_on_atomic_t(9)*

*4.6.0-rc5*

Wait for an atomic_t to become 0


Synopsis
========

.. c:function:: int wait_on_atomic_t( atomic_t * val, int (*action) atomic_t *, unsigned mode )

Arguments
=========

``val``
    The atomic value being waited on, a kernel virtual address

``action``
    the function used to sleep, which may take special actions

``mode``
    the task state to sleep in


Description
===========

Wait for an atomic_t to become 0. We abuse the bit-wait waitqueue table
for the purpose of getting a waitqueue, but we set the key to a bit
number outside of the target 'word'.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
