.. -*- coding: utf-8; mode: rst -*-

.. _API-vb2-set-plane-payload:

=====================
vb2_set_plane_payload
=====================

*man vb2_set_plane_payload(9)*

*4.6.0-rc5*

set bytesused for the plane plane_no


Synopsis
========

.. c:function:: void vb2_set_plane_payload( struct vb2_buffer * vb, unsigned int plane_no, unsigned long size )

Arguments
=========

``vb``
    buffer for which plane payload should be set

``plane_no``
    plane number for which payload should be set

``size``
    payload in bytes


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
