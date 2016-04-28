.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-pipeline-link-notify:

=========================
v4l2_pipeline_link_notify
=========================

*man v4l2_pipeline_link_notify(9)*

*4.6.0-rc5*

Link management notification callback


Synopsis
========

.. c:function:: int v4l2_pipeline_link_notify( struct media_link * link, u32 flags, unsigned int notification )

Arguments
=========

``link``
    The link

``flags``
    New link flags that will be applied

``notification``
    The link's state change notification type (MEDIA_DEV_NOTIFY_*)


Description
===========

React to link management on powered pipelines by updating the use count
of all entities in the source and sink sides of the link. Entities are
powered on or off accordingly. The use of this function should be paired
with ``v4l2_pipeline_pm_use``.

Return 0 on success or a negative error code on failure. Powering
entities off is assumed to never fail. This function will not fail for
disconnection events.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
