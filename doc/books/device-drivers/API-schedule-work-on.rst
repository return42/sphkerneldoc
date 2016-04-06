
.. _API-schedule-work-on:

================
schedule_work_on
================

*man schedule_work_on(9)*

*4.6.0-rc1*

put work task on a specific cpu


Synopsis
========

.. c:function:: bool schedule_work_on( int cpu, struct work_struct * work )

Arguments
=========

``cpu``
    cpu to put the work task on

``work``
    job to be done


Description
===========

This puts a job on a specific cpu
