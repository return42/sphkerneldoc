
.. _API-schedule-delayed-work:

=====================
schedule_delayed_work
=====================

*man schedule_delayed_work(9)*

*4.6.0-rc1*

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

After waiting for a given time this puts a job in the kernel-global workqueue.
