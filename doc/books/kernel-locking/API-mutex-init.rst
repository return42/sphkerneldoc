
.. _API-mutex-init:

==========
mutex_init
==========

*man mutex_init(9)*

*4.6.0-rc1*

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
