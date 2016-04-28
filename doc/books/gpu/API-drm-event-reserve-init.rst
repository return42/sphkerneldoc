.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-event-reserve-init:

======================
drm_event_reserve_init
======================

*man drm_event_reserve_init(9)*

*4.6.0-rc5*

init a DRM event and reserve space for it


Synopsis
========

.. c:function:: int drm_event_reserve_init( struct drm_device * dev, struct drm_file * file_priv, struct drm_pending_event * p, struct drm_event * e )

Arguments
=========

``dev``
    DRM device

``file_priv``
    DRM file private data

``p``
    tracking structure for the pending event

``e``
    actual event data to deliver to userspace


Description
===========

This function prepares the passed in event for eventual delivery. If the
event doesn't get delivered (because the IOCTL fails later on, before
queuing up anything) then the even must be cancelled and freed using
``drm_event_cancel_free``. Successfully initialized events should be
sent out using ``drm_send_event`` or ``drm_send_event_locked`` to signal
completion of the asynchronous event to userspace.

If callers embedded ``p`` into a larger structure it must be allocated
with kmalloc and ``p`` must be the first member element.

Callers which already hold dev->event_lock should use
``drm_event_reserve_init`` instead.


RETURNS
=======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
