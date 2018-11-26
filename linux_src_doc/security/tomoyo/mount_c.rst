.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/mount.c

.. _`tomoyo_audit_mount_log`:

tomoyo_audit_mount_log
======================

.. c:function:: int tomoyo_audit_mount_log(struct tomoyo_request_info *r)

    Audit mount log.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

.. _`tomoyo_audit_mount_log.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_check_mount_acl`:

tomoyo_check_mount_acl
======================

.. c:function:: bool tomoyo_check_mount_acl(struct tomoyo_request_info *r, const struct tomoyo_acl_info *ptr)

    Check permission for path path path number operation.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param ptr:
        Pointer to "struct tomoyo_acl_info".
    :type ptr: const struct tomoyo_acl_info \*

.. _`tomoyo_check_mount_acl.description`:

Description
-----------

Returns true if granted, false otherwise.

.. _`tomoyo_mount_acl`:

tomoyo_mount_acl
================

.. c:function:: int tomoyo_mount_acl(struct tomoyo_request_info *r, const char *dev_name, const struct path *dir, const char *type, unsigned long flags)

    Check permission for \ :c:func:`mount`\  operation.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param dev_name:
        Name of device file. Maybe NULL.
    :type dev_name: const char \*

    :param dir:
        Pointer to "struct path".
    :type dir: const struct path \*

    :param type:
        Name of filesystem type.
    :type type: const char \*

    :param flags:
        Mount options.
    :type flags: unsigned long

.. _`tomoyo_mount_acl.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_mount_permission`:

tomoyo_mount_permission
=======================

.. c:function:: int tomoyo_mount_permission(const char *dev_name, const struct path *path, const char *type, unsigned long flags, void *data_page)

    Check permission for \ :c:func:`mount`\  operation.

    :param dev_name:
        Name of device file. Maybe NULL.
    :type dev_name: const char \*

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

    :param type:
        Name of filesystem type. Maybe NULL.
    :type type: const char \*

    :param flags:
        Mount options.
    :type flags: unsigned long

    :param data_page:
        Optional data. Maybe NULL.
    :type data_page: void \*

.. _`tomoyo_mount_permission.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. This file was automatic generated / don't edit.

