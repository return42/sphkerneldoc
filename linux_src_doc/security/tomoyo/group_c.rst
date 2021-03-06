.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/group.c

.. _`tomoyo_same_path_group`:

tomoyo_same_path_group
======================

.. c:function:: bool tomoyo_same_path_group(const struct tomoyo_acl_head *a, const struct tomoyo_acl_head *b)

    Check for duplicated "struct tomoyo_path_group" entry.

    :param a:
        Pointer to "struct tomoyo_acl_head".
    :type a: const struct tomoyo_acl_head \*

    :param b:
        Pointer to "struct tomoyo_acl_head".
    :type b: const struct tomoyo_acl_head \*

.. _`tomoyo_same_path_group.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_same_number_group`:

tomoyo_same_number_group
========================

.. c:function:: bool tomoyo_same_number_group(const struct tomoyo_acl_head *a, const struct tomoyo_acl_head *b)

    Check for duplicated "struct tomoyo_number_group" entry.

    :param a:
        Pointer to "struct tomoyo_acl_head".
    :type a: const struct tomoyo_acl_head \*

    :param b:
        Pointer to "struct tomoyo_acl_head".
    :type b: const struct tomoyo_acl_head \*

.. _`tomoyo_same_number_group.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_same_address_group`:

tomoyo_same_address_group
=========================

.. c:function:: bool tomoyo_same_address_group(const struct tomoyo_acl_head *a, const struct tomoyo_acl_head *b)

    Check for duplicated "struct tomoyo_address_group" entry.

    :param a:
        Pointer to "struct tomoyo_acl_head".
    :type a: const struct tomoyo_acl_head \*

    :param b:
        Pointer to "struct tomoyo_acl_head".
    :type b: const struct tomoyo_acl_head \*

.. _`tomoyo_same_address_group.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_write_group`:

tomoyo_write_group
==================

.. c:function:: int tomoyo_write_group(struct tomoyo_acl_param *param, const u8 type)

    Write "struct tomoyo_path_group"/"struct tomoyo_number_group"/"struct tomoyo_address_group" list.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

    :param type:
        Type of this group.
    :type type: const u8

.. _`tomoyo_write_group.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_matches_group`:

tomoyo_path_matches_group
=========================

.. c:function:: const struct tomoyo_path_info *tomoyo_path_matches_group(const struct tomoyo_path_info *pathname, const struct tomoyo_group *group)

    Check whether the given pathname matches members of the given pathname group.

    :param pathname:
        The name of pathname.
    :type pathname: const struct tomoyo_path_info \*

    :param group:
        Pointer to "struct tomoyo_path_group".
    :type group: const struct tomoyo_group \*

.. _`tomoyo_path_matches_group.description`:

Description
-----------

Returns matched member's pathname if \ ``pathname``\  matches pathnames in \ ``group``\ ,
NULL otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_number_matches_group`:

tomoyo_number_matches_group
===========================

.. c:function:: bool tomoyo_number_matches_group(const unsigned long min, const unsigned long max, const struct tomoyo_group *group)

    Check whether the given number matches members of the given number group.

    :param min:
        Min number.
    :type min: const unsigned long

    :param max:
        Max number.
    :type max: const unsigned long

    :param group:
        Pointer to "struct tomoyo_number_group".
    :type group: const struct tomoyo_group \*

.. _`tomoyo_number_matches_group.description`:

Description
-----------

Returns true if \ ``min``\  and \ ``max``\  partially overlaps \ ``group``\ , false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_address_matches_group`:

tomoyo_address_matches_group
============================

.. c:function:: bool tomoyo_address_matches_group(const bool is_ipv6, const __be32 *address, const struct tomoyo_group *group)

    Check whether the given address matches members of the given address group.

    :param is_ipv6:
        True if \ ``address``\  is an IPv6 address.
    :type is_ipv6: const bool

    :param address:
        An IPv4 or IPv6 address.
    :type address: const __be32 \*

    :param group:
        Pointer to "struct tomoyo_address_group".
    :type group: const struct tomoyo_group \*

.. _`tomoyo_address_matches_group.description`:

Description
-----------

Returns true if \ ``address``\  matches addresses in \ ``group``\  group, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. This file was automatic generated / don't edit.

