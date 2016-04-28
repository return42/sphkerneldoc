.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-softirq-exit:

==================
trace_softirq_exit
==================

*man trace_softirq_exit(9)*

*4.6.0-rc5*

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

When used in combination with the softirq_entry tracepoint we can
determine the softirq handler routine.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
