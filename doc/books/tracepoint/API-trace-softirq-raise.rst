.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-softirq-raise:

===================
trace_softirq_raise
===================

*man trace_softirq_raise(9)*

*4.6.0-rc5*

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

When used in combination with the softirq_entry tracepoint we can
determine the softirq raise to run latency.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
