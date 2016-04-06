
.. _API-drm-gem-prime-fd-to-handle:

==========================
drm_gem_prime_fd_to_handle
==========================

*man drm_gem_prime_fd_to_handle(9)*

*4.6.0-rc1*

PRIME import function for GEM drivers


Synopsis
========

.. c:function:: int drm_gem_prime_fd_to_handle( struct drm_device * dev, struct drm_file * file_priv, int prime_fd, uint32_t * handle )

Arguments
=========

``dev``
    dev to export the buffer from

``file_priv``
    drm file-private structure

``prime_fd``
    fd id of the dma-buf which should be imported

``handle``
    pointer to storage for the handle of the imported buffer object


Description
===========

This is the PRIME import function which must be used mandatorily by GEM drivers to ensure correct lifetime management of the underlying GEM object. The actual importing of GEM
object from the dma-buf is done through the gem_import_export driver callback.
