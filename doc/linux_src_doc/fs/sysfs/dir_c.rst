.. -*- coding: utf-8; mode: rst -*-

=====
dir.c
=====


.. _`sysfs_create_dir_ns`:

sysfs_create_dir_ns
===================

.. c:function:: int sysfs_create_dir_ns (struct kobject *kobj, const void *ns)

    create a directory for an object with a namespace tag

    :param struct kobject \*kobj:
        object we're creating directory for

    :param const void \*ns:
        the namespace tag to use



.. _`sysfs_remove_dir`:

sysfs_remove_dir
================

.. c:function:: void sysfs_remove_dir (struct kobject *kobj)

    remove an object's directory.

    :param struct kobject \*kobj:
        object.



.. _`sysfs_remove_dir.description`:

Description
-----------

The only thing special about this is that we remove any files in
the directory before we remove the directory, and we've inlined
what used to be :c:func:`sysfs_rmdir` below, instead of calling separately.



.. _`sysfs_create_mount_point`:

sysfs_create_mount_point
========================

.. c:function:: int sysfs_create_mount_point (struct kobject *parent_kobj, const char *name)

    create an always empty directory

    :param struct kobject \*parent_kobj:
        kobject that will contain this always empty directory

    :param const char \*name:
        The name of the always empty directory to add



.. _`sysfs_remove_mount_point`:

sysfs_remove_mount_point
========================

.. c:function:: void sysfs_remove_mount_point (struct kobject *parent_kobj, const char *name)

    remove an always empty directory.

    :param struct kobject \*parent_kobj:
        kobject that will contain this always empty directory

    :param const char \*name:
        The name of the always empty directory to remove

