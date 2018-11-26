.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/environ.c

.. _`tomoyo_check_env_acl`:

tomoyo_check_env_acl
====================

.. c:function:: bool tomoyo_check_env_acl(struct tomoyo_request_info *r, const struct tomoyo_acl_info *ptr)

    Check permission for environment variable's name.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param ptr:
        Pointer to "struct tomoyo_acl_info".
    :type ptr: const struct tomoyo_acl_info \*

.. _`tomoyo_check_env_acl.description`:

Description
-----------

Returns true if granted, false otherwise.

.. _`tomoyo_audit_env_log`:

tomoyo_audit_env_log
====================

.. c:function:: int tomoyo_audit_env_log(struct tomoyo_request_info *r)

    Audit environment variable name log.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

.. _`tomoyo_audit_env_log.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_env_perm`:

tomoyo_env_perm
===============

.. c:function:: int tomoyo_env_perm(struct tomoyo_request_info *r, const char *env)

    Check permission for environment variable's name.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param env:
        The name of environment variable.
    :type env: const char \*

.. _`tomoyo_env_perm.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_same_env_acl`:

tomoyo_same_env_acl
===================

.. c:function:: bool tomoyo_same_env_acl(const struct tomoyo_acl_info *a, const struct tomoyo_acl_info *b)

    Check for duplicated "struct tomoyo_env_acl" entry.

    :param a:
        Pointer to "struct tomoyo_acl_info".
    :type a: const struct tomoyo_acl_info \*

    :param b:
        Pointer to "struct tomoyo_acl_info".
    :type b: const struct tomoyo_acl_info \*

.. _`tomoyo_same_env_acl.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_write_env`:

tomoyo_write_env
================

.. c:function:: int tomoyo_write_env(struct tomoyo_acl_param *param)

    Write "struct tomoyo_env_acl" list.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

.. _`tomoyo_write_env.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_write_misc`:

tomoyo_write_misc
=================

.. c:function:: int tomoyo_write_misc(struct tomoyo_acl_param *param)

    Update environment variable list.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

.. _`tomoyo_write_misc.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. This file was automatic generated / don't edit.

