.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/common.h

.. _`tomoyo_read_lock`:

tomoyo_read_lock
================

.. c:function:: int tomoyo_read_lock( void)

    Take lock for protecting policy.

    :param  void:
        no arguments

.. _`tomoyo_read_lock.description`:

Description
-----------

Returns index number for \ :c:func:`tomoyo_read_unlock`\ .

.. _`tomoyo_read_unlock`:

tomoyo_read_unlock
==================

.. c:function:: void tomoyo_read_unlock(int idx)

    Release lock for protecting policy.

    :param int idx:
        Index number returned by \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_read_unlock.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_sys_getppid`:

tomoyo_sys_getppid
==================

.. c:function:: pid_t tomoyo_sys_getppid( void)

    Copy of \ :c:func:`getppid`\ .

    :param  void:
        no arguments

.. _`tomoyo_sys_getppid.description`:

Description
-----------

Returns parent process's PID.

Alpha does not have \ :c:func:`getppid`\  defined. To be able to build this module on
Alpha, I have to copy \ :c:func:`getppid`\  from kernel/timer.c.

.. _`tomoyo_sys_getpid`:

tomoyo_sys_getpid
=================

.. c:function:: pid_t tomoyo_sys_getpid( void)

    Copy of \ :c:func:`getpid`\ .

    :param  void:
        no arguments

.. _`tomoyo_sys_getpid.description`:

Description
-----------

Returns current thread's PID.

Alpha does not have \ :c:func:`getpid`\  defined. To be able to build this module on
Alpha, I have to copy \ :c:func:`getpid`\  from kernel/timer.c.

.. _`tomoyo_pathcmp`:

tomoyo_pathcmp
==============

.. c:function:: bool tomoyo_pathcmp(const struct tomoyo_path_info *a, const struct tomoyo_path_info *b)

    \ :c:func:`strcmp`\  for "struct tomoyo_path_info" structure.

    :param const struct tomoyo_path_info \*a:
        Pointer to "struct tomoyo_path_info".

    :param const struct tomoyo_path_info \*b:
        Pointer to "struct tomoyo_path_info".

.. _`tomoyo_pathcmp.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_put_name`:

tomoyo_put_name
===============

.. c:function:: void tomoyo_put_name(const struct tomoyo_path_info *name)

    Drop reference on "struct tomoyo_name".

    :param const struct tomoyo_path_info \*name:
        Pointer to "struct tomoyo_path_info". Maybe NULL.

.. _`tomoyo_put_name.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_put_condition`:

tomoyo_put_condition
====================

.. c:function:: void tomoyo_put_condition(struct tomoyo_condition *cond)

    Drop reference on "struct tomoyo_condition".

    :param struct tomoyo_condition \*cond:
        Pointer to "struct tomoyo_condition". Maybe NULL.

.. _`tomoyo_put_condition.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_put_group`:

tomoyo_put_group
================

.. c:function:: void tomoyo_put_group(struct tomoyo_group *group)

    Drop reference on "struct tomoyo_group".

    :param struct tomoyo_group \*group:
        Pointer to "struct tomoyo_group". Maybe NULL.

.. _`tomoyo_put_group.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_domain`:

tomoyo_domain
=============

.. c:function:: struct tomoyo_domain_info *tomoyo_domain( void)

    Get "struct tomoyo_domain_info" for current thread.

    :param  void:
        no arguments

.. _`tomoyo_domain.description`:

Description
-----------

Returns pointer to "struct tomoyo_domain_info" for current thread.

.. _`tomoyo_real_domain`:

tomoyo_real_domain
==================

.. c:function:: struct tomoyo_domain_info *tomoyo_real_domain(struct task_struct *task)

    Get "struct tomoyo_domain_info" for specified thread.

    :param struct task_struct \*task:
        Pointer to "struct task_struct".

.. _`tomoyo_real_domain.description`:

Description
-----------

Returns pointer to "struct tomoyo_security" for specified thread.

.. _`tomoyo_same_name_union`:

tomoyo_same_name_union
======================

.. c:function:: bool tomoyo_same_name_union(const struct tomoyo_name_union *a, const struct tomoyo_name_union *b)

    Check for duplicated "struct tomoyo_name_union" entry.

    :param const struct tomoyo_name_union \*a:
        Pointer to "struct tomoyo_name_union".

    :param const struct tomoyo_name_union \*b:
        Pointer to "struct tomoyo_name_union".

.. _`tomoyo_same_name_union.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_same_number_union`:

tomoyo_same_number_union
========================

.. c:function:: bool tomoyo_same_number_union(const struct tomoyo_number_union *a, const struct tomoyo_number_union *b)

    Check for duplicated "struct tomoyo_number_union" entry.

    :param const struct tomoyo_number_union \*a:
        Pointer to "struct tomoyo_number_union".

    :param const struct tomoyo_number_union \*b:
        Pointer to "struct tomoyo_number_union".

.. _`tomoyo_same_number_union.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_same_ipaddr_union`:

tomoyo_same_ipaddr_union
========================

.. c:function:: bool tomoyo_same_ipaddr_union(const struct tomoyo_ipaddr_union *a, const struct tomoyo_ipaddr_union *b)

    Check for duplicated "struct tomoyo_ipaddr_union" entry.

    :param const struct tomoyo_ipaddr_union \*a:
        Pointer to "struct tomoyo_ipaddr_union".

    :param const struct tomoyo_ipaddr_union \*b:
        Pointer to "struct tomoyo_ipaddr_union".

.. _`tomoyo_same_ipaddr_union.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_current_namespace`:

tomoyo_current_namespace
========================

.. c:function:: struct tomoyo_policy_namespace *tomoyo_current_namespace( void)

    Get "struct tomoyo_policy_namespace" for current thread.

    :param  void:
        no arguments

.. _`tomoyo_current_namespace.description`:

Description
-----------

Returns pointer to "struct tomoyo_policy_namespace" for current thread.

.. _`tomoyo_round2`:

tomoyo_round2
=============

.. c:function:: int tomoyo_round2(size_t size)

    Round up to power of 2 for calculating memory usage.

    :param size_t size:
        Size to be rounded up.

.. _`tomoyo_round2.description`:

Description
-----------

Returns \ ``size``\ .

Since SLOB does not round up, this function simply returns \ ``size``\ .

.. _`tomoyo_round2`:

tomoyo_round2
=============

.. c:function:: int tomoyo_round2(size_t size)

    Round up to power of 2 for calculating memory usage.

    :param size_t size:
        Size to be rounded up.

.. _`tomoyo_round2.description`:

Description
-----------

Returns rounded size.

Strictly speaking, SLAB may be able to allocate (e.g.) 96 bytes instead of
(e.g.) 128 bytes.

.. _`list_for_each_cookie`:

list_for_each_cookie
====================

.. c:function::  list_for_each_cookie( pos,  head)

    iterate over a list with cookie.

    :param  pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.

    :param  head:
        the head for your list.

.. This file was automatic generated / don't edit.

