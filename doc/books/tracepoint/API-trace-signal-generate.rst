.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-signal-generate:

=====================
trace_signal_generate
=====================

*man trace_signal_generate(9)*

*4.6.0-rc5*

called when a signal is generated


Synopsis
========

.. c:function:: void trace_signal_generate( int sig, struct siginfo * info, struct task_struct * task, int group, int result )

Arguments
=========

``sig``
    signal number

``info``
    pointer to struct siginfo

``task``
    pointer to struct task_struct

``group``
    shared or private

``result``
    TRACE_SIGNAL_*


Description
===========

Current process sends a 'sig' signal to 'task' process with 'info'
siginfo. If 'info' is SEND_SIG_NOINFO or SEND_SIG_PRIV, 'info' is
not a pointer and you can't access its field. Instead, SEND_SIG_NOINFO
means that si_code is SI_USER, and SEND_SIG_PRIV means that si_code
is SI_KERNEL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
