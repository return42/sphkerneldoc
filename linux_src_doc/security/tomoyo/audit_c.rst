.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/audit.c

.. _`tomoyo_print_bprm`:

tomoyo_print_bprm
=================

.. c:function:: char *tomoyo_print_bprm(struct linux_binprm *bprm, struct tomoyo_page_dump *dump)

    Print "struct linux_binprm" for auditing.

    :param struct linux_binprm \*bprm:
        Pointer to "struct linux_binprm".

    :param struct tomoyo_page_dump \*dump:
        Pointer to "struct tomoyo_page_dump".

.. _`tomoyo_print_bprm.description`:

Description
-----------

Returns the contents of \ ``bprm``\  on success, NULL otherwise.

This function uses \ :c:func:`kzalloc`\ , so caller must \ :c:func:`kfree`\  if this function
didn't return NULL.

.. _`tomoyo_filetype`:

tomoyo_filetype
===============

.. c:function:: const char *tomoyo_filetype(const umode_t mode)

    Get string representation of file type.

    :param const umode_t mode:
        Mode value for \ :c:func:`stat`\ .

.. _`tomoyo_filetype.description`:

Description
-----------

Returns file type string.

.. _`tomoyo_print_header`:

tomoyo_print_header
===================

.. c:function:: char *tomoyo_print_header(struct tomoyo_request_info *r)

    Get header line of audit log.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

.. _`tomoyo_print_header.description`:

Description
-----------

Returns string representation.

This function uses \ :c:func:`kmalloc`\ , so caller must \ :c:func:`kfree`\  if this function
didn't return NULL.

.. _`tomoyo_init_log`:

tomoyo_init_log
===============

.. c:function:: char *tomoyo_init_log(struct tomoyo_request_info *r, int len, const char *fmt, va_list args)

    Allocate buffer for audit logs.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param int len:
        Buffer size needed for \ ``fmt``\  and \ ``args``\ .

    :param const char \*fmt:
        The \ :c:func:`printf`\ 's format string.

    :param va_list args:
        va_list structure for \ ``fmt``\ .

.. _`tomoyo_init_log.description`:

Description
-----------

Returns pointer to allocated memory.

This function uses \ :c:func:`kzalloc`\ , so caller must \ :c:func:`kfree`\  if this function
didn't return NULL.

.. _`tomoyo_get_audit`:

tomoyo_get_audit
================

.. c:function:: bool tomoyo_get_audit(const struct tomoyo_policy_namespace *ns, const u8 profile, const u8 index, const struct tomoyo_acl_info *matched_acl, const bool is_granted)

    Get audit mode.

    :param const struct tomoyo_policy_namespace \*ns:
        Pointer to "struct tomoyo_policy_namespace".

    :param const u8 profile:
        Profile number.

    :param const u8 index:
        Index number of functionality.

    :param const struct tomoyo_acl_info \*matched_acl:
        *undescribed*

    :param const bool is_granted:
        True if granted log, false otherwise.

.. _`tomoyo_get_audit.description`:

Description
-----------

Returns true if this request should be audited, false otherwise.

.. _`tomoyo_write_log2`:

tomoyo_write_log2
=================

.. c:function:: void tomoyo_write_log2(struct tomoyo_request_info *r, int len, const char *fmt, va_list args)

    Write an audit log.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param int len:
        Buffer size needed for \ ``fmt``\  and \ ``args``\ .

    :param const char \*fmt:
        The \ :c:func:`printf`\ 's format string.

    :param va_list args:
        va_list structure for \ ``fmt``\ .

.. _`tomoyo_write_log2.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_write_log`:

tomoyo_write_log
================

.. c:function:: void tomoyo_write_log(struct tomoyo_request_info *r, const char *fmt,  ...)

    Write an audit log.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param const char \*fmt:
        The \ :c:func:`printf`\ 's format string, followed by parameters.

    :param ellipsis ellipsis:
        variable arguments

.. _`tomoyo_write_log.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_read_log`:

tomoyo_read_log
===============

.. c:function:: void tomoyo_read_log(struct tomoyo_io_buffer *head)

    Read an audit log.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

.. _`tomoyo_read_log.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_poll_log`:

tomoyo_poll_log
===============

.. c:function:: unsigned int tomoyo_poll_log(struct file *file, poll_table *wait)

    Wait for an audit log.

    :param struct file \*file:
        Pointer to "struct file".

    :param poll_table \*wait:
        Pointer to "poll_table". Maybe NULL.

.. _`tomoyo_poll_log.description`:

Description
-----------

Returns POLLIN \| POLLRDNORM when ready to read an audit log.

.. This file was automatic generated / don't edit.

