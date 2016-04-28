.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-mc-create-media-graph:

==========================
v4l2_mc_create_media_graph
==========================

*man v4l2_mc_create_media_graph(9)*

*4.6.0-rc5*

create Media Controller links at the graph.


Synopsis
========

.. c:function:: int v4l2_mc_create_media_graph( struct media_device * mdev )

Arguments
=========

``mdev``
    pointer to the ``media_device`` struct.


Description
===========

Add links between the entities commonly found on PC customer's hardware
at


the V4L2 side
=============

camera sensors, audio and video PLL-IF decoders, tuners, analog TV
decoder and I/O entities (video, VBI and Software Defined Radio).


NOTE
====

webcams are modelled on a very simple way: the sensor is connected
directly to the I/O entity. All dirty details, like scaler and crop HW
are hidden. While such mapping is enough for v4l2 interface centric
PC-consumer's hardware, V4L2 subdev centric camera hardware should not
use this routine, as it will not build the right graph.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
