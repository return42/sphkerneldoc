.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/mount.c

.. _`tomoyo_audit_mount_log`:

tomoyo_audit_mount_log
======================

.. c:function:: int tomoyo_audit_mount_log(struct tomoyo_request_info *r)

    Audit mount log.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

.. _`tomoyo_audit_mount_log.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_check_mount_acl`:

tomoyo_check_mount_acl
======================

.. c:function:: bool tomoyo_check_mount_acl(struct tomoyo_request_info *r, const struct tomoyo_acl_info *ptr)

    Check permission for path path path number operation.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param const struct tomoyo_acl_info \*ptr:
        Pointer to "struct tomoyo_acl_info".

.. _`tomoyo_check_mount_acl.description`:

Description
-----------

Returns true if granted, false otherwise.

.. _`tomoyo_mount_acl`:

tomoyo_mount_acl
================

.. c:function:: int tomoyo_mount_acl(struct tomoyo_request_info *r, const char *dev_name, const struct path *dir, const char *type, unsigned long flags)

    Check permission for \ :c:func:`mount`\  operation.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param const char \*dev_name:
        Name of device file. Maybe NULL.

    :param const struct path \*dir:
        Pointer to "struct path".

    :param const char \*type:
        Name of filesystem type.

    :param unsigned long flags:
        Mount options.

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

    :param const char \*dev_name:
        Name of device file. Maybe NULL.

    :param const struct path \*path:
        Pointer to "struct path".

    :param const char \*type:
        Name of filesystem type. Maybe NULL.

    :param unsigned long flags:
        Mount options.

    :param void \*data_page:
        Optional data. Maybe NULL.

.. _`tomoyo_mount_permission.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. This file was automatic generated / don't edit.

