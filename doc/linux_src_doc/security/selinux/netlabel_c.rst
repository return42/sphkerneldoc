.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/netlabel.c

.. _`selinux_netlbl_sidlookup_cached`:

selinux_netlbl_sidlookup_cached
===============================

.. c:function:: int selinux_netlbl_sidlookup_cached(struct sk_buff *skb, struct netlbl_lsm_secattr *secattr, u32 *sid)

    Cache a SID lookup

    :param struct sk_buff \*skb:
        the packet

    :param struct netlbl_lsm_secattr \*secattr:
        the NetLabel security attributes

    :param u32 \*sid:
        the SID

.. _`selinux_netlbl_sidlookup_cached.description`:

Description
-----------

Query the SELinux security server to lookup the correct SID for the given
security attributes.  If the query is successful, cache the result to speed
up future lookups.  Returns zero on success, negative values on failure.

.. _`selinux_netlbl_sock_genattr`:

selinux_netlbl_sock_genattr
===========================

.. c:function:: struct netlbl_lsm_secattr *selinux_netlbl_sock_genattr(struct sock *sk)

    Generate the NetLabel socket secattr

    :param struct sock \*sk:
        the socket

.. _`selinux_netlbl_sock_genattr.description`:

Description
-----------

Generate the NetLabel security attributes for a socket, making full use of
the socket's attribute cache.  Returns a pointer to the security attributes
on success, NULL on failure.

.. _`selinux_netlbl_sock_getattr`:

selinux_netlbl_sock_getattr
===========================

.. c:function:: struct netlbl_lsm_secattr *selinux_netlbl_sock_getattr(const struct sock *sk, u32 sid)

    Get the cached NetLabel secattr

    :param const struct sock \*sk:
        the socket

    :param u32 sid:
        the SID

.. _`selinux_netlbl_sock_getattr.description`:

Description
-----------

Query the socket's cached secattr and if the SID matches the cached value
return the cache, otherwise return NULL.

.. _`selinux_netlbl_cache_invalidate`:

selinux_netlbl_cache_invalidate
===============================

.. c:function:: void selinux_netlbl_cache_invalidate( void)

    Invalidate the NetLabel cache

    :param  void:
        no arguments

.. _`selinux_netlbl_cache_invalidate.description`:

Description
-----------

Invalidate the NetLabel security attribute mapping cache.

.. _`selinux_netlbl_err`:

selinux_netlbl_err
==================

.. c:function:: void selinux_netlbl_err(struct sk_buff *skb, int error, int gateway)

    Handle a NetLabel packet error

    :param struct sk_buff \*skb:
        the packet

    :param int error:
        the error code

    :param int gateway:
        true if host is acting as a gateway, false otherwise

.. _`selinux_netlbl_err.description`:

Description
-----------

When a packet is dropped due to a call to \ :c:func:`avc_has_perm`\  pass the error
code to the NetLabel subsystem so any protocol specific processing can be
done.  This is safe to call even if you are unsure if NetLabel labeling is
present on the packet, NetLabel is smart enough to only act when it should.

.. _`selinux_netlbl_sk_security_free`:

selinux_netlbl_sk_security_free
===============================

.. c:function:: void selinux_netlbl_sk_security_free(struct sk_security_struct *sksec)

    Free the NetLabel fields

    :param struct sk_security_struct \*sksec:
        the sk_security_struct

.. _`selinux_netlbl_sk_security_free.description`:

Description
-----------

Free all of the memory in the NetLabel fields of a sk_security_struct.

.. _`selinux_netlbl_sk_security_reset`:

selinux_netlbl_sk_security_reset
================================

.. c:function:: void selinux_netlbl_sk_security_reset(struct sk_security_struct *sksec)

    Reset the NetLabel fields

    :param struct sk_security_struct \*sksec:
        the sk_security_struct

.. _`selinux_netlbl_sk_security_reset.description`:

Description
-----------

Called when the NetLabel state of a sk_security_struct needs to be reset.
The caller is responsible for all the NetLabel sk_security_struct locking.

.. _`selinux_netlbl_skbuff_getsid`:

selinux_netlbl_skbuff_getsid
============================

.. c:function:: int selinux_netlbl_skbuff_getsid(struct sk_buff *skb, u16 family, u32 *type, u32 *sid)

    Get the sid of a packet using NetLabel

    :param struct sk_buff \*skb:
        the packet

    :param u16 family:
        protocol family

    :param u32 \*type:
        NetLabel labeling protocol type

    :param u32 \*sid:
        the SID

.. _`selinux_netlbl_skbuff_getsid.description`:

Description
-----------

Call the NetLabel mechanism to get the security attributes of the given
packet and use those attributes to determine the correct context/SID to
assign to the packet.  Returns zero on success, negative values on failure.

.. _`selinux_netlbl_skbuff_setsid`:

selinux_netlbl_skbuff_setsid
============================

.. c:function:: int selinux_netlbl_skbuff_setsid(struct sk_buff *skb, u16 family, u32 sid)

    Set the NetLabel on a packet given a sid

    :param struct sk_buff \*skb:
        the packet

    :param u16 family:
        protocol family

    :param u32 sid:
        the SID

.. _`selinux_netlbl_skbuff_setsid.description`:

Description
-----------

Description
Call the NetLabel mechanism to set the label of a packet using \ ``sid``\ .
Returns zero on success, negative values on failure.

.. _`selinux_netlbl_inet_conn_request`:

selinux_netlbl_inet_conn_request
================================

.. c:function:: int selinux_netlbl_inet_conn_request(struct request_sock *req, u16 family)

    Label an incoming stream connection

    :param struct request_sock \*req:
        incoming connection request socket

    :param u16 family:
        *undescribed*

.. _`selinux_netlbl_inet_conn_request.description`:

Description
-----------

A new incoming connection request is represented by \ ``req``\ , we need to label
the new request_sock here and the stack will ensure the on-the-wire label
will get preserved when a full sock is created once the connection handshake
is complete.  Returns zero on success, negative values on failure.

.. _`selinux_netlbl_inet_csk_clone`:

selinux_netlbl_inet_csk_clone
=============================

.. c:function:: void selinux_netlbl_inet_csk_clone(struct sock *sk, u16 family)

    Initialize the newly created sock

    :param struct sock \*sk:
        the new sock

    :param u16 family:
        *undescribed*

.. _`selinux_netlbl_inet_csk_clone.description`:

Description
-----------

A new connection has been established using \ ``sk``\ , we've already labeled the
socket via the request_sock struct in \ :c:func:`selinux_netlbl_inet_conn_request`\  but
we need to set the NetLabel state here since we now have a sock structure.

.. _`selinux_netlbl_socket_post_create`:

selinux_netlbl_socket_post_create
=================================

.. c:function:: int selinux_netlbl_socket_post_create(struct sock *sk, u16 family)

    Label a socket using NetLabel

    :param struct sock \*sk:
        *undescribed*

    :param u16 family:
        protocol family

.. _`selinux_netlbl_socket_post_create.description`:

Description
-----------

Attempt to label a socket using the NetLabel mechanism using the given
SID.  Returns zero values on success, negative values on failure.

.. _`selinux_netlbl_sock_rcv_skb`:

selinux_netlbl_sock_rcv_skb
===========================

.. c:function:: int selinux_netlbl_sock_rcv_skb(struct sk_security_struct *sksec, struct sk_buff *skb, u16 family, struct common_audit_data *ad)

    Do an inbound access check using NetLabel

    :param struct sk_security_struct \*sksec:
        the sock's sk_security_struct

    :param struct sk_buff \*skb:
        the packet

    :param u16 family:
        protocol family

    :param struct common_audit_data \*ad:
        the audit data

.. _`selinux_netlbl_sock_rcv_skb.description`:

Description
-----------

Fetch the NetLabel security attributes from \ ``skb``\  and perform an access check
against the receiving socket.  Returns zero on success, negative values on
error.

.. _`selinux_netlbl_socket_setsockopt`:

selinux_netlbl_socket_setsockopt
================================

.. c:function:: int selinux_netlbl_socket_setsockopt(struct socket *sock, int level, int optname)

    Do not allow users to remove a NetLabel

    :param struct socket \*sock:
        the socket

    :param int level:
        the socket level or protocol

    :param int optname:
        the socket option name

.. _`selinux_netlbl_socket_setsockopt.description`:

Description
-----------

Check the \ :c:func:`setsockopt`\  call and if the user is trying to replace the IP
options on a socket and a NetLabel is in place for the socket deny the
access; otherwise allow the access.  Returns zero when the access is
allowed, -EACCES when denied, and other negative values on error.

.. _`selinux_netlbl_socket_connect`:

selinux_netlbl_socket_connect
=============================

.. c:function:: int selinux_netlbl_socket_connect(struct sock *sk, struct sockaddr *addr)

    Label a client-side socket on connect

    :param struct sock \*sk:
        the socket to label

    :param struct sockaddr \*addr:
        the destination address

.. _`selinux_netlbl_socket_connect.description`:

Description
-----------

Attempt to label a connected socket with NetLabel using the given address.
Returns zero values on success, negative values on failure.

.. This file was automatic generated / don't edit.

