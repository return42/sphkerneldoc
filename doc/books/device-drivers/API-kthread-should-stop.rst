.. -*- coding: utf-8; mode: rst -*-

.. _API-kthread-should-stop:

===================
kthread_should_stop
===================

*man kthread_should_stop(9)*

*4.6.0-rc5*

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

When someone calls ``kthread_stop`` on your kthread, it will be woken
and this will return true. You should then return, and your return value
will be passed through to ``kthread_stop``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
