.. -*- coding: utf-8; mode: rst -*-

.. _API---napi-schedule:

===============
__napi_schedule
===============

*man __napi_schedule(9)*

*4.6.0-rc5*

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

The entry's receive function will be scheduled to run. Consider using
``__napi_schedule_irqoff`` if hard irqs are masked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
