.. -*- coding: utf-8; mode: rst -*-

.. _API-media-gobj-destroy:

==================
media_gobj_destroy
==================

*man media_gobj_destroy(9)*

*4.6.0-rc5*

Stop using a graph object on a media device


Synopsis
========

.. c:function:: void media_gobj_destroy( struct media_gobj * gobj )

Arguments
=========

``gobj``
    Pointer to the graph object


Description
===========

This should be called by all routines like ``media_device_unregister``
that remove/destroy media graph objects.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
