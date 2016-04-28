.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l-disable-media-source:

========================
v4l_disable_media_source
========================

*man v4l_disable_media_source(9)*

*4.6.0-rc5*

Release media source


Synopsis
========

.. c:function:: void v4l_disable_media_source( struct video_device * vdev )

Arguments
=========

``vdev``
    pointer to struct video_device


Description
===========

This interface calls disable_source handler to release the media
source. The disable_source handler stops the active media pipeline
between the media source and the media entity associated with the video
device.


Return
======

returns zero on success or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
