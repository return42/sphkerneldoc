
.. _API-v4l-enable-media-source:

=======================
v4l_enable_media_source
=======================

*man v4l_enable_media_source(9)*

*4.6.0-rc1*

Hold media source for exclusive use if free


Synopsis
========

.. c:function:: int v4l_enable_media_source( struct video_device * vdev )

Arguments
=========

``vdev``
    pointer to struct video_device


Description
===========

This interface calls enable_source handler to determine if media source is free for use. The enable_source handler is responsible for checking is the media source is free and
start a pipeline between the media source and the media entity associated with the video device. This interface should be called from v4l2-core and dvb-core interfaces that change
the source configuration.


Return
======

returns zero on success or a negative error code.
