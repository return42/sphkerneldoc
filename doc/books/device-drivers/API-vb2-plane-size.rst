
.. _API-vb2-plane-size:

==============
vb2_plane_size
==============

*man vb2_plane_size(9)*

*4.6.0-rc1*

return plane size in bytes


Synopsis
========

.. c:function:: unsigned long vb2_plane_size( struct vb2_buffer * vb, unsigned int plane_no )

Arguments
=========

``vb``
    buffer for which plane size should be returned

``plane_no``
    plane number for which size should be returned
