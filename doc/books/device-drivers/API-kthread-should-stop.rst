
.. _API-kthread-should-stop:

===================
kthread_should_stop
===================

*man kthread_should_stop(9)*

*4.6.0-rc1*

should this kthread return now?


Synopsis
========

.. c:function:: bool kthread_should_stop( void )

Arguments
=========

``void``
    no arguments


Description
===========

When someone calls ``kthread_stop`` on your kthread, it will be woken and this will return true. You should then return, and your return value will be passed through to
``kthread_stop``.
