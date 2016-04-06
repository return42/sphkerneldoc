
.. _API-wakeup-readers:

==============
wakeup_readers
==============

*man wakeup_readers(9)*

*4.6.0-rc1*

wake up readers waiting on a channel


Synopsis
========

.. c:function:: void wakeup_readers( unsigned long data )

Arguments
=========

``data``
    contains the channel buffer


Description
===========

This is the timer function used to defer reader waking.
