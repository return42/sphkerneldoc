.. -*- coding: utf-8; mode: rst -*-

.. _API-schedule-work:

=============
schedule_work
=============

*man schedule_work(9)*

*4.6.0-rc5*

put work task in global workqueue


Synopsis
========

.. c:function:: bool schedule_work( struct work_struct * work )

Arguments
=========

``work``
    job to be done


Description
===========

Returns ``false`` if ``work`` was already on the kernel-global workqueue
and ``true`` otherwise.

This puts a job in the kernel-global workqueue if it was not already
queued and leaves it in the same position on the kernel-global workqueue
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
