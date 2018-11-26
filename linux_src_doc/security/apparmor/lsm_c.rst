.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/lsm.c

.. _`common_perm`:

common_perm
===========

.. c:function:: int common_perm(const char *op, const struct path *path, u32 mask, struct path_cond *cond)

    basic common permission check wrapper fn for paths

    :param op:
        operation being checked
    :type op: const char \*

    :param path:
        path to check permission of  (NOT NULL)
    :type path: const struct path \*

    :param mask:
        requested permissions mask
    :type mask: u32

    :param cond:
        conditional info for the permission request  (NOT NULL)
    :type cond: struct path_cond \*

.. _`common_perm.return`:

Return
------

\ ``0``\  else error code if error or permission denied

.. _`common_perm_cond`:

common_perm_cond
================

.. c:function:: int common_perm_cond(const char *op, const struct path *path, u32 mask)

    common permission wrapper around inode cond

    :param op:
        operation being checked
    :type op: const char \*

    :param path:
        location to check (NOT NULL)
    :type path: const struct path \*

    :param mask:
        requested permissions mask
    :type mask: u32

.. _`common_perm_cond.return`:

Return
------

\ ``0``\  else error code if error or permission denied

.. _`common_perm_dir_dentry`:

common_perm_dir_dentry
======================

.. c:function:: int common_perm_dir_dentry(const char *op, const struct path *dir, struct dentry *dentry, u32 mask, struct path_cond *cond)

    common permission wrapper when path is dir, dentry

    :param op:
        operation being checked
    :type op: const char \*

    :param dir:
        directory of the dentry  (NOT NULL)
    :type dir: const struct path \*

    :param dentry:
        dentry to check  (NOT NULL)
    :type dentry: struct dentry \*

    :param mask:
        requested permissions mask
    :type mask: u32

    :param cond:
        conditional info for the permission request  (NOT NULL)
    :type cond: struct path_cond \*

.. _`common_perm_dir_dentry.return`:

Return
------

\ ``0``\  else error code if error or permission denied

.. _`common_perm_rm`:

common_perm_rm
==============

.. c:function:: int common_perm_rm(const char *op, const struct path *dir, struct dentry *dentry, u32 mask)

    common permission wrapper for operations doing rm

    :param op:
        operation being checked
    :type op: const char \*

    :param dir:
        directory that the dentry is in  (NOT NULL)
    :type dir: const struct path \*

    :param dentry:
        dentry being rm'd  (NOT NULL)
    :type dentry: struct dentry \*

    :param mask:
        requested permission mask
    :type mask: u32

.. _`common_perm_rm.return`:

Return
------

\ ``0``\  else error code if error or permission denied

.. _`common_perm_create`:

common_perm_create
==================

.. c:function:: int common_perm_create(const char *op, const struct path *dir, struct dentry *dentry, u32 mask, umode_t mode)

    common permission wrapper for operations doing create

    :param op:
        operation being checked
    :type op: const char \*

    :param dir:
        directory that dentry will be created in  (NOT NULL)
    :type dir: const struct path \*

    :param dentry:
        dentry to create   (NOT NULL)
    :type dentry: struct dentry \*

    :param mask:
        request permission mask
    :type mask: u32

    :param mode:
        created file mode
    :type mode: umode_t

.. _`common_perm_create.return`:

Return
------

\ ``0``\  else error code if error or permission denied

.. _`apparmor_bprm_committing_creds`:

apparmor_bprm_committing_creds
==============================

.. c:function:: void apparmor_bprm_committing_creds(struct linux_binprm *bprm)

    do task cleanup on committing new creds

    :param bprm:
        binprm for the exec  (NOT NULL)
    :type bprm: struct linux_binprm \*

.. _`apparmor_bprm_committed_creds`:

apparmor_bprm_committed_creds
=============================

.. c:function:: void apparmor_bprm_committed_creds(struct linux_binprm *bprm)

    do cleanup after new creds committed

    :param bprm:
        binprm for the exec  (NOT NULL)
    :type bprm: struct linux_binprm \*

.. _`apparmor_sk_alloc_security`:

apparmor_sk_alloc_security
==========================

.. c:function:: int apparmor_sk_alloc_security(struct sock *sk, int family, gfp_t flags)

    allocate and attach the sk_security field

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param family:
        *undescribed*
    :type family: int

    :param flags:
        *undescribed*
    :type flags: gfp_t

.. _`apparmor_sk_free_security`:

apparmor_sk_free_security
=========================

.. c:function:: void apparmor_sk_free_security(struct sock *sk)

    free the sk_security field

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`apparmor_sk_clone_security`:

apparmor_sk_clone_security
==========================

.. c:function:: void apparmor_sk_clone_security(const struct sock *sk, struct sock *newsk)

    clone the sk_security field

    :param sk:
        *undescribed*
    :type sk: const struct sock \*

    :param newsk:
        *undescribed*
    :type newsk: struct sock \*

.. _`apparmor_socket_create`:

apparmor_socket_create
======================

.. c:function:: int apparmor_socket_create(int family, int type, int protocol, int kern)

    check perms before creating a new socket

    :param family:
        *undescribed*
    :type family: int

    :param type:
        *undescribed*
    :type type: int

    :param protocol:
        *undescribed*
    :type protocol: int

    :param kern:
        *undescribed*
    :type kern: int

.. _`apparmor_socket_post_create`:

apparmor_socket_post_create
===========================

.. c:function:: int apparmor_socket_post_create(struct socket *sock, int family, int type, int protocol, int kern)

    setup the per-socket security struct

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param family:
        *undescribed*
    :type family: int

    :param type:
        *undescribed*
    :type type: int

    :param protocol:
        *undescribed*
    :type protocol: int

    :param kern:
        *undescribed*
    :type kern: int

.. _`apparmor_socket_post_create.note`:

Note
----

-   kernel sockets currently labeled unconfined but we may want to
move to a special kernel label
-   socket may not have sk here if created with sock_create_lite or
sock_alloc. These should be accept cases which will be handled in
sock_graft.

.. _`apparmor_socket_bind`:

apparmor_socket_bind
====================

.. c:function:: int apparmor_socket_bind(struct socket *sock, struct sockaddr *address, int addrlen)

    check perms before bind addr to socket

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param address:
        *undescribed*
    :type address: struct sockaddr \*

    :param addrlen:
        *undescribed*
    :type addrlen: int

.. _`apparmor_socket_connect`:

apparmor_socket_connect
=======================

.. c:function:: int apparmor_socket_connect(struct socket *sock, struct sockaddr *address, int addrlen)

    check perms before connecting \ ``sock``\  to \ ``address``\ 

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param address:
        *undescribed*
    :type address: struct sockaddr \*

    :param addrlen:
        *undescribed*
    :type addrlen: int

.. _`apparmor_socket_listen`:

apparmor_socket_listen
======================

.. c:function:: int apparmor_socket_listen(struct socket *sock, int backlog)

    check perms before allowing listen

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param backlog:
        *undescribed*
    :type backlog: int

.. _`apparmor_socket_accept`:

apparmor_socket_accept
======================

.. c:function:: int apparmor_socket_accept(struct socket *sock, struct socket *newsock)

    check perms before accepting a new connection.

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param newsock:
        *undescribed*
    :type newsock: struct socket \*

.. _`apparmor_socket_accept.note`:

Note
----

while \ ``newsock``\  is created and has some information, the accept
has not been done.

.. _`apparmor_socket_sendmsg`:

apparmor_socket_sendmsg
=======================

.. c:function:: int apparmor_socket_sendmsg(struct socket *sock, struct msghdr *msg, int size)

    check perms before sending msg to another socket

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param msg:
        *undescribed*
    :type msg: struct msghdr \*

    :param size:
        *undescribed*
    :type size: int

.. _`apparmor_socket_recvmsg`:

apparmor_socket_recvmsg
=======================

.. c:function:: int apparmor_socket_recvmsg(struct socket *sock, struct msghdr *msg, int size, int flags)

    check perms before receiving a message

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param msg:
        *undescribed*
    :type msg: struct msghdr \*

    :param size:
        *undescribed*
    :type size: int

    :param flags:
        *undescribed*
    :type flags: int

.. _`apparmor_socket_getsockname`:

apparmor_socket_getsockname
===========================

.. c:function:: int apparmor_socket_getsockname(struct socket *sock)

    check perms before getting the local address

    :param sock:
        *undescribed*
    :type sock: struct socket \*

.. _`apparmor_socket_getpeername`:

apparmor_socket_getpeername
===========================

.. c:function:: int apparmor_socket_getpeername(struct socket *sock)

    check perms before getting remote address

    :param sock:
        *undescribed*
    :type sock: struct socket \*

.. _`apparmor_socket_getsockopt`:

apparmor_socket_getsockopt
==========================

.. c:function:: int apparmor_socket_getsockopt(struct socket *sock, int level, int optname)

    check perms before getting socket options

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param level:
        *undescribed*
    :type level: int

    :param optname:
        *undescribed*
    :type optname: int

.. _`apparmor_socket_setsockopt`:

apparmor_socket_setsockopt
==========================

.. c:function:: int apparmor_socket_setsockopt(struct socket *sock, int level, int optname)

    check perms before setting socket options

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param level:
        *undescribed*
    :type level: int

    :param optname:
        *undescribed*
    :type optname: int

.. _`apparmor_socket_shutdown`:

apparmor_socket_shutdown
========================

.. c:function:: int apparmor_socket_shutdown(struct socket *sock, int how)

    check perms before shutting down \ ``sock``\  conn

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param how:
        *undescribed*
    :type how: int

.. _`apparmor_socket_sock_rcv_skb`:

apparmor_socket_sock_rcv_skb
============================

.. c:function:: int apparmor_socket_sock_rcv_skb(struct sock *sk, struct sk_buff *skb)

    check perms before associating skb to sk

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`apparmor_socket_sock_rcv_skb.note`:

Note
----

can not sleep may be called with locks held

dont want protocol specific in \__skb_recv_datagram()
to deny an incoming connection  \ :c:func:`socket_sock_rcv_skb`\ 

.. _`apparmor_socket_getpeersec_stream`:

apparmor_socket_getpeersec_stream
=================================

.. c:function:: int apparmor_socket_getpeersec_stream(struct socket *sock, char __user *optval, int __user *optlen, unsigned int len)

    get security context of peer

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param optval:
        *undescribed*
    :type optval: char __user \*

    :param optlen:
        *undescribed*
    :type optlen: int __user \*

    :param len:
        *undescribed*
    :type len: unsigned int

.. _`apparmor_socket_getpeersec_stream.note`:

Note
----

for tcp only valid if using ipsec or cipso on lan

.. _`apparmor_socket_getpeersec_dgram`:

apparmor_socket_getpeersec_dgram
================================

.. c:function:: int apparmor_socket_getpeersec_dgram(struct socket *sock, struct sk_buff *skb, u32 *secid)

    get security label of packet

    :param sock:
        the peer socket
    :type sock: struct socket \*

    :param skb:
        packet data
    :type skb: struct sk_buff \*

    :param secid:
        pointer to where to put the secid of the packet
    :type secid: u32 \*

.. _`apparmor_socket_getpeersec_dgram.description`:

Description
-----------

Sets the netlabel socket state on sk from parent

.. _`apparmor_sock_graft`:

apparmor_sock_graft
===================

.. c:function:: void apparmor_sock_graft(struct sock *sk, struct socket *parent)

    Initialize newly created socket

    :param sk:
        child sock
    :type sk: struct sock \*

    :param parent:
        parent socket
    :type parent: struct socket \*

.. _`apparmor_sock_graft.note`:

Note
----

could set off of SOCK_CTX(parent) but need to track inode and we can
just set sk security information off of current creating process label
Labeling of sk for accept case - probably should be sock based
instead of task, because of the case where an implicitly labeled
socket is shared by different tasks.

.. _`set_init_ctx`:

set_init_ctx
============

.. c:function:: int set_init_ctx( void)

    set a task context and profile on the first task.

    :param void:
        no arguments
    :type void: 

.. _`set_init_ctx.todo`:

TODO
----

allow setting an alternate profile than unconfined

.. This file was automatic generated / don't edit.

