.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sunrpc/addr.h

.. _`rpc_cmp_addr`:

rpc_cmp_addr
============

.. c:function:: bool rpc_cmp_addr(const struct sockaddr *sap1, const struct sockaddr *sap2)

    compare the address portion of two sockaddrs.

    :param const struct sockaddr \*sap1:
        first sockaddr

    :param const struct sockaddr \*sap2:
        second sockaddr

.. _`rpc_cmp_addr.description`:

Description
-----------

Just compares the family and address portion. Ignores port, but
compares the scope if it's a link-local address.

Returns true if the addrs are equal, false if they aren't.

.. _`rpc_cmp_addr_port`:

rpc_cmp_addr_port
=================

.. c:function:: bool rpc_cmp_addr_port(const struct sockaddr *sap1, const struct sockaddr *sap2)

    compare the address and port number of two sockaddrs.

    :param const struct sockaddr \*sap1:
        first sockaddr

    :param const struct sockaddr \*sap2:
        second sockaddr

.. _`rpc_copy_addr`:

rpc_copy_addr
=============

.. c:function:: bool rpc_copy_addr(struct sockaddr *dst, const struct sockaddr *src)

    copy the address portion of one sockaddr to another

    :param struct sockaddr \*dst:
        destination sockaddr

    :param const struct sockaddr \*src:
        source sockaddr

.. _`rpc_copy_addr.description`:

Description
-----------

Just copies the address portion and family. Ignores port, scope, etc.
Caller is responsible for making certain that dst is large enough to hold
the address in src. Returns true if address family is supported. Returns
false otherwise.

.. _`rpc_get_scope_id`:

rpc_get_scope_id
================

.. c:function:: u32 rpc_get_scope_id(const struct sockaddr *sa)

    return scopeid for a given sockaddr

    :param const struct sockaddr \*sa:
        sockaddr to get scopeid from

.. _`rpc_get_scope_id.description`:

Description
-----------

Returns the value of the sin6_scope_id for AF_INET6 addrs, or 0 if
not an AF_INET6 address.

.. This file was automatic generated / don't edit.

