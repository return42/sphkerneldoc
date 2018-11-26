.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/svc.c

.. _`svc_register`:

svc_register
============

.. c:function:: int svc_register(const struct svc_serv *serv, struct net *net, const int family, const unsigned short proto, const unsigned short port)

    register an RPC service with the local portmapper

    :param serv:
        svc_serv struct for the service to register
    :type serv: const struct svc_serv \*

    :param net:
        net namespace for the service to register
    :type net: struct net \*

    :param family:
        protocol family of service's listener socket
    :type family: const int

    :param proto:
        transport protocol number to advertise
    :type proto: const unsigned short

    :param port:
        port to advertise
    :type port: const unsigned short

.. _`svc_register.description`:

Description
-----------

Service is registered for any address in the passed-in protocol family

.. _`svc_fill_write_vector`:

svc_fill_write_vector
=====================

.. c:function:: unsigned int svc_fill_write_vector(struct svc_rqst *rqstp, struct page **pages, struct kvec *first, size_t total)

    Construct data argument for VFS write call

    :param rqstp:
        svc_rqst to operate on
    :type rqstp: struct svc_rqst \*

    :param pages:
        list of pages containing data payload
    :type pages: struct page \*\*

    :param first:
        buffer containing first section of write payload
    :type first: struct kvec \*

    :param total:
        total number of bytes of write payload
    :type total: size_t

.. _`svc_fill_write_vector.description`:

Description
-----------

Fills in rqstp::rq_vec, and returns the number of elements.

.. _`svc_fill_symlink_pathname`:

svc_fill_symlink_pathname
=========================

.. c:function:: char *svc_fill_symlink_pathname(struct svc_rqst *rqstp, struct kvec *first, void *p, size_t total)

    Construct pathname argument for VFS symlink call

    :param rqstp:
        svc_rqst to operate on
    :type rqstp: struct svc_rqst \*

    :param first:
        buffer containing first section of pathname
    :type first: struct kvec \*

    :param p:
        buffer containing remaining section of pathname
    :type p: void \*

    :param total:
        total length of the pathname argument
    :type total: size_t

.. _`svc_fill_symlink_pathname.description`:

Description
-----------

The VFS symlink API demands a NUL-terminated pathname in mapped memory.
Returns pointer to a NUL-terminated string, or an ERR_PTR. Caller must free
the returned string.

.. This file was automatic generated / don't edit.

