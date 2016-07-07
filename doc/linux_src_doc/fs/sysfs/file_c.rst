.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/sysfs/file.c

.. _`sysfs_create_file_ns`:

sysfs_create_file_ns
====================

.. c:function:: int sysfs_create_file_ns(struct kobject *kobj, const struct attribute *attr, const void *ns)

    create an attribute file for an object with custom ns

    :param struct kobject \*kobj:
        object we're creating for

    :param const struct attribute \*attr:
        attribute descriptor

    :param const void \*ns:
        namespace the new file should belong to

.. _`sysfs_add_file_to_group`:

sysfs_add_file_to_group
=======================

.. c:function:: int sysfs_add_file_to_group(struct kobject *kobj, const struct attribute *attr, const char *group)

    add an attribute file to a pre-existing group.

    :param struct kobject \*kobj:
        object we're acting for.

    :param const struct attribute \*attr:
        attribute descriptor.

    :param const char \*group:
        group name.

.. _`sysfs_chmod_file`:

sysfs_chmod_file
================

.. c:function:: int sysfs_chmod_file(struct kobject *kobj, const struct attribute *attr, umode_t mode)

    update the modified mode value on an object attribute.

    :param struct kobject \*kobj:
        object we're acting for.

    :param const struct attribute \*attr:
        attribute descriptor.

    :param umode_t mode:
        file permissions.

.. _`sysfs_remove_file_ns`:

sysfs_remove_file_ns
====================

.. c:function:: void sysfs_remove_file_ns(struct kobject *kobj, const struct attribute *attr, const void *ns)

    remove an object attribute with a custom ns tag

    :param struct kobject \*kobj:
        object we're acting for

    :param const struct attribute \*attr:
        attribute descriptor

    :param const void \*ns:
        namespace tag of the file to remove

.. _`sysfs_remove_file_ns.description`:

Description
-----------

Hash the attribute name and namespace tag and kill the victim.

.. _`sysfs_remove_file_self`:

sysfs_remove_file_self
======================

.. c:function:: bool sysfs_remove_file_self(struct kobject *kobj, const struct attribute *attr)

    remove an object attribute from its own method

    :param struct kobject \*kobj:
        object we're acting for

    :param const struct attribute \*attr:
        attribute descriptor

.. _`sysfs_remove_file_self.description`:

Description
-----------

See \ :c:func:`kernfs_remove_self`\  for details.

.. _`sysfs_remove_file_from_group`:

sysfs_remove_file_from_group
============================

.. c:function:: void sysfs_remove_file_from_group(struct kobject *kobj, const struct attribute *attr, const char *group)

    remove an attribute file from a group.

    :param struct kobject \*kobj:
        object we're acting for.

    :param const struct attribute \*attr:
        attribute descriptor.

    :param const char \*group:
        group name.

.. _`sysfs_create_bin_file`:

sysfs_create_bin_file
=====================

.. c:function:: int sysfs_create_bin_file(struct kobject *kobj, const struct bin_attribute *attr)

    create binary file for object.

    :param struct kobject \*kobj:
        object.

    :param const struct bin_attribute \*attr:
        attribute descriptor.

.. _`sysfs_remove_bin_file`:

sysfs_remove_bin_file
=====================

.. c:function:: void sysfs_remove_bin_file(struct kobject *kobj, const struct bin_attribute *attr)

    remove binary file for object.

    :param struct kobject \*kobj:
        object.

    :param const struct bin_attribute \*attr:
        attribute descriptor.

.. This file was automatic generated / don't edit.

