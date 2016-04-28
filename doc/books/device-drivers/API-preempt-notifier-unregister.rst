.. -*- coding: utf-8; mode: rst -*-

.. _API-preempt-notifier-unregister:

===========================
preempt_notifier_unregister
===========================

*man preempt_notifier_unregister(9)*

*4.6.0-rc5*

no longer interested in preemption notifications


Synopsis
========

.. c:function:: void preempt_notifier_unregister( struct preempt_notifier * notifier )

Arguments
=========

``notifier``
    notifier struct to unregister


Description
===========

This is *not* safe to call from within a preemption notifier.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
