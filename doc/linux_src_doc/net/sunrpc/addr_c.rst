.. -*- coding: utf-8; mode: rst -*-

======
addr.c
======


.. _`rpc_ntop`:

rpc_ntop
========

.. c:function:: size_t rpc_ntop (const struct sockaddr *sap, char *buf, const size_t buflen)

    construct a presentation address in @buf

    :param const struct sockaddr \*sap:
        socket address

    :param char \*buf:
        construction area

    :param const size_t buflen:
        size of ``buf``\ , in bytes



.. _`rpc_ntop.description`:

Description
-----------

Plants a ``NUL-terminated`` string in ``buf`` and returns the length
of the string, excluding the ``NUL``\ .  Otherwise zero is returned.



.. _`rpc_pton`:

rpc_pton
========

.. c:function:: size_t rpc_pton (struct net *net, const char *buf, const size_t buflen, struct sockaddr *sap, const size_t salen)

    Construct a sockaddr in @sap

    :param struct net \*net:
        applicable network namespace

    :param const char \*buf:
        C string containing presentation format IP address

    :param const size_t buflen:
        length of presentation address in bytes

    :param struct sockaddr \*sap:
        buffer into which to plant socket address

    :param const size_t salen:
        size of buffer in bytes



.. _`rpc_pton.description`:

Description
-----------

Returns the size of the socket address if successful; otherwise
zero is returned.

Plants a socket address in ``sap`` and returns the size of the
socket address, if successful.  Returns zero if an error
occurred.



.. _`rpc_sockaddr2uaddr`:

rpc_sockaddr2uaddr
==================

.. c:function:: char *rpc_sockaddr2uaddr (const struct sockaddr *sap, gfp_t gfp_flags)

    Construct a universal address string from @sap.

    :param const struct sockaddr \*sap:
        socket address

    :param gfp_t gfp_flags:
        allocation mode



.. _`rpc_sockaddr2uaddr.description`:

Description
-----------

Returns a ``NUL-terminated`` string in dynamically allocated memory;
otherwise NULL is returned if an error occurred.  Caller must
free the returned string.



.. _`rpc_uaddr2sockaddr`:

rpc_uaddr2sockaddr
==================

.. c:function:: size_t rpc_uaddr2sockaddr (struct net *net, const char *uaddr, const size_t uaddr_len, struct sockaddr *sap, const size_t salen)

    convert a universal address to a socket address.

    :param struct net \*net:
        applicable network namespace

    :param const char \*uaddr:
        C string containing universal address to convert

    :param const size_t uaddr_len:
        length of universal address string

    :param struct sockaddr \*sap:
        buffer into which to plant socket address

    :param const size_t salen:
        size of buffer



.. _`rpc_uaddr2sockaddr.description`:

Description
-----------

``uaddr`` does not have to be '\0'-terminated, but :c:func:`kstrtou8` and
:c:func:`rpc_pton` require proper string termination to be successful.

Returns the size of the socket address if successful; otherwise
zero is returned.

