
.. _API-drm-gem-prime-handle-to-fd:

==========================
drm_gem_prime_handle_to_fd
==========================

*man drm_gem_prime_handle_to_fd(9)*

*4.6.0-rc1*

PRIME export function for GEM drivers


Synopsis
========

.. c:function:: int drm_gem_prime_handle_to_fd( struct drm_device * dev, struct drm_file * file_priv, uint32_t handle, uint32_t flags, int * prime_fd )

Arguments
=========

``dev``
    dev to export the buffer from

``file_priv``
    drm file-private structure

``handle``
    buffer handle to export

``flags``
    flags like DRM_CLOEXEC

``prime_fd``
    pointer to storage for the fd id of the create dma-buf


Description
===========

This is the PRIME export function which must be used mandatorily by GEM drivers to ensure correct lifetime management of the underlying GEM object. The actual exporting from GEM
object to a dma-buf is done through the gem_prime_export driver callback.
