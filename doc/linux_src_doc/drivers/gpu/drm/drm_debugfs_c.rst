.. -*- coding: utf-8; mode: rst -*-

=============
drm_debugfs.c
=============


.. _`drm_debugfs_create_files`:

drm_debugfs_create_files
========================

.. c:function:: int drm_debugfs_create_files (const struct drm_info_list *files, int count, struct dentry *root, struct drm_minor *minor)

    :param const struct drm_info_list \*files:

        *undescribed*

    :param int count:

        *undescribed*

    :param struct dentry \*root:

        *undescribed*

    :param struct drm_minor \*minor:

        *undescribed*



.. _`drm_debugfs_create_files.description`:

Description
-----------


\param files The array of files to create
\param count The number of files given
\param root DRI debugfs dir entry.
\param minor device minor number
\return Zero on success, non-zero on failure

Create a given set of debugfs files represented by an array of
gdm_debugfs_lists in the given root directory.



.. _`drm_debugfs_init`:

drm_debugfs_init
================

.. c:function:: int drm_debugfs_init (struct drm_minor *minor, int minor_id, struct dentry *root)

    :param struct drm_minor \*minor:

        *undescribed*

    :param int minor_id:

        *undescribed*

    :param struct dentry \*root:

        *undescribed*



.. _`drm_debugfs_init.description`:

Description
-----------


\param dev DRM device
\param minor device minor number
\param root DRI debugfs dir entry.

Create the DRI debugfs root entry "/sys/kernel/debug/dri", the device debugfs root entry
"/sys/kernel/debug/dri/\ ``minor``\ %/", and each entry in debugfs_list as
"/sys/kernel/debug/dri/\ ``minor``\ %/\ ``name``\ %".



.. _`drm_debugfs_remove_files`:

drm_debugfs_remove_files
========================

.. c:function:: int drm_debugfs_remove_files (const struct drm_info_list *files, int count, struct drm_minor *minor)

    :param const struct drm_info_list \*files:

        *undescribed*

    :param int count:

        *undescribed*

    :param struct drm_minor \*minor:

        *undescribed*



.. _`drm_debugfs_remove_files.description`:

Description
-----------


\param files The list of files
\param count The number of files
\param minor The minor of which we should remove the files
\return always zero.

Remove all debugfs entries created by :c:func:`debugfs_init`.



.. _`drm_debugfs_cleanup`:

drm_debugfs_cleanup
===================

.. c:function:: int drm_debugfs_cleanup (struct drm_minor *minor)

    :param struct drm_minor \*minor:

        *undescribed*



.. _`drm_debugfs_cleanup.description`:

Description
-----------


\param minor device minor number.
\return always zero.

Remove all debugfs entries created by :c:func:`debugfs_init`.

