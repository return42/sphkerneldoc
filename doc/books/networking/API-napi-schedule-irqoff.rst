
.. _API-napi-schedule-irqoff:

====================
napi_schedule_irqoff
====================

*man napi_schedule_irqoff(9)*

*4.6.0-rc1*

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
