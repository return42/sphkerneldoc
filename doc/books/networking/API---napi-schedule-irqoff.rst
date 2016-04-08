
.. _API---napi-schedule-irqoff:

======================
__napi_schedule_irqoff
======================

*man __napi_schedule_irqoff(9)*

*4.6.0-rc1*

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
