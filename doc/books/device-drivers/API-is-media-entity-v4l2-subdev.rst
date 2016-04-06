
.. _API-is-media-entity-v4l2-subdev:

===========================
is_media_entity_v4l2_subdev
===========================

*man is_media_entity_v4l2_subdev(9)*

*4.6.0-rc1*

return true if the entity main function is associated with the V4L2 API subdev usage


Synopsis
========

.. c:function:: bool is_media_entity_v4l2_subdev( struct media_entity * entity )

Arguments
=========

``entity``
    pointer to entity


Description
===========

This is an ancillary function used by subdev-based V4L2 drivers. It checks if the entity function is one of functions used by a V4L2 subdev, e. g. camera-relatef functions, analog
TV decoder, TV tuner, V4L2 DSPs.
