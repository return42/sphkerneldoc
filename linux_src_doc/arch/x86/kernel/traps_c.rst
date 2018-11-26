.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/traps.c

.. _`ist_begin_non_atomic`:

ist_begin_non_atomic
====================

.. c:function:: void ist_begin_non_atomic(struct pt_regs *regs)

    begin a non-atomic section in an IST exception

    :param regs:
        regs passed to the IST exception handler
    :type regs: struct pt_regs \*

.. _`ist_begin_non_atomic.description`:

Description
-----------

IST exception handlers normally cannot schedule.  As a special
exception, if the exception interrupted userspace code (i.e.
user_mode(regs) would return true) and the exception was not
a double fault, it can be safe to schedule.  \ :c:func:`ist_begin_non_atomic`\ 
begins a non-atomic section within an \ :c:func:`ist_enter`\ /ist_exit() region.
Callers are responsible for enabling interrupts themselves inside
the non-atomic section, and callers must call \ :c:func:`ist_end_non_atomic`\ 
before \ :c:func:`ist_exit`\ .

.. _`ist_end_non_atomic`:

ist_end_non_atomic
==================

.. c:function:: void ist_end_non_atomic( void)

    begin a non-atomic section in an IST exception

    :param void:
        no arguments
    :type void: 

.. _`ist_end_non_atomic.description`:

Description
-----------

Ends a non-atomic section started with \ :c:func:`ist_begin_non_atomic`\ .

.. This file was automatic generated / don't edit.

