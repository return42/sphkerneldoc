.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-tkill:

=========
sys_tkill
=========

*man sys_tkill(9)*

*4.6.0-rc5*

send signal to one specific task


Synopsis
========

.. c:function:: long sys_tkill( pid_t pid, int sig )

Arguments
=========

``pid``
    the PID of the task

``sig``
    signal to be sent


Description
===========

Send a signal to only one task, even if it's a CLONE_THREAD task.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
