.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/domain.c

.. _`tomoyo_update_policy`:

tomoyo_update_policy
====================

.. c:function:: int tomoyo_update_policy(struct tomoyo_acl_head *new_entry, const int size, struct tomoyo_acl_param *param, bool (*check_duplicate)(const struct tomoyo_acl_head *, const struct tomoyo_acl_head *))

    Update an entry for exception policy.

    :param struct tomoyo_acl_head \*new_entry:
        Pointer to "struct tomoyo_acl_info".

    :param const int size:
        Size of \ ``new_entry``\  in bytes.

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

    :param bool (\*check_duplicate)(const struct tomoyo_acl_head \*, const struct tomoyo_acl_head \*):
        Callback function to find duplicated entry.

.. _`tomoyo_update_policy.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_same_acl_head`:

tomoyo_same_acl_head
====================

.. c:function:: bool tomoyo_same_acl_head(const struct tomoyo_acl_info *a, const struct tomoyo_acl_info *b)

    Check for duplicated "struct tomoyo_acl_info" entry.

    :param const struct tomoyo_acl_info \*a:
        Pointer to "struct tomoyo_acl_info".

    :param const struct tomoyo_acl_info \*b:
        Pointer to "struct tomoyo_acl_info".

.. _`tomoyo_same_acl_head.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_update_domain`:

tomoyo_update_domain
====================

.. c:function:: int tomoyo_update_domain(struct tomoyo_acl_info *new_entry, const int size, struct tomoyo_acl_param *param, bool (*check_duplicate)(const struct tomoyo_acl_info *, const struct tomoyo_acl_info *), bool (*merge_duplicate)(struct tomoyo_acl_info *, struct tomoyo_acl_info *, const bool))

    Update an entry for domain policy.

    :param struct tomoyo_acl_info \*new_entry:
        Pointer to "struct tomoyo_acl_info".

    :param const int size:
        Size of \ ``new_entry``\  in bytes.

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

    :param bool (\*check_duplicate)(const struct tomoyo_acl_info \*, const struct tomoyo_acl_info \*):
        Callback function to find duplicated entry.

    :param bool (\*merge_duplicate)(struct tomoyo_acl_info \*, struct tomoyo_acl_info \*, const bool):
        Callback function to merge duplicated entry.

.. _`tomoyo_update_domain.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_check_acl`:

tomoyo_check_acl
================

.. c:function:: void tomoyo_check_acl(struct tomoyo_request_info *r, bool (*check_entry)(struct tomoyo_request_info *, const struct tomoyo_acl_info *))

    Do permission check.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param bool (\*check_entry)(struct tomoyo_request_info \*, const struct tomoyo_acl_info \*):
        Callback function to check type specific parameters.

.. _`tomoyo_check_acl.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_last_word`:

tomoyo_last_word
================

.. c:function:: const char *tomoyo_last_word(const char *name)

    Get last component of a domainname.

    :param const char \*name:
        Domainname to check.

.. _`tomoyo_last_word.description`:

Description
-----------

Returns the last word of \ ``domainname``\ .

.. _`tomoyo_same_transition_control`:

tomoyo_same_transition_control
==============================

.. c:function:: bool tomoyo_same_transition_control(const struct tomoyo_acl_head *a, const struct tomoyo_acl_head *b)

    Check for duplicated "struct tomoyo_transition_control" entry.

    :param const struct tomoyo_acl_head \*a:
        Pointer to "struct tomoyo_acl_head".

    :param const struct tomoyo_acl_head \*b:
        Pointer to "struct tomoyo_acl_head".

.. _`tomoyo_same_transition_control.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_write_transition_control`:

tomoyo_write_transition_control
===============================

.. c:function:: int tomoyo_write_transition_control(struct tomoyo_acl_param *param, const u8 type)

    Write "struct tomoyo_transition_control" list.

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

    :param const u8 type:
        Type of this entry.

.. _`tomoyo_write_transition_control.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_scan_transition`:

tomoyo_scan_transition
======================

.. c:function:: bool tomoyo_scan_transition(const struct list_head *list, const struct tomoyo_path_info *domainname, const struct tomoyo_path_info *program, const char *last_name, const enum tomoyo_transition_type type)

    Try to find specific domain transition type.

    :param const struct list_head \*list:
        Pointer to "struct list_head".

    :param const struct tomoyo_path_info \*domainname:
        The name of current domain.

    :param const struct tomoyo_path_info \*program:
        The name of requested program.

    :param const char \*last_name:
        The last component of \ ``domainname``\ .

    :param const enum tomoyo_transition_type type:
        One of values in "enum tomoyo_transition_type".

.. _`tomoyo_scan_transition.description`:

Description
-----------

Returns true if found one, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_transition_type`:

tomoyo_transition_type
======================

.. c:function:: enum tomoyo_transition_type tomoyo_transition_type(const struct tomoyo_policy_namespace *ns, const struct tomoyo_path_info *domainname, const struct tomoyo_path_info *program)

    Get domain transition type.

    :param const struct tomoyo_policy_namespace \*ns:
        Pointer to "struct tomoyo_policy_namespace".

    :param const struct tomoyo_path_info \*domainname:
        The name of current domain.

    :param const struct tomoyo_path_info \*program:
        The name of requested program.

.. _`tomoyo_transition_type.description`:

Description
-----------

Returns TOMOYO_TRANSITION_CONTROL_TRANSIT if executing \ ``program``\  causes
domain transition across namespaces, TOMOYO_TRANSITION_CONTROL_INITIALIZE if
executing \ ``program``\  reinitializes domain transition within that namespace,
TOMOYO_TRANSITION_CONTROL_KEEP if executing \ ``program``\  stays at \ ``domainname``\  ,
others otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_same_aggregator`:

tomoyo_same_aggregator
======================

.. c:function:: bool tomoyo_same_aggregator(const struct tomoyo_acl_head *a, const struct tomoyo_acl_head *b)

    Check for duplicated "struct tomoyo_aggregator" entry.

    :param const struct tomoyo_acl_head \*a:
        Pointer to "struct tomoyo_acl_head".

    :param const struct tomoyo_acl_head \*b:
        Pointer to "struct tomoyo_acl_head".

.. _`tomoyo_same_aggregator.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_write_aggregator`:

tomoyo_write_aggregator
=======================

.. c:function:: int tomoyo_write_aggregator(struct tomoyo_acl_param *param)

    Write "struct tomoyo_aggregator" list.

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

.. _`tomoyo_write_aggregator.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_find_namespace`:

tomoyo_find_namespace
=====================

.. c:function:: struct tomoyo_policy_namespace *tomoyo_find_namespace(const char *name, const unsigned int len)

    Find specified namespace.

    :param const char \*name:
        Name of namespace to find.

    :param const unsigned int len:
        Length of \ ``name``\ .

.. _`tomoyo_find_namespace.description`:

Description
-----------

Returns pointer to "struct tomoyo_policy_namespace" if found,
NULL otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_assign_namespace`:

tomoyo_assign_namespace
=======================

.. c:function:: struct tomoyo_policy_namespace *tomoyo_assign_namespace(const char *domainname)

    Create a new namespace.

    :param const char \*domainname:
        Name of namespace to create.

.. _`tomoyo_assign_namespace.description`:

Description
-----------

Returns pointer to "struct tomoyo_policy_namespace" on success,
NULL otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_namespace_jump`:

tomoyo_namespace_jump
=====================

.. c:function:: bool tomoyo_namespace_jump(const char *domainname)

    Check for namespace jump.

    :param const char \*domainname:
        Name of domain.

.. _`tomoyo_namespace_jump.description`:

Description
-----------

Returns true if namespace differs, false otherwise.

.. _`tomoyo_assign_domain`:

tomoyo_assign_domain
====================

.. c:function:: struct tomoyo_domain_info *tomoyo_assign_domain(const char *domainname, const bool transit)

    Create a domain or a namespace.

    :param const char \*domainname:
        The name of domain.

    :param const bool transit:
        True if transit to domain found or created.

.. _`tomoyo_assign_domain.description`:

Description
-----------

Returns pointer to "struct tomoyo_domain_info" on success, NULL otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_environ`:

tomoyo_environ
==============

.. c:function:: int tomoyo_environ(struct tomoyo_execve *ee)

    Check permission for environment variable names.

    :param struct tomoyo_execve \*ee:
        Pointer to "struct tomoyo_execve".

.. _`tomoyo_environ.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_find_next_domain`:

tomoyo_find_next_domain
=======================

.. c:function:: int tomoyo_find_next_domain(struct linux_binprm *bprm)

    Find a domain.

    :param struct linux_binprm \*bprm:
        Pointer to "struct linux_binprm".

.. _`tomoyo_find_next_domain.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_dump_page`:

tomoyo_dump_page
================

.. c:function:: bool tomoyo_dump_page(struct linux_binprm *bprm, unsigned long pos, struct tomoyo_page_dump *dump)

    Dump a page to buffer.

    :param struct linux_binprm \*bprm:
        Pointer to "struct linux_binprm".

    :param unsigned long pos:
        Location to dump.

    :param struct tomoyo_page_dump \*dump:
        Poiner to "struct tomoyo_page_dump".

.. _`tomoyo_dump_page.description`:

Description
-----------

Returns true on success, false otherwise.

.. This file was automatic generated / don't edit.

