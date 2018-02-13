.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/common.c

.. _`tomoyo_yesno`:

tomoyo_yesno
============

.. c:function:: const char *tomoyo_yesno(const unsigned int value)

    Return "yes" or "no".

    :param const unsigned int value:
        Bool value.

.. _`tomoyo_addprintf`:

tomoyo_addprintf
================

.. c:function:: void tomoyo_addprintf(char *buffer, int len, const char *fmt,  ...)

    \ :c:func:`strncat`\ -like-snprintf().

    :param char \*buffer:
        Buffer to write to. Must be '\0'-terminated.

    :param int len:
        Size of \ ``buffer``\ .

    :param const char \*fmt:
        The \ :c:func:`printf`\ 's format string, followed by parameters.

    :param ellipsis ellipsis:
        variable arguments

.. _`tomoyo_addprintf.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_flush`:

tomoyo_flush
============

.. c:function:: bool tomoyo_flush(struct tomoyo_io_buffer *head)

    Flush queued string to userspace's buffer.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_flush.description`:

Description
-----------

Returns true if all data was flushed, false otherwise.

.. _`tomoyo_set_string`:

tomoyo_set_string
=================

.. c:function:: void tomoyo_set_string(struct tomoyo_io_buffer *head, const char *string)

    Queue string to "struct tomoyo_io_buffer" structure.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const char \*string:
        String to print.

.. _`tomoyo_set_string.description`:

Description
-----------

Note that \ ``string``\  has to be kept valid until \ ``head``\  is \ :c:func:`kfree`\ d.
This means that char[] allocated on stack memory cannot be passed to
this function. Use \ :c:func:`tomoyo_io_printf`\  for char[] allocated on stack memory.

.. _`tomoyo_io_printf`:

tomoyo_io_printf
================

.. c:function:: void tomoyo_io_printf(struct tomoyo_io_buffer *head, const char *fmt,  ...)

    \ :c:func:`printf`\  to "struct tomoyo_io_buffer" structure.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const char \*fmt:
        The \ :c:func:`printf`\ 's format string, followed by parameters.

    :param ellipsis ellipsis:
        variable arguments

.. _`tomoyo_set_space`:

tomoyo_set_space
================

.. c:function:: void tomoyo_set_space(struct tomoyo_io_buffer *head)

    Put a space to "struct tomoyo_io_buffer" structure.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_set_space.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_set_lf`:

tomoyo_set_lf
=============

.. c:function:: bool tomoyo_set_lf(struct tomoyo_io_buffer *head)

    Put a line feed to "struct tomoyo_io_buffer" structure.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_set_lf.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_set_slash`:

tomoyo_set_slash
================

.. c:function:: void tomoyo_set_slash(struct tomoyo_io_buffer *head)

    Put a shash to "struct tomoyo_io_buffer" structure.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_set_slash.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_init_policy_namespace`:

tomoyo_init_policy_namespace
============================

.. c:function:: void tomoyo_init_policy_namespace(struct tomoyo_policy_namespace *ns)

    Initialize namespace.

    :param struct tomoyo_policy_namespace \*ns:
        Pointer to "struct tomoyo_policy_namespace".

.. _`tomoyo_init_policy_namespace.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_print_namespace`:

tomoyo_print_namespace
======================

.. c:function:: void tomoyo_print_namespace(struct tomoyo_io_buffer *head)

    Print namespace header.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_print_namespace.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_print_name_union`:

tomoyo_print_name_union
=======================

.. c:function:: void tomoyo_print_name_union(struct tomoyo_io_buffer *head, const struct tomoyo_name_union *ptr)

    Print a tomoyo_name_union.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const struct tomoyo_name_union \*ptr:
        Pointer to "struct tomoyo_name_union".

.. _`tomoyo_print_name_union_quoted`:

tomoyo_print_name_union_quoted
==============================

.. c:function:: void tomoyo_print_name_union_quoted(struct tomoyo_io_buffer *head, const struct tomoyo_name_union *ptr)

    Print a tomoyo_name_union with a quote.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const struct tomoyo_name_union \*ptr:
        Pointer to "struct tomoyo_name_union".

.. _`tomoyo_print_name_union_quoted.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_print_number_union_nospace`:

tomoyo_print_number_union_nospace
=================================

.. c:function:: void tomoyo_print_number_union_nospace(struct tomoyo_io_buffer *head, const struct tomoyo_number_union *ptr)

    Print a tomoyo_number_union without a space.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const struct tomoyo_number_union \*ptr:
        Pointer to "struct tomoyo_number_union".

.. _`tomoyo_print_number_union_nospace.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_print_number_union`:

tomoyo_print_number_union
=========================

.. c:function:: void tomoyo_print_number_union(struct tomoyo_io_buffer *head, const struct tomoyo_number_union *ptr)

    Print a tomoyo_number_union.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const struct tomoyo_number_union \*ptr:
        Pointer to "struct tomoyo_number_union".

.. _`tomoyo_print_number_union.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_assign_profile`:

tomoyo_assign_profile
=====================

.. c:function:: struct tomoyo_profile *tomoyo_assign_profile(struct tomoyo_policy_namespace *ns, const unsigned int profile)

    Create a new profile.

    :param struct tomoyo_policy_namespace \*ns:
        Pointer to "struct tomoyo_policy_namespace".

    :param const unsigned int profile:
        Profile number to create.

.. _`tomoyo_assign_profile.description`:

Description
-----------

Returns pointer to "struct tomoyo_profile" on success, NULL otherwise.

.. _`tomoyo_profile`:

tomoyo_profile
==============

.. c:function:: struct tomoyo_profile *tomoyo_profile(const struct tomoyo_policy_namespace *ns, const u8 profile)

    Find a profile.

    :param const struct tomoyo_policy_namespace \*ns:
        Pointer to "struct tomoyo_policy_namespace".

    :param const u8 profile:
        Profile number to find.

.. _`tomoyo_profile.description`:

Description
-----------

Returns pointer to "struct tomoyo_profile".

.. _`tomoyo_find_yesno`:

tomoyo_find_yesno
=================

.. c:function:: s8 tomoyo_find_yesno(const char *string, const char *find)

    Find values for specified keyword.

    :param const char \*string:
        String to check.

    :param const char \*find:
        Name of keyword.

.. _`tomoyo_find_yesno.description`:

Description
-----------

Returns 1 if "@find=yes" was found, 0 if "@find=no" was found, -1 otherwise.

.. _`tomoyo_set_uint`:

tomoyo_set_uint
===============

.. c:function:: void tomoyo_set_uint(unsigned int *i, const char *string, const char *find)

    Set value for specified preference.

    :param unsigned int \*i:
        Pointer to "unsigned int".

    :param const char \*string:
        String to check.

    :param const char \*find:
        Name of keyword.

.. _`tomoyo_set_uint.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_set_mode`:

tomoyo_set_mode
===============

.. c:function:: int tomoyo_set_mode(char *name, const char *value, struct tomoyo_profile *profile)

    Set mode for specified profile.

    :param char \*name:
        Name of functionality.

    :param const char \*value:
        Mode for \ ``name``\ .

    :param struct tomoyo_profile \*profile:
        Pointer to "struct tomoyo_profile".

.. _`tomoyo_set_mode.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_write_profile`:

tomoyo_write_profile
====================

.. c:function:: int tomoyo_write_profile(struct tomoyo_io_buffer *head)

    Write profile table.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_profile.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_print_config`:

tomoyo_print_config
===================

.. c:function:: void tomoyo_print_config(struct tomoyo_io_buffer *head, const u8 config)

    Print mode for specified functionality.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const u8 config:
        Mode for that functionality.

.. _`tomoyo_print_config.description`:

Description
-----------

Returns nothing.

Caller prints functionality's name.

.. _`tomoyo_read_profile`:

tomoyo_read_profile
===================

.. c:function:: void tomoyo_read_profile(struct tomoyo_io_buffer *head)

    Read profile table.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_profile.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_same_manager`:

tomoyo_same_manager
===================

.. c:function:: bool tomoyo_same_manager(const struct tomoyo_acl_head *a, const struct tomoyo_acl_head *b)

    Check for duplicated "struct tomoyo_manager" entry.

    :param const struct tomoyo_acl_head \*a:
        Pointer to "struct tomoyo_acl_head".

    :param const struct tomoyo_acl_head \*b:
        Pointer to "struct tomoyo_acl_head".

.. _`tomoyo_same_manager.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_update_manager_entry`:

tomoyo_update_manager_entry
===========================

.. c:function:: int tomoyo_update_manager_entry(const char *manager, const bool is_delete)

    Add a manager entry.

    :param const char \*manager:
        The path to manager or the domainnamme.

    :param const bool is_delete:
        True if it is a delete request.

.. _`tomoyo_update_manager_entry.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_write_manager`:

tomoyo_write_manager
====================

.. c:function:: int tomoyo_write_manager(struct tomoyo_io_buffer *head)

    Write manager policy.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_manager.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_read_manager`:

tomoyo_read_manager
===================

.. c:function:: void tomoyo_read_manager(struct tomoyo_io_buffer *head)

    Read manager policy.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_manager.description`:

Description
-----------

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_manager`:

tomoyo_manager
==============

.. c:function:: bool tomoyo_manager( void)

    Check whether the current process is a policy manager.

    :param  void:
        no arguments

.. _`tomoyo_manager.description`:

Description
-----------

Returns true if the current process is permitted to modify policy
via /sys/kernel/security/tomoyo/ interface.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_select_domain`:

tomoyo_select_domain
====================

.. c:function:: bool tomoyo_select_domain(struct tomoyo_io_buffer *head, const char *data)

    Parse select command.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const char \*data:
        String to parse.

.. _`tomoyo_select_domain.description`:

Description
-----------

Returns true on success, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_same_task_acl`:

tomoyo_same_task_acl
====================

.. c:function:: bool tomoyo_same_task_acl(const struct tomoyo_acl_info *a, const struct tomoyo_acl_info *b)

    Check for duplicated "struct tomoyo_task_acl" entry.

    :param const struct tomoyo_acl_info \*a:
        Pointer to "struct tomoyo_acl_info".

    :param const struct tomoyo_acl_info \*b:
        Pointer to "struct tomoyo_acl_info".

.. _`tomoyo_same_task_acl.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_write_task`:

tomoyo_write_task
=================

.. c:function:: int tomoyo_write_task(struct tomoyo_acl_param *param)

    Update task related list.

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

.. _`tomoyo_write_task.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_delete_domain`:

tomoyo_delete_domain
====================

.. c:function:: int tomoyo_delete_domain(char *domainname)

    Delete a domain.

    :param char \*domainname:
        The name of domain.

.. _`tomoyo_delete_domain.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_write_domain2`:

tomoyo_write_domain2
====================

.. c:function:: int tomoyo_write_domain2(struct tomoyo_policy_namespace *ns, struct list_head *list, char *data, const bool is_delete)

    Write domain policy.

    :param struct tomoyo_policy_namespace \*ns:
        Pointer to "struct tomoyo_policy_namespace".

    :param struct list_head \*list:
        Pointer to "struct list_head".

    :param char \*data:
        Policy to be interpreted.

    :param const bool is_delete:
        True if it is a delete request.

.. _`tomoyo_write_domain2.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_write_domain`:

tomoyo_write_domain
===================

.. c:function:: int tomoyo_write_domain(struct tomoyo_io_buffer *head)

    Write domain policy.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_domain.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_print_condition`:

tomoyo_print_condition
======================

.. c:function:: bool tomoyo_print_condition(struct tomoyo_io_buffer *head, const struct tomoyo_condition *cond)

    Print condition part.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const struct tomoyo_condition \*cond:
        Pointer to "struct tomoyo_condition".

.. _`tomoyo_print_condition.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_set_group`:

tomoyo_set_group
================

.. c:function:: void tomoyo_set_group(struct tomoyo_io_buffer *head, const char *category)

    Print "acl_group " header keyword and category name.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const char \*category:
        Category name.

.. _`tomoyo_set_group.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_print_entry`:

tomoyo_print_entry
==================

.. c:function:: bool tomoyo_print_entry(struct tomoyo_io_buffer *head, struct tomoyo_acl_info *acl)

    Print an ACL entry.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param struct tomoyo_acl_info \*acl:
        Pointer to an ACL entry.

.. _`tomoyo_print_entry.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_read_domain2`:

tomoyo_read_domain2
===================

.. c:function:: bool tomoyo_read_domain2(struct tomoyo_io_buffer *head, struct list_head *list)

    Read domain policy.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param struct list_head \*list:
        Pointer to "struct list_head".

.. _`tomoyo_read_domain2.description`:

Description
-----------

Caller holds \ :c:func:`tomoyo_read_lock`\ .

Returns true on success, false otherwise.

.. _`tomoyo_read_domain`:

tomoyo_read_domain
==================

.. c:function:: void tomoyo_read_domain(struct tomoyo_io_buffer *head)

    Read domain policy.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_domain.description`:

Description
-----------

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_write_pid`:

tomoyo_write_pid
================

.. c:function:: int tomoyo_write_pid(struct tomoyo_io_buffer *head)

    Specify PID to obtain domainname.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_pid.description`:

Description
-----------

Returns 0.

.. _`tomoyo_read_pid`:

tomoyo_read_pid
===============

.. c:function:: void tomoyo_read_pid(struct tomoyo_io_buffer *head)

    Get domainname of the specified PID.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_pid.description`:

Description
-----------

Returns the domainname which the specified PID is in on success,
empty string otherwise.
The PID is specified by \ :c:func:`tomoyo_write_pid`\  so that the user can obtain
using \ :c:func:`read`\ /write() interface rather than \ :c:func:`sysctl`\  interface.

.. _`tomoyo_write_exception`:

tomoyo_write_exception
======================

.. c:function:: int tomoyo_write_exception(struct tomoyo_io_buffer *head)

    Write exception policy.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_exception.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_read_group`:

tomoyo_read_group
=================

.. c:function:: bool tomoyo_read_group(struct tomoyo_io_buffer *head, const int idx)

    Read "struct tomoyo_path_group"/"struct tomoyo_number_group"/"struct tomoyo_address_group" list.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const int idx:
        Index number.

.. _`tomoyo_read_group.description`:

Description
-----------

Returns true on success, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_read_policy`:

tomoyo_read_policy
==================

.. c:function:: bool tomoyo_read_policy(struct tomoyo_io_buffer *head, const int idx)

    Read "struct tomoyo_..._entry" list.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const int idx:
        Index number.

.. _`tomoyo_read_policy.description`:

Description
-----------

Returns true on success, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_read_exception`:

tomoyo_read_exception
=====================

.. c:function:: void tomoyo_read_exception(struct tomoyo_io_buffer *head)

    Read exception policy.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_exception.description`:

Description
-----------

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_truncate`:

tomoyo_truncate
===============

.. c:function:: int tomoyo_truncate(char *str)

    Truncate a line.

    :param char \*str:
        String to truncate.

.. _`tomoyo_truncate.description`:

Description
-----------

Returns length of truncated \ ``str``\ .

.. _`tomoyo_add_entry`:

tomoyo_add_entry
================

.. c:function:: void tomoyo_add_entry(struct tomoyo_domain_info *domain, char *header)

    Add an ACL to current thread's domain. Used by learning mode.

    :param struct tomoyo_domain_info \*domain:
        Pointer to "struct tomoyo_domain_info".

    :param char \*header:
        Lines containing ACL.

.. _`tomoyo_add_entry.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_supervisor`:

tomoyo_supervisor
=================

.. c:function:: int tomoyo_supervisor(struct tomoyo_request_info *r, const char *fmt,  ...)

    Ask for the supervisor's decision.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param const char \*fmt:
        The \ :c:func:`printf`\ 's format string, followed by parameters.

    :param ellipsis ellipsis:
        variable arguments

.. _`tomoyo_supervisor.description`:

Description
-----------

Returns 0 if the supervisor decided to permit the access request which
violated the policy in enforcing mode, TOMOYO_RETRY_REQUEST if the
supervisor decided to retry the access request which violated the policy in
enforcing mode, 0 if it is not in enforcing mode, -EPERM otherwise.

.. _`tomoyo_find_domain_by_qid`:

tomoyo_find_domain_by_qid
=========================

.. c:function:: struct tomoyo_domain_info *tomoyo_find_domain_by_qid(unsigned int serial)

    Get domain by query id.

    :param unsigned int serial:
        Query ID assigned by \ :c:func:`tomoyo_supervisor`\ .

.. _`tomoyo_find_domain_by_qid.description`:

Description
-----------

Returns pointer to "struct tomoyo_domain_info" if found, NULL otherwise.

.. _`tomoyo_poll_query`:

tomoyo_poll_query
=================

.. c:function:: __poll_t tomoyo_poll_query(struct file *file, poll_table *wait)

    \ :c:func:`poll`\  for /sys/kernel/security/tomoyo/query.

    :param struct file \*file:
        Pointer to "struct file".

    :param poll_table \*wait:
        Pointer to "poll_table".

.. _`tomoyo_poll_query.description`:

Description
-----------

Returns EPOLLIN \| EPOLLRDNORM when ready to read, 0 otherwise.

Waits for access requests which violated policy in enforcing mode.

.. _`tomoyo_read_query`:

tomoyo_read_query
=================

.. c:function:: void tomoyo_read_query(struct tomoyo_io_buffer *head)

    Read access requests which violated policy in enforcing mode.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_answer`:

tomoyo_write_answer
===================

.. c:function:: int tomoyo_write_answer(struct tomoyo_io_buffer *head)

    Write the supervisor's decision.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_answer.description`:

Description
-----------

Returns 0 on success, -EINVAL otherwise.

.. _`tomoyo_read_version`:

tomoyo_read_version
===================

.. c:function:: void tomoyo_read_version(struct tomoyo_io_buffer *head)

    Get version.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_version.description`:

Description
-----------

Returns version information.

.. _`tomoyo_update_stat`:

tomoyo_update_stat
==================

.. c:function:: void tomoyo_update_stat(const u8 index)

    Update statistic counters.

    :param const u8 index:
        Index for policy type.

.. _`tomoyo_update_stat.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_read_stat`:

tomoyo_read_stat
================

.. c:function:: void tomoyo_read_stat(struct tomoyo_io_buffer *head)

    Read statistic data.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_stat.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_write_stat`:

tomoyo_write_stat
=================

.. c:function:: int tomoyo_write_stat(struct tomoyo_io_buffer *head)

    Set memory quota.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_write_stat.description`:

Description
-----------

Returns 0.

.. _`tomoyo_open_control`:

tomoyo_open_control
===================

.. c:function:: int tomoyo_open_control(const u8 type, struct file *file)

    \ :c:func:`open`\  for /sys/kernel/security/tomoyo/ interface.

    :param const u8 type:
        Type of interface.

    :param struct file \*file:
        Pointer to "struct file".

.. _`tomoyo_open_control.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_poll_control`:

tomoyo_poll_control
===================

.. c:function:: __poll_t tomoyo_poll_control(struct file *file, poll_table *wait)

    \ :c:func:`poll`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct file \*file:
        Pointer to "struct file".

    :param poll_table \*wait:
        Pointer to "poll_table". Maybe NULL.

.. _`tomoyo_poll_control.description`:

Description
-----------

Returns EPOLLIN \| EPOLLRDNORM \| EPOLLOUT \| EPOLLWRNORM if ready to read/write,
EPOLLOUT \| EPOLLWRNORM otherwise.

.. _`tomoyo_set_namespace_cursor`:

tomoyo_set_namespace_cursor
===========================

.. c:function:: void tomoyo_set_namespace_cursor(struct tomoyo_io_buffer *head)

    Set namespace to read.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_set_namespace_cursor.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_has_more_namespace`:

tomoyo_has_more_namespace
=========================

.. c:function:: bool tomoyo_has_more_namespace(struct tomoyo_io_buffer *head)

    Check for unread namespaces.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_has_more_namespace.description`:

Description
-----------

Returns true if we have more entries to print, false otherwise.

.. _`tomoyo_read_control`:

tomoyo_read_control
===================

.. c:function:: ssize_t tomoyo_read_control(struct tomoyo_io_buffer *head, char __user *buffer, const int buffer_len)

    \ :c:func:`read`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param char __user \*buffer:
        Poiner to buffer to write to.

    :param const int buffer_len:
        Size of \ ``buffer``\ .

.. _`tomoyo_read_control.description`:

Description
-----------

Returns bytes read on success, negative value otherwise.

.. _`tomoyo_parse_policy`:

tomoyo_parse_policy
===================

.. c:function:: int tomoyo_parse_policy(struct tomoyo_io_buffer *head, char *line)

    Parse a policy line.

    :param struct tomoyo_io_buffer \*head:
        Poiter to "struct tomoyo_io_buffer".

    :param char \*line:
        Line to parse.

.. _`tomoyo_parse_policy.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_write_control`:

tomoyo_write_control
====================

.. c:function:: ssize_t tomoyo_write_control(struct tomoyo_io_buffer *head, const char __user *buffer, const int buffer_len)

    \ :c:func:`write`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const char __user \*buffer:
        Pointer to buffer to read from.

    :param const int buffer_len:
        Size of \ ``buffer``\ .

.. _`tomoyo_write_control.description`:

Description
-----------

Returns \ ``buffer_len``\  on success, negative value otherwise.

.. _`tomoyo_close_control`:

tomoyo_close_control
====================

.. c:function:: void tomoyo_close_control(struct tomoyo_io_buffer *head)

    \ :c:func:`close`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_check_profile`:

tomoyo_check_profile
====================

.. c:function:: void tomoyo_check_profile( void)

    Check all profiles currently assigned to domains are defined.

    :param  void:
        no arguments

.. _`tomoyo_load_builtin_policy`:

tomoyo_load_builtin_policy
==========================

.. c:function:: void tomoyo_load_builtin_policy( void)

    Load built-in policy.

    :param  void:
        no arguments

.. _`tomoyo_load_builtin_policy.description`:

Description
-----------

Returns nothing.

.. This file was automatic generated / don't edit.

