
.. _API---napi-schedule:

===============
__napi_schedule
===============

*man __napi_schedule(9)*

*4.6.0-rc1*

schedule for receive


Synopsis
========

.. c:function:: void __napi_schedule( struct napi_struct * n )

Arguments
=========

``n``
    entry to schedule


Description
===========

The entry's receive function will be scheduled to run. Consider using ``__napi_schedule_irqoff`` if hard irqs are masked.
