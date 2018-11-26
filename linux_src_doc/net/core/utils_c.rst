.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/utils.c

.. _`in4_pton`:

in4_pton
========

.. c:function:: int in4_pton(const char *src, int srclen, u8 *dst, int delim, const char **end)

    convert an IPv4 address from literal to binary representation

    :param src:
        the start of the IPv4 address string
    :type src: const char \*

    :param srclen:
        the length of the string, -1 means strlen(src)
    :type srclen: int

    :param dst:
        the binary (u8[4] array) representation of the IPv4 address
    :type dst: u8 \*

    :param delim:
        the delimiter of the IPv4 address in \ ``src``\ , -1 means no delimiter
    :type delim: int

    :param end:
        A pointer to the end of the parsed string will be placed here
    :type end: const char \*\*

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

    :param src:
        the start of the IPv6 address string
    :type src: const char \*

    :param srclen:
        the length of the string, -1 means strlen(src)
    :type srclen: int

    :param dst:
        the binary (u8[16] array) representation of the IPv6 address
    :type dst: u8 \*

    :param delim:
        the delimiter of the IPv6 address in \ ``src``\ , -1 means no delimiter
    :type delim: int

    :param end:
        A pointer to the end of the parsed string will be placed here
    :type end: const char \*\*

.. _`in6_pton.description`:

Description
-----------

Return one on success, return zero when any error occurs
and \ ``end``\  will point to the end of the parsed string.

.. _`inet_pton_with_scope`:

inet_pton_with_scope
====================

.. c:function:: int inet_pton_with_scope(struct net *net, __kernel_sa_family_t af, const char *src, const char *port, struct sockaddr_storage *addr)

    convert an IPv4/IPv6 and port to socket address

    :param net:
        net namespace (used for scope handling)
    :type net: struct net \*

    :param af:
        address family, AF_INET, AF_INET6 or AF_UNSPEC for either
    :type af: __kernel_sa_family_t

    :param src:
        the start of the address string
    :type src: const char \*

    :param port:
        the start of the port string (or NULL for none)
    :type port: const char \*

    :param addr:
        output socket address
    :type addr: struct sockaddr_storage \*

.. _`inet_pton_with_scope.description`:

Description
-----------

Return zero on success, return errno when any error occurs.

.. This file was automatic generated / don't edit.

