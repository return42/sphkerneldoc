.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/utils.c

.. _`in4_pton`:

in4_pton
========

.. c:function:: int in4_pton(const char *src, int srclen, u8 *dst, int delim, const char **end)

    convert an IPv4 address from literal to binary representation

    :param const char \*src:
        the start of the IPv4 address string

    :param int srclen:
        the length of the string, -1 means strlen(src)

    :param u8 \*dst:
        the binary (u8[4] array) representation of the IPv4 address

    :param int delim:
        the delimiter of the IPv4 address in \ ``src``\ , -1 means no delimiter

    :param const char \*\*end:
        A pointer to the end of the parsed string will be placed here

.. _`in4_pton.description`:

Description
-----------

Return one on success, return zero when any error occurs
and \ ``end``\  will point to the end of the parsed string.

.. _`in6_pton`:

in6_pton
========

.. c:function:: int in6_pton(const char *src, int srclen, u8 *dst, int delim, const char **end)

    convert an IPv6 address from literal to binary representation

    :param const char \*src:
        the start of the IPv6 address string

    :param int srclen:
        the length of the string, -1 means strlen(src)

    :param u8 \*dst:
        the binary (u8[16] array) representation of the IPv6 address

    :param int delim:
        the delimiter of the IPv6 address in \ ``src``\ , -1 means no delimiter

    :param const char \*\*end:
        A pointer to the end of the parsed string will be placed here

.. _`in6_pton.description`:

Description
-----------

Return one on success, return zero when any error occurs
and \ ``end``\  will point to the end of the parsed string.

.. This file was automatic generated / don't edit.

