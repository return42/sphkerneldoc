
.. _API-trace-signal-deliver:

====================
trace_signal_deliver
====================

*man trace_signal_deliver(9)*

*4.6.0-rc1*

called when a signal is delivered


Synopsis
========

.. c:function:: void trace_signal_deliver( int sig, struct siginfo * info, struct k_sigaction * ka )

Arguments
=========

``sig``
    signal number

``info``
    pointer to struct siginfo

``ka``
    pointer to struct k_sigaction


Description
===========

A 'sig' signal is delivered to current process with 'info' siginfo, and it will be handled by 'ka'. ka->sa.sa_handler can be SIG_IGN or SIG_DFL. Note that some signals reported
by signal_generate tracepoint can be lost, ignored or modified (by debugger) before hitting this tracepoint. This means, this can show which signals are actually delivered, but
matching generated signals and delivered signals may not be correct.
