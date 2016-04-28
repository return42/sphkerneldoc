.. -*- coding: utf-8; mode: rst -*-

.. _API---napi-schedule-irqoff:

======================
__napi_schedule_irqoff
======================

*man __napi_schedule_irqoff(9)*

*4.6.0-rc5*

schedule for receive


Synopsis
========

.. c:function:: void __napi_schedule_irqoff( struct napi_struct * n )

Arguments
=========

``n``
    entry to schedule


Description
===========

Variant of ``__napi_schedule`` assuming hard irqs are masked


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
