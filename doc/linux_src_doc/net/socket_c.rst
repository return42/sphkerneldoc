.. -*- coding: utf-8; mode: rst -*-

========
socket.c
========

.. _`move_addr_to_kernel`:

move_addr_to_kernel
===================

.. c:function:: int move_addr_to_kernel (void __user *uaddr, int ulen, struct sockaddr_storage *kaddr)

    copy a socket address into kernel space

    :param void __user \*uaddr:
        Address in user space

    :param int ulen:
        Length in user space

    :param struct sockaddr_storage \*kaddr:
        Address in kernel space


.. _`move_addr_to_kernel.description`:

Description
-----------

The address is copied into kernel space. If the provided address is
too long an error code of -EINVAL is returned. If the copy gives
invalid addresses -EFAULT is returned. On a success 0 is returned.


.. _`move_addr_to_user`:

move_addr_to_user
=================

.. c:function:: int move_addr_to_user (struct sockaddr_storage *kaddr, int klen, void __user *uaddr, int __user *ulen)

    copy an address to user space

    :param struct sockaddr_storage \*kaddr:
        kernel space address

    :param int klen:
        length of address in kernel

    :param void __user \*uaddr:
        user space address

    :param int __user \*ulen:
        pointer to user length field


.. _`move_addr_to_user.description`:

Description
-----------

The value pointed to by ulen on entry is the buffer length available.
This is overwritten with the buffer space used. -EINVAL is returned
if an overlong buffer is specified or a negative buffer size. -EFAULT
is returned if either the buffer or the length field are not
accessible.
After copying the data up to the limit the user specifies, the true
length of the data is written over the length limit the user
specified. Zero is returned for a success.


.. _`sockfd_lookup`:

sockfd_lookup
=============

.. c:function:: struct socket *sockfd_lookup (int fd, int *err)

    Go from a file number to its socket slot

    :param int fd:
        file handle

    :param int \*err:
        pointer to an error code return


.. _`sockfd_lookup.description`:

Description
-----------

The file handle passed in is locked and the socket it is bound
too is returned. If an error occurs the err pointer is overwritten
with a negative errno code and NULL is returned. The function checks
for both invalid handles and passing a handle which is not a socket.

On a success the socket object pointer is returned.


.. _`sock_alloc`:

sock_alloc
==========

.. c:function:: struct socket *sock_alloc ( void)

    allocate a socket

    :param void:
        no arguments


.. _`sock_alloc.description`:

Description
-----------


Allocate a new inode and socket object. The two are bound together
and initialised. The socket is then returned. If we are out of inodes
NULL is returned.


.. _`sock_release`:

sock_release
============

.. c:function:: void sock_release (struct socket *sock)

    close a socket

    :param struct socket \*sock:
        socket to close


.. _`sock_release.description`:

Description
-----------

The socket is released from the protocol stack if it has a release
callback, and the inode is then released if the socket is bound to
an inode not a file.


.. _`kernel_recvmsg`:

kernel_recvmsg
==============

.. c:function:: int kernel_recvmsg (struct socket *sock, struct msghdr *msg, struct kvec *vec, size_t num, size_t size, int flags)

    Receive a message from a socket (kernel space)

    :param struct socket \*sock:
        The socket to receive the message from

    :param struct msghdr \*msg:
        Received message

    :param struct kvec \*vec:
        Input s/g array for message data

    :param size_t num:
        Size of input s/g array

    :param size_t size:
        Number of bytes to read

    :param int flags:
        Message flags (MSG_DONTWAIT, etc...)


.. _`kernel_recvmsg.description`:

Description
-----------

On return the msg structure contains the scatter/gather array passed in the
vec argument. The array is modified so that it consists of the unfilled
portion of the original array.

The returned value is the total number of bytes received, or an error.


.. _`sock_register`:

sock_register
=============

.. c:function:: int sock_register (const struct net_proto_family *ops)

    add a socket protocol handler

    :param const struct net_proto_family \*ops:
        description of protocol


.. _`sock_register.description`:

Description
-----------

This function is called by a protocol handler that wants to
advertise its address family, and have it linked into the
socket interface. The value ops->family corresponds to the
socket system call protocol family.


.. _`sock_unregister`:

sock_unregister
===============

.. c:function:: void sock_unregister (int family)

    remove a protocol handler

    :param int family:
        protocol family to remove


.. _`sock_unregister.description`:

Description
-----------

This function is called by a protocol handler that wants to
remove its address family, and have it unlinked from the
new socket creation.

If protocol handler is a module, then it can use module reference
counts to protect against new references. If protocol handler is not
a module then it needs to provide its own protection in
the ops->create routine.

