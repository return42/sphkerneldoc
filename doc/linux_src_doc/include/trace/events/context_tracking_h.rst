.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/context_tracking.h

.. _`trace_user_enter`:

trace_user_enter
================

.. c:function:: void trace_user_enter(int dummy)

    called when the kernel resumes to userspace

    :param int dummy:
        dummy arg to make trace event macro happy

.. _`trace_user_enter.description`:

Description
-----------

This event occurs when the kernel resumes to userspace  after
an exception or a syscall.

.. _`trace_user_exit`:

trace_user_exit
===============

.. c:function:: void trace_user_exit(int dummy)

    called when userspace enters the kernel

    :param int dummy:
        dummy arg to make trace event macro happy

.. _`trace_user_exit.description`:

Description
-----------

This event occurs when userspace enters the kernel through
an exception or a syscall.

.. This file was automatic generated / don't edit.

