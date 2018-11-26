.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/sysfs/dir.c

.. _`sysfs_create_dir_ns`:

sysfs_create_dir_ns
===================

.. c:function:: int sysfs_create_dir_ns(struct kobject *kobj, const void *ns)

    create a directory for an object with a namespace tag

    :param kobj:
        object we're creating directory for
    :type kobj: struct kobject \*

    :param ns:
        the namespace tag to use
    :type ns: const void \*

.. _`sysfs_remove_dir`:

sysfs_remove_dir
================

.. c:function:: void sysfs_remove_dir(struct kobject *kobj)

    remove an object's directory.

    :param kobj:
        object.
    :type kobj: struct kobject \*

.. _`sysfs_remove_dir.description`:

Description
-----------

The only thing special about this is that we remove any files in
the directory before we remove the directory, and we've inlined
what used to be \ :c:func:`sysfs_rmdir`\  below, instead of calling separately.

.. _`sysfs_create_mount_point`:

sysfs_create_mount_point
========================

.. c:function:: int sysfs_create_mount_point(struct kobject *parent_kobj, const char *name)

    create an always empty directory

    :param parent_kobj:
        kobject that will contain this always empty directory
    :type parent_kobj: struct kobject \*

    :param name:
        The name of the always empty directory to add
    :type name: const char \*

.. _`sysfs_remove_mount_point`:

sysfs_remove_mount_point
========================

.. c:function:: void sysfs_remove_mount_point(struct kobject *parent_kobj, const char *name)

    remove an always empty directory.

    :param parent_kobj:
        kobject that will contain this always empty directory
    :type parent_kobj: struct kobject \*

    :param name:
        The name of the always empty directory to remove
    :type name: const char \*

.. This file was automatic generated / don't edit.

