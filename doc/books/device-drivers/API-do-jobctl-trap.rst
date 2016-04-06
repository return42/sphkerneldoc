
.. _API-do-jobctl-trap:

==============
do_jobctl_trap
==============

*man do_jobctl_trap(9)*

*4.6.0-rc1*

take care of ptrace jobctl traps


Synopsis
========

.. c:function:: void do_jobctl_trap( void )

Arguments
=========

``void``
    no arguments


Description
===========

When PT_SEIZED, it's used for both group stop and explicit SEIZE/INTERRUPT traps. Both generate PTRACE_EVENT_STOP trap with accompanying siginfo. If stopped, lower eight bits of
exit_code contain the stop signal; otherwise, ``SIGTRAP``.

When !PT_SEIZED, it's used only for group stop trap with stop signal number as exit_code and no siginfo.


CONTEXT
=======

Must be called with ``current``->sighand->siglock held, which may be released and re-acquired before returning with intervening sleep.
