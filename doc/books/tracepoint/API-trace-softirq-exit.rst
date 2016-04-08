
.. _API-trace-softirq-exit:

==================
trace_softirq_exit
==================

*man trace_softirq_exit(9)*

*4.6.0-rc1*

called immediately after the softirq handler returns


Synopsis
========

.. c:function:: void trace_softirq_exit( unsigned int vec_nr )

Arguments
=========

``vec_nr``
    softirq vector number


Description
===========

When used in combination with the softirq_entry tracepoint we can determine the softirq handler routine.
