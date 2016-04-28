.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-format-plane-width:

======================
drm_format_plane_width
======================

*man drm_format_plane_width(9)*

*4.6.0-rc5*

width of the plane given the first plane


Synopsis
========

.. c:function:: int drm_format_plane_width( int width, uint32_t format, int plane )

Arguments
=========

``width``
    width of the first plane

``format``
    pixel format

``plane``
    plane index


Returns
=======

The width of ``plane``, given that the width of the first plane is
``width``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
