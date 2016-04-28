.. -*- coding: utf-8; mode: rst -*-

.. _API-signal-delivered:

================
signal_delivered
================

*man signal_delivered(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: void signal_delivered( struct ksignal * ksig, int stepping )

Arguments
=========

``ksig``
    kernel signal struct

``stepping``
    nonzero if debugger single-step or block-step in use


Description
===========

This function should be called when a signal has successfully been
delivered. It updates the blocked signals accordingly
(``ksig``->ka.sa.sa_mask is always blocked, and the signal itself is
blocked unless ``SA_NODEFER`` is set in ``ksig``->ka.sa.sa_flags.
Tracing is notified.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
