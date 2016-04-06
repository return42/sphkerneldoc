
.. _API---audit-signal-info:

===================
__audit_signal_info
===================

*man __audit_signal_info(9)*

*4.6.0-rc1*

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

If the audit subsystem is being terminated, record the task (pid) and uid that is doing that.
