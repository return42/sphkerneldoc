.. -*- coding: utf-8; mode: rst -*-

.. _API-kthread-should-park:

===================
kthread_should_park
===================

*man kthread_should_park(9)*

*4.6.0-rc5*

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

When someone calls ``kthread_park`` on your kthread, it will be woken
and this will return true. You should then do the necessary cleanup and
call ``kthread_parkme``

Similar to ``kthread_should_stop``, but this keeps the thread alive and
in a park position. ``kthread_unpark`` “restarts” the thread and calls
the thread function again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
