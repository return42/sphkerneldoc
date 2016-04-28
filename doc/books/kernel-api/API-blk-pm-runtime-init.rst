.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-pm-runtime-init:

===================
blk_pm_runtime_init
===================

*man blk_pm_runtime_init(9)*

*4.6.0-rc5*

Block layer runtime PM initialization routine


Synopsis
========

.. c:function:: void blk_pm_runtime_init( struct request_queue * q, struct device * dev )

Arguments
=========

``q``
    the queue of the device

``dev``
    the device the queue belongs to


Description
===========

Initialize runtime-PM-related fields for ``q`` and start auto suspend
for ``dev``. Drivers that want to take advantage of request-based
runtime PM should call this function after ``dev`` has been initialized,
and its request queue ``q`` has been allocated, and runtime PM for it
can not happen yet(either due to disabled/forbidden or its usage_count
> 0). In most cases, driver should call this function before any I/O has
taken place.

This function takes care of setting up using auto suspend for the
device, the autosuspend delay is set to -1 to make runtime suspend
impossible until an updated value is either set by user or by driver.
Drivers do not need to touch other autosuspend settings.

The block layer runtime PM is request based, so only works for drivers
that use request as their IO unit instead of those directly use bio's.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
