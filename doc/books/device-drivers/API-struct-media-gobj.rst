.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-media-gobj:

=================
struct media_gobj
=================

*man struct media_gobj(9)*

*4.6.0-rc5*

Define a graph object.


Synopsis
========

.. code-block:: c

    struct media_gobj {
      struct media_device * mdev;
      u32 id;
      struct list_head list;
    };


Members
=======

mdev
    Pointer to the struct media_device that owns the object

id
    Non-zero object ID identifier. The ID should be unique inside a
    media_device, as it is composed by ``MEDIA_BITS_PER_TYPE`` to store
    the type plus ``MEDIA_BITS_PER_ID`` to store the ID

list
    List entry stored in one of the per-type mdev object lists


Description
===========

All objects on the media graph should have this struct embedded


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
