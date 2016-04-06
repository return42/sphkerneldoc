
.. _API-drm-framebuffer-lookup:

======================
drm_framebuffer_lookup
======================

*man drm_framebuffer_lookup(9)*

*4.6.0-rc1*

look up a drm framebuffer and grab a reference


Synopsis
========

.. c:function:: struct drm_framebuffer ⋆ drm_framebuffer_lookup( struct drm_device * dev, uint32_t id )

Arguments
=========

``dev``
    drm device

``id``
    id of the fb object


Description
===========

If successful, this grabs an additional reference to the framebuffer - callers need to make sure to eventually unreference the returned framebuffer again, using
``drm_framebuffer_unreference``.
