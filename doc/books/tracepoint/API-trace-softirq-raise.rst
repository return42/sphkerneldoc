
.. _API-trace-softirq-raise:

===================
trace_softirq_raise
===================

*man trace_softirq_raise(9)*

*4.6.0-rc1*

called immediately when a softirq is raised


Synopsis
========

.. c:function:: void trace_softirq_raise( unsigned int vec_nr )

Arguments
=========

``vec_nr``
    softirq vector number


Description
===========

When used in combination with the softirq_entry tracepoint we can determine the softirq raise to run latency.
