.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_debugfs.c

.. _`drm_debugfs_create_files`:

drm_debugfs_create_files
========================

.. c:function:: int drm_debugfs_create_files(const struct drm_info_list *files, int count, struct dentry *root, struct drm_minor *minor)

    Initialize a given set of debugfs files for DRM minor

    :param files:
        The array of files to create
    :type files: const struct drm_info_list \*

    :param count:
        The number of files given
    :type count: int

    :param root:
        DRI debugfs dir entry.
    :type root: struct dentry \*

    :param minor:
        device minor number
    :type minor: struct drm_minor \*

.. _`drm_debugfs_create_files.description`:

Description
-----------

Create a given set of debugfs files represented by an array of
\ :c:type:`struct drm_info_list <drm_info_list>`\  in the given root directory. These files will be removed
automatically on \ :c:func:`drm_debugfs_cleanup`\ .

.. This file was automatic generated / don't edit.

