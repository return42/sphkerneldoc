.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/lib.c

.. _`aa_split_fqname`:

aa_split_fqname
===============

.. c:function:: char *aa_split_fqname(char *fqname, char **ns_name)

    split a fqname into a profile and namespace name

    :param char \*fqname:
        a full qualified name in namespace profile format (NOT NULL)

    :param char \*\*ns_name:
        pointer to portion of the string containing the ns name (NOT NULL)

.. _`aa_split_fqname.return`:

Return
------

profile name or NULL if one is not specified

Split a namespace name from a profile name (see policy.c for naming
description).  If a portion of the name is missing it returns NULL for
that portion.

.. _`aa_split_fqname.note`:

NOTE
----

may modify the \ ``fqname``\  string.  The pointers returned point
into the \ ``fqname``\  string.

.. _`aa_info_message`:

aa_info_message
===============

.. c:function:: void aa_info_message(const char *str)

    log a none profile related status message

    :param const char \*str:
        message to log

.. _`__aa_kvmalloc`:

__aa_kvmalloc
=============

.. c:function:: void *__aa_kvmalloc(size_t size, gfp_t flags)

    do allocation preferring kmalloc but falling back to vmalloc

    :param size_t size:
        how many bytes of memory are required

    :param gfp_t flags:
        the type of memory to allocate (see kmalloc).

.. _`__aa_kvmalloc.return`:

Return
------

allocated buffer or NULL if failed

It is possible that policy being loaded from the user is larger than
what can be allocated by kmalloc, in those cases fall back to vmalloc.

.. This file was automatic generated / don't edit.

