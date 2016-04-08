
.. _API-trace-softirq-entry:

===================
trace_softirq_entry
===================

*man trace_softirq_entry(9)*

*4.6.0-rc1*

called immediately before the softirq handler


Synopsis
========

.. c:function:: void trace_softirq_entry( unsigned int vec_nr )

Arguments
=========

``vec_nr``
    softirq vector number


Description
===========

When used in combination with the softirq_exit tracepoint we can determine the softirq handler routine.
