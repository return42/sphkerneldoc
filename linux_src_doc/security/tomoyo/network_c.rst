.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/network.c

.. _`tomoyo_parse_ipaddr_union`:

tomoyo_parse_ipaddr_union
=========================

.. c:function:: bool tomoyo_parse_ipaddr_union(struct tomoyo_acl_param *param, struct tomoyo_ipaddr_union *ptr)

    Parse an IP address.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

    :param ptr:
        Pointer to "struct tomoyo_ipaddr_union".
    :type ptr: struct tomoyo_ipaddr_union \*

.. _`tomoyo_parse_ipaddr_union.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_print_ipv4`:

tomoyo_print_ipv4
=================

.. c:function:: void tomoyo_print_ipv4(char *buffer, const unsigned int buffer_len, const __be32 *min_ip, const __be32 *max_ip)

    Print an IPv4 address.

    :param buffer:
        Buffer to write to.
    :type buffer: char \*

    :param buffer_len:
        Size of \ ``buffer``\ .
    :type buffer_len: const unsigned int

    :param min_ip:
        Pointer to \__be32.
    :type min_ip: const __be32 \*

    :param max_ip:
        Pointer to \__be32.
    :type max_ip: const __be32 \*

.. _`tomoyo_print_ipv4.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_print_ipv6`:

tomoyo_print_ipv6
=================

.. c:function:: void tomoyo_print_ipv6(char *buffer, const unsigned int buffer_len, const struct in6_addr *min_ip, const struct in6_addr *max_ip)

    Print an IPv6 address.

    :param buffer:
        Buffer to write to.
    :type buffer: char \*

    :param buffer_len:
        Size of \ ``buffer``\ .
    :type buffer_len: const unsigned int

    :param min_ip:
        Pointer to "struct in6_addr".
    :type min_ip: const struct in6_addr \*

    :param max_ip:
        Pointer to "struct in6_addr".
    :type max_ip: const struct in6_addr \*

.. _`tomoyo_print_ipv6.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_print_ip`:

tomoyo_print_ip
===============

.. c:function:: void tomoyo_print_ip(char *buf, const unsigned int size, const struct tomoyo_ipaddr_union *ptr)

    Print an IP address.

    :param buf:
        Buffer to write to.
    :type buf: char \*

    :param size:
        Size of \ ``buf``\ .
    :type size: const unsigned int

    :param ptr:
        Pointer to "struct ipaddr_union".
    :type ptr: const struct tomoyo_ipaddr_union \*

.. _`tomoyo_print_ip.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_same_inet_acl`:

tomoyo_same_inet_acl
====================

.. c:function:: bool tomoyo_same_inet_acl(const struct tomoyo_acl_info *a, const struct tomoyo_acl_info *b)

    Check for duplicated "struct tomoyo_inet_acl" entry.

    :param a:
        Pointer to "struct tomoyo_acl_info".
    :type a: const struct tomoyo_acl_info \*

    :param b:
        Pointer to "struct tomoyo_acl_info".
    :type b: const struct tomoyo_acl_info \*

.. _`tomoyo_same_inet_acl.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\  except permission bits, false otherwise.

.. _`tomoyo_same_unix_acl`:

tomoyo_same_unix_acl
====================

.. c:function:: bool tomoyo_same_unix_acl(const struct tomoyo_acl_info *a, const struct tomoyo_acl_info *b)

    Check for duplicated "struct tomoyo_unix_acl" entry.

    :param a:
        Pointer to "struct tomoyo_acl_info".
    :type a: const struct tomoyo_acl_info \*

    :param b:
        Pointer to "struct tomoyo_acl_info".
    :type b: const struct tomoyo_acl_info \*

.. _`tomoyo_same_unix_acl.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\  except permission bits, false otherwise.

.. _`tomoyo_merge_inet_acl`:

tomoyo_merge_inet_acl
=====================

.. c:function:: bool tomoyo_merge_inet_acl(struct tomoyo_acl_info *a, struct tomoyo_acl_info *b, const bool is_delete)

    Merge duplicated "struct tomoyo_inet_acl" entry.

    :param a:
        Pointer to "struct tomoyo_acl_info".
    :type a: struct tomoyo_acl_info \*

    :param b:
        Pointer to "struct tomoyo_acl_info".
    :type b: struct tomoyo_acl_info \*

    :param is_delete:
        True for \ ``a``\  &= ~@b, false for \ ``a``\  \|= \ ``b``\ .
    :type is_delete: const bool

.. _`tomoyo_merge_inet_acl.description`:

Description
-----------

Returns true if \ ``a``\  is empty, false otherwise.

.. _`tomoyo_merge_unix_acl`:

tomoyo_merge_unix_acl
=====================

.. c:function:: bool tomoyo_merge_unix_acl(struct tomoyo_acl_info *a, struct tomoyo_acl_info *b, const bool is_delete)

    Merge duplicated "struct tomoyo_unix_acl" entry.

    :param a:
        Pointer to "struct tomoyo_acl_info".
    :type a: struct tomoyo_acl_info \*

    :param b:
        Pointer to "struct tomoyo_acl_info".
    :type b: struct tomoyo_acl_info \*

    :param is_delete:
        True for \ ``a``\  &= ~@b, false for \ ``a``\  \|= \ ``b``\ .
    :type is_delete: const bool

.. _`tomoyo_merge_unix_acl.description`:

Description
-----------

Returns true if \ ``a``\  is empty, false otherwise.

.. _`tomoyo_write_inet_network`:

tomoyo_write_inet_network
=========================

.. c:function:: int tomoyo_write_inet_network(struct tomoyo_acl_param *param)

    Write "struct tomoyo_inet_acl" list.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

.. _`tomoyo_write_inet_network.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_write_unix_network`:

tomoyo_write_unix_network
=========================

.. c:function:: int tomoyo_write_unix_network(struct tomoyo_acl_param *param)

    Write "struct tomoyo_unix_acl" list.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

.. _`tomoyo_write_unix_network.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_audit_net_log`:

tomoyo_audit_net_log
====================

.. c:function:: int tomoyo_audit_net_log(struct tomoyo_request_info *r, const char *family, const u8 protocol, const u8 operation, const char *address)

    Audit network log.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param family:
        Name of socket family ("inet" or "unix").
    :type family: const char \*

    :param protocol:
        Name of protocol in \ ``family``\ .
    :type protocol: const u8

    :param operation:
        Name of socket operation.
    :type operation: const u8

    :param address:
        Name of address.
    :type address: const char \*

.. _`tomoyo_audit_net_log.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_audit_inet_log`:

tomoyo_audit_inet_log
=====================

.. c:function:: int tomoyo_audit_inet_log(struct tomoyo_request_info *r)

    Audit INET network log.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

.. _`tomoyo_audit_inet_log.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_audit_unix_log`:

tomoyo_audit_unix_log
=====================

.. c:function:: int tomoyo_audit_unix_log(struct tomoyo_request_info *r)

    Audit UNIX network log.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

.. _`tomoyo_audit_unix_log.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_check_inet_acl`:

tomoyo_check_inet_acl
=====================

.. c:function:: bool tomoyo_check_inet_acl(struct tomoyo_request_info *r, const struct tomoyo_acl_info *ptr)

    Check permission for inet domain socket operation.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param ptr:
        Pointer to "struct tomoyo_acl_info".
    :type ptr: const struct tomoyo_acl_info \*

.. _`tomoyo_check_inet_acl.description`:

Description
-----------

Returns true if granted, false otherwise.

.. _`tomoyo_check_unix_acl`:

tomoyo_check_unix_acl
=====================

.. c:function:: bool tomoyo_check_unix_acl(struct tomoyo_request_info *r, const struct tomoyo_acl_info *ptr)

    Check permission for unix domain socket operation.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param ptr:
        Pointer to "struct tomoyo_acl_info".
    :type ptr: const struct tomoyo_acl_info \*

.. _`tomoyo_check_unix_acl.description`:

Description
-----------

Returns true if granted, false otherwise.

.. _`tomoyo_inet_entry`:

tomoyo_inet_entry
=================

.. c:function:: int tomoyo_inet_entry(const struct tomoyo_addr_info *address)

    Check permission for INET network operation.

    :param address:
        Pointer to "struct tomoyo_addr_info".
    :type address: const struct tomoyo_addr_info \*

.. _`tomoyo_inet_entry.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_check_inet_address`:

tomoyo_check_inet_address
=========================

.. c:function:: int tomoyo_check_inet_address(const struct sockaddr *addr, const unsigned int addr_len, const u16 port, struct tomoyo_addr_info *address)

    Check permission for inet domain socket's operation.

    :param addr:
        Pointer to "struct sockaddr".
    :type addr: const struct sockaddr \*

    :param addr_len:
        Size of \ ``addr``\ .
    :type addr_len: const unsigned int

    :param port:
        Port number.
    :type port: const u16

    :param address:
        Pointer to "struct tomoyo_addr_info".
    :type address: struct tomoyo_addr_info \*

.. _`tomoyo_check_inet_address.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_unix_entry`:

tomoyo_unix_entry
=================

.. c:function:: int tomoyo_unix_entry(const struct tomoyo_addr_info *address)

    Check permission for UNIX network operation.

    :param address:
        Pointer to "struct tomoyo_addr_info".
    :type address: const struct tomoyo_addr_info \*

.. _`tomoyo_unix_entry.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_check_unix_address`:

tomoyo_check_unix_address
=========================

.. c:function:: int tomoyo_check_unix_address(struct sockaddr *addr, const unsigned int addr_len, struct tomoyo_addr_info *address)

    Check permission for unix domain socket's operation.

    :param addr:
        Pointer to "struct sockaddr".
    :type addr: struct sockaddr \*

    :param addr_len:
        Size of \ ``addr``\ .
    :type addr_len: const unsigned int

    :param address:
        Pointer to "struct tomoyo_addr_info".
    :type address: struct tomoyo_addr_info \*

.. _`tomoyo_check_unix_address.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_kernel_service`:

tomoyo_kernel_service
=====================

.. c:function:: bool tomoyo_kernel_service( void)

    Check whether I'm kernel service or not.

    :param void:
        no arguments
    :type void: 

.. _`tomoyo_kernel_service.description`:

Description
-----------

Returns true if I'm kernel service, false otherwise.

.. _`tomoyo_sock_family`:

tomoyo_sock_family
==================

.. c:function:: u8 tomoyo_sock_family(struct sock *sk)

    Get socket's family.

    :param sk:
        Pointer to "struct sock".
    :type sk: struct sock \*

.. _`tomoyo_sock_family.description`:

Description
-----------

Returns one of PF_INET, PF_INET6, PF_UNIX or 0.

.. _`tomoyo_socket_listen_permission`:

tomoyo_socket_listen_permission
===============================

.. c:function:: int tomoyo_socket_listen_permission(struct socket *sock)

    Check permission for listening a socket.

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

.. _`tomoyo_socket_listen_permission.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_connect_permission`:

tomoyo_socket_connect_permission
================================

.. c:function:: int tomoyo_socket_connect_permission(struct socket *sock, struct sockaddr *addr, int addr_len)

    Check permission for setting the remote address of a socket.

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

    :param addr:
        Pointer to "struct sockaddr".
    :type addr: struct sockaddr \*

    :param addr_len:
        Size of \ ``addr``\ .
    :type addr_len: int

.. _`tomoyo_socket_connect_permission.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_bind_permission`:

tomoyo_socket_bind_permission
=============================

.. c:function:: int tomoyo_socket_bind_permission(struct socket *sock, struct sockaddr *addr, int addr_len)

    Check permission for setting the local address of a socket.

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

    :param addr:
        Pointer to "struct sockaddr".
    :type addr: struct sockaddr \*

    :param addr_len:
        Size of \ ``addr``\ .
    :type addr_len: int

.. _`tomoyo_socket_bind_permission.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_sendmsg_permission`:

tomoyo_socket_sendmsg_permission
================================

.. c:function:: int tomoyo_socket_sendmsg_permission(struct socket *sock, struct msghdr *msg, int size)

    Check permission for sending a datagram.

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

    :param msg:
        Pointer to "struct msghdr".
    :type msg: struct msghdr \*

    :param size:
        Unused.
    :type size: int

.. _`tomoyo_socket_sendmsg_permission.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. This file was automatic generated / don't edit.

