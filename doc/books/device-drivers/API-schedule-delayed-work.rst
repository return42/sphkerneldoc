.. -*- coding: utf-8; mode: rst -*-

.. _API-schedule-delayed-work:

=====================
schedule_delayed_work
=====================

*man schedule_delayed_work(9)*

*4.6.0-rc5*

put work task in global workqueue after delay


Synopsis
========

.. c:function:: bool schedule_delayed_work( struct delayed_work * dwork, unsigned long delay )

Arguments
=========

``dwork``
    job to be done

``delay``
    number of jiffies to wait or 0 for immediate execution


Description
===========

After waiting for a given time this puts a job in the kernel-global
workqueue.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
