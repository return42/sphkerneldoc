
.. _API-vb2-get-plane-payload:

=====================
vb2_get_plane_payload
=====================

*man vb2_get_plane_payload(9)*

*4.6.0-rc1*

get bytesused for the plane plane_no


Synopsis
========

.. c:function:: unsigned long vb2_get_plane_payload( struct vb2_buffer * vb, unsigned int plane_no )

Arguments
=========

``vb``
    buffer for which plane payload should be set

``plane_no``
    plane number for which payload should be set
