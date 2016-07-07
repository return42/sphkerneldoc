.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/memory.c

.. _`tomoyo_warn_oom`:

tomoyo_warn_oom
===============

.. c:function:: void tomoyo_warn_oom(const char *function)

    Print out of memory warning message.

    :param const char \*function:
        Function's name.

.. _`tomoyo_memory_ok`:

tomoyo_memory_ok
================

.. c:function:: bool tomoyo_memory_ok(void *ptr)

    Check memory quota.

    :param void \*ptr:
        Pointer to allocated memory.

.. _`tomoyo_memory_ok.description`:

Description
-----------

Returns true on success, false otherwise.

Returns true if \ ``ptr``\  is not NULL and quota not exceeded, false otherwise.

Caller holds tomoyo_policy_lock mutex.

.. _`tomoyo_commit_ok`:

tomoyo_commit_ok
================

.. c:function:: void *tomoyo_commit_ok(void *data, const unsigned int size)

    Check memory quota.

    :param void \*data:
        Data to copy from.

    :param const unsigned int size:
        Size in byte.

.. _`tomoyo_commit_ok.description`:

Description
-----------

Returns pointer to allocated memory on success, NULL otherwise.
\ ``data``\  is zero-cleared on success.

Caller holds tomoyo_policy_lock mutex.

.. _`tomoyo_get_group`:

tomoyo_get_group
================

.. c:function:: struct tomoyo_group *tomoyo_get_group(struct tomoyo_acl_param *param, const u8 idx)

    Allocate memory for "struct tomoyo_path_group"/"struct tomoyo_number_group".

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

    :param const u8 idx:
        Index number.

.. _`tomoyo_get_group.description`:

Description
-----------

Returns pointer to "struct tomoyo_group" on success, NULL otherwise.

.. _`tomoyo_get_name`:

tomoyo_get_name
===============

.. c:function:: const struct tomoyo_path_info *tomoyo_get_name(const char *name)

    Allocate permanent memory for string data.

    :param const char \*name:
        The string to store into the permernent memory.

.. _`tomoyo_get_name.description`:

Description
-----------

Returns pointer to "struct tomoyo_path_info" on success, NULL otherwise.

.. _`tomoyo_mm_init`:

tomoyo_mm_init
==============

.. c:function:: void tomoyo_mm_init( void)

    Initialize mm related code.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

