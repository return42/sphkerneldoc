
.. _API-kthread-should-park:

===================
kthread_should_park
===================

*man kthread_should_park(9)*

*4.6.0-rc1*

should this kthread park now?


Synopsis
========

.. c:function:: bool kthread_should_park( void )

Arguments
=========

``void``
    no arguments


Description
===========

When someone calls ``kthread_park`` on your kthread, it will be woken and this will return true. You should then do the necessary cleanup and call ``kthread_parkme``

Similar to ``kthread_should_stop``, but this keeps the thread alive and in a park position. ``kthread_unpark`` “restarts” the thread and calls the thread function again.
