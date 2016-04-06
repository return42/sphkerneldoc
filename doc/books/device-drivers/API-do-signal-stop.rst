
.. _API-do-signal-stop:

==============
do_signal_stop
==============

*man do_signal_stop(9)*

*4.6.0-rc1*

handle group stop for SIGSTOP and other stop signals


Synopsis
========

.. c:function:: bool do_signal_stop( int signr )

Arguments
=========

``signr``
    signr causing group stop if initiating


Description
===========

If ``JOBCTL_STOP_PENDING`` is not set yet, initiate group stop with ``signr`` and participate in it. If already set, participate in the existing group stop. If participated in a
group stop (and thus slept), ``true`` is returned with siglock released.

If ptraced, this function doesn't handle stop itself. Instead, ``JOBCTL_TRAP_STOP`` is scheduled and ``false`` is returned with siglock untouched. The caller must ensure that
INTERRUPT trap handling takes places afterwards.


CONTEXT
=======

Must be called with ``current``->sighand->siglock held, which is released on ``true`` return.


RETURNS
=======

``false`` if group stop is already cancelled or ptrace trap is scheduled. ``true`` if participated in group stop.
