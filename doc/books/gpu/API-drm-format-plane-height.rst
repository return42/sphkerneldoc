
.. _API-drm-format-plane-height:

=======================
drm_format_plane_height
=======================

*man drm_format_plane_height(9)*

*4.6.0-rc1*

height of the plane given the first plane


Synopsis
========

.. c:function:: int drm_format_plane_height( int height, uint32_t format, int plane )

Arguments
=========

``height``
    height of the first plane

``format``
    pixel format

``plane``
    plane index


Returns
=======

The height of ``plane``, given that the height of the first plane is ``height``.
