.. -*- coding: utf-8; mode: rst -*-

.. _API-is-media-entity-v4l2-io:

=======================
is_media_entity_v4l2_io
=======================

*man is_media_entity_v4l2_io(9)*

*4.6.0-rc5*

identify if the entity main function is a V4L2 I/O


Synopsis
========

.. c:function:: bool is_media_entity_v4l2_io( struct media_entity * entity )

Arguments
=========

``entity``
    pointer to entity


Return
======

true if the entity main function is one of the V4L2 I/O types (video,
VBI or SDR radio); false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
