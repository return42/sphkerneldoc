.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-media-gobj-type:

====================
enum media_gobj_type
====================

*man enum media_gobj_type(9)*

*4.6.0-rc5*

type of a graph object


Synopsis
========

.. code-block:: c

    enum media_gobj_type {
      MEDIA_GRAPH_ENTITY,
      MEDIA_GRAPH_PAD,
      MEDIA_GRAPH_LINK,
      MEDIA_GRAPH_INTF_DEVNODE
    };


Constants
=========

MEDIA_GRAPH_ENTITY
    Identify a media entity

MEDIA_GRAPH_PAD
    Identify a media pad

MEDIA_GRAPH_LINK
    Identify a media link

MEDIA_GRAPH_INTF_DEVNODE
    Identify a media Kernel API interface via a device node


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
