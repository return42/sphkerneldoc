.. -*- coding: utf-8; mode: rst -*-

.. _API-mutex-init:

==========
mutex_init
==========

*man mutex_init(9)*

*4.6.0-rc5*

initialize the mutex


Synopsis
========

.. c:function:: mutex_init( mutex )

Arguments
=========

``mutex``
    the mutex to be initialized


Description
===========

Initialize the mutex to unlocked state.

It is not allowed to initialize an already locked mutex.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
