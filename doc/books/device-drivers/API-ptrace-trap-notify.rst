.. -*- coding: utf-8; mode: rst -*-

.. _API-ptrace-trap-notify:

==================
ptrace_trap_notify
==================

*man ptrace_trap_notify(9)*

*4.6.0-rc5*

schedule trap to notify ptracer


Synopsis
========

.. c:function:: void ptrace_trap_notify( struct task_struct * t )

Arguments
=========

``t``
    tracee wanting to notify tracer


Description
===========

This function schedules sticky ptrace trap which is cleared on the next
TRAP_STOP to notify ptracer of an event. ``t`` must have been seized by
ptracer.

If ``t`` is running, STOP trap will be taken. If trapped for STOP and
ptracer is listening for events, tracee is woken up so that it can
re-trap for the new event. If trapped otherwise, STOP trap will be
eventually taken without returning to userland after the existing traps
are finished by PTRACE_CONT.


CONTEXT
=======

Must be called with ``task``->sighand->siglock held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
