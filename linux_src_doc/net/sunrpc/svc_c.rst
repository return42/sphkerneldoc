.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/svc.c

.. _`svc_register`:

svc_register
============

.. c:function:: int svc_register(const struct svc_serv *serv, struct net *net, const int family, const unsigned short proto, const unsigned short port)

    register an RPC service with the local portmapper

    :param const struct svc_serv \*serv:
        svc_serv struct for the service to register

    :param struct net \*net:
        net namespace for the service to register

    :param const int family:
        protocol family of service's listener socket

    :param const unsigned short proto:
        transport protocol number to advertise

    :param const unsigned short port:
        port to advertise

.. _`svc_register.description`:

Description
-----------

Service is registered for any address in the passed-in protocol family

.. _`svc_fill_write_vector`:

svc_fill_write_vector
=====================

.. c:function:: unsigned int svc_fill_write_vector(struct svc_rqst *rqstp, struct kvec *first, size_t total)

    Construct data argument for VFS write call

    :param struct svc_rqst \*rqstp:
        svc_rqst to operate on

    :param struct kvec \*first:
        buffer containing first section of write payload

    :param size_t total:
        total number of bytes of write payload

.. _`svc_fill_write_vector.description`:

Description
-----------

Returns the number of elements populated in the data argument array.

.. _`svc_fill_symlink_pathname`:

svc_fill_symlink_pathname
=========================

.. c:function:: char *svc_fill_symlink_pathname(struct svc_rqst *rqstp, struct kvec *first, size_t total)

    Construct pathname argument for VFS symlink call

    :param struct svc_rqst \*rqstp:
        svc_rqst to operate on

    :param struct kvec \*first:
        buffer containing first section of pathname

    :param size_t total:
        total length of the pathname argument

.. _`svc_fill_symlink_pathname.description`:

Description
-----------

Returns pointer to a NUL-terminated string, or an ERR_PTR. The buffer is
released automatically when \ ``rqstp``\  is recycled.

.. This file was automatic generated / don't edit.

