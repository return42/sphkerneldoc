.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/signal.h

.. _`trace_signal_generate`:

trace_signal_generate
=====================

.. c:function:: void trace_signal_generate(int sig, struct kernel_siginfo *info, struct task_struct *task, int group, int result)

    called when a signal is generated

    :param sig:
        signal number
    :type sig: int

    :param info:
        pointer to struct siginfo
    :type info: struct kernel_siginfo \*

    :param task:
        pointer to struct task_struct
    :type task: struct task_struct \*

    :param group:
        shared or private
    :type group: int

    :param result:
        TRACE_SIGNAL_*
    :type result: int

.. _`trace_signal_generate.description`:

Description
-----------

Current process sends a 'sig' signal to 'task' process with
'info' siginfo. If 'info' is SEND_SIG_NOINFO or SEND_SIG_PRIV,
'info' is not a pointer and you can't access its field. Instead,
SEND_SIG_NOINFO means that si_code is SI_USER, and SEND_SIG_PRIV
means that si_code is SI_KERNEL.

.. _`trace_signal_deliver`:

trace_signal_deliver
====================

.. c:function:: void trace_signal_deliver(int sig, struct kernel_siginfo *info, struct k_sigaction *ka)

    called when a signal is delivered

    :param sig:
        signal number
    :type sig: int

    :param info:
        pointer to struct siginfo
    :type info: struct kernel_siginfo \*

    :param ka:
        pointer to struct k_sigaction
    :type ka: struct k_sigaction \*

.. _`trace_signal_deliver.description`:

Description
-----------

A 'sig' signal is delivered to current process with 'info' siginfo,
and it will be handled by 'ka'. ka->sa.sa_handler can be SIG_IGN or
SIG_DFL.
Note that some signals reported by signal_generate tracepoint can be
lost, ignored or modified (by debugger) before hitting this tracepoint.
This means, this can show which signals are actually delivered, but
matching generated signals and delivered signals may not be correct.

.. This file was automatic generated / don't edit.

