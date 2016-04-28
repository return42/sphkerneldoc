.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-softirq-entry:

===================
trace_softirq_entry
===================

*man trace_softirq_entry(9)*

*4.6.0-rc5*

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

When used in combination with the softirq_exit tracepoint we can
determine the softirq handler routine.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
