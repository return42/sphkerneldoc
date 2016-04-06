
.. _API-schedule-delayed-work-on:

========================
schedule_delayed_work_on
========================

*man schedule_delayed_work_on(9)*

*4.6.0-rc1*

queue work in global workqueue on CPU after delay


Synopsis
========

.. c:function:: bool schedule_delayed_work_on( int cpu, struct delayed_work * dwork, unsigned long delay )

Arguments
=========

``cpu``
    cpu to use

``dwork``
    job to be done

``delay``
    number of jiffies to wait


Description
===========

After waiting for a given time this puts a job in the kernel-global workqueue on the specified CPU.
