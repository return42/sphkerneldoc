.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-signal-info:

===================
__audit_signal_info
===================

*man __audit_signal_info(9)*

*4.6.0-rc5*

record signal info for shutting down audit subsystem


Synopsis
========

.. c:function:: int __audit_signal_info( int sig, struct task_struct * t )

Arguments
=========

``sig``
    signal value

``t``
    task being signaled


Description
===========

If the audit subsystem is being terminated, record the task (pid) and
uid that is doing that.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
