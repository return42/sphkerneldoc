.. -*- coding: utf-8; mode: rst -*-

.. _API-wakeup-readers:

==============
wakeup_readers
==============

*man wakeup_readers(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
