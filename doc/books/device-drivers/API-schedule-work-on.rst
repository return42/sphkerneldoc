.. -*- coding: utf-8; mode: rst -*-

.. _API-schedule-work-on:

================
schedule_work_on
================

*man schedule_work_on(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
