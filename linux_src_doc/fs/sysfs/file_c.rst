.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/sysfs/file.c

.. _`sysfs_create_file_ns`:

sysfs_create_file_ns
====================

.. c:function:: int sysfs_create_file_ns(struct kobject *kobj, const struct attribute *attr, const void *ns)

    create an attribute file for an object with custom ns

    :param kobj:
        object we're creating for
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor
    :type attr: const struct attribute \*

    :param ns:
        namespace the new file should belong to
    :type ns: const void \*

.. _`sysfs_add_file_to_group`:

sysfs_add_file_to_group
=======================

.. c:function:: int sysfs_add_file_to_group(struct kobject *kobj, const struct attribute *attr, const char *group)

    add an attribute file to a pre-existing group.

    :param kobj:
        object we're acting for.
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor.
    :type attr: const struct attribute \*

    :param group:
        group name.
    :type group: const char \*

.. _`sysfs_chmod_file`:

sysfs_chmod_file
================

.. c:function:: int sysfs_chmod_file(struct kobject *kobj, const struct attribute *attr, umode_t mode)

    update the modified mode value on an object attribute.

    :param kobj:
        object we're acting for.
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor.
    :type attr: const struct attribute \*

    :param mode:
        file permissions.
    :type mode: umode_t

.. _`sysfs_break_active_protection`:

sysfs_break_active_protection
=============================

.. c:function:: struct kernfs_node *sysfs_break_active_protection(struct kobject *kobj, const struct attribute *attr)

    break "active" protection

    :param kobj:
        The kernel object \ ``attr``\  is associated with.
    :type kobj: struct kobject \*

    :param attr:
        The attribute to break the "active" protection for.
    :type attr: const struct attribute \*

.. _`sysfs_break_active_protection.description`:

Description
-----------

With sysfs, just like kernfs, deletion of an attribute is postponed until
all active .show() and .store() callbacks have finished unless this function
is called. Hence this function is useful in methods that implement self
deletion.

.. _`sysfs_unbreak_active_protection`:

sysfs_unbreak_active_protection
===============================

.. c:function:: void sysfs_unbreak_active_protection(struct kernfs_node *kn)

    restore "active" protection

    :param kn:
        Pointer returned by \ :c:func:`sysfs_break_active_protection`\ .
    :type kn: struct kernfs_node \*

.. _`sysfs_unbreak_active_protection.description`:

Description
-----------

Undo the effects of \ :c:func:`sysfs_break_active_protection`\ . Since this function
calls \ :c:func:`kernfs_put`\  on the kernfs node that corresponds to the 'attr'
argument passed to \ :c:func:`sysfs_break_active_protection`\  that attribute may have
been removed between the \ :c:func:`sysfs_break_active_protection`\  and
\ :c:func:`sysfs_unbreak_active_protection`\  calls, it is not safe to access \ ``kn``\  after
this function has returned.

.. _`sysfs_remove_file_ns`:

sysfs_remove_file_ns
====================

.. c:function:: void sysfs_remove_file_ns(struct kobject *kobj, const struct attribute *attr, const void *ns)

    remove an object attribute with a custom ns tag

    :param kobj:
        object we're acting for
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor
    :type attr: const struct attribute \*

    :param ns:
        namespace tag of the file to remove
    :type ns: const void \*

.. _`sysfs_remove_file_ns.description`:

Description
-----------

Hash the attribute name and namespace tag and kill the victim.

.. _`sysfs_remove_file_self`:

sysfs_remove_file_self
======================

.. c:function:: bool sysfs_remove_file_self(struct kobject *kobj, const struct attribute *attr)

    remove an object attribute from its own method

    :param kobj:
        object we're acting for
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor
    :type attr: const struct attribute \*

.. _`sysfs_remove_file_self.description`:

Description
-----------

See \ :c:func:`kernfs_remove_self`\  for details.

.. _`sysfs_remove_file_from_group`:

sysfs_remove_file_from_group
============================

.. c:function:: void sysfs_remove_file_from_group(struct kobject *kobj, const struct attribute *attr, const char *group)

    remove an attribute file from a group.

    :param kobj:
        object we're acting for.
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor.
    :type attr: const struct attribute \*

    :param group:
        group name.
    :type group: const char \*

.. _`sysfs_create_bin_file`:

sysfs_create_bin_file
=====================

.. c:function:: int sysfs_create_bin_file(struct kobject *kobj, const struct bin_attribute *attr)

    create binary file for object.

    :param kobj:
        object.
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor.
    :type attr: const struct bin_attribute \*

.. _`sysfs_remove_bin_file`:

sysfs_remove_bin_file
=====================

.. c:function:: void sysfs_remove_bin_file(struct kobject *kobj, const struct bin_attribute *attr)

    remove binary file for object.

    :param kobj:
        object.
    :type kobj: struct kobject \*

    :param attr:
        attribute descriptor.
    :type attr: const struct bin_attribute \*

.. This file was automatic generated / don't edit.

