.. -*- coding: utf-8; mode: rst -*-

.. _API-napi-schedule-irqoff:

====================
napi_schedule_irqoff
====================

*man napi_schedule_irqoff(9)*

*4.6.0-rc5*

schedule NAPI poll


Synopsis
========

.. c:function:: void napi_schedule_irqoff( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Variant of ``napi_schedule``, assuming hard irqs are masked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
