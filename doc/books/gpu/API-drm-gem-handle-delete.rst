
.. _API-drm-gem-handle-delete:

=====================
drm_gem_handle_delete
=====================

*man drm_gem_handle_delete(9)*

*4.6.0-rc1*

deletes the given file-private handle


Synopsis
========

.. c:function:: int drm_gem_handle_delete( struct drm_file * filp, u32 handle )

Arguments
=========

``filp``
    drm file-private structure to use for the handle look up

``handle``
    userspace handle to delete


Description
===========

Removes the GEM handle from the ``filp`` lookup table which has been added with ``drm_gem_handle_create``. If this is the last handle also cleans up linked resources like GEM
names.
