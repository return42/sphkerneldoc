.. -*- coding: utf-8; mode: rst -*-

==========
svc_xprt.c
==========

.. _`svc_print_addr`:

svc_print_addr
==============

.. c:function:: char *svc_print_addr (struct svc_rqst *rqstp, char *buf, size_t len)

    Format rq_addr field for printing

    :param struct svc_rqst \*rqstp:
        svc_rqst struct containing address to print

    :param char \*buf:
        target buffer for formatted address

    :param size_t len:
        length of target buffer


.. _`svc_reserve`:

svc_reserve
===========

.. c:function:: void svc_reserve (struct svc_rqst *rqstp, int space)

    change the space reserved for the reply to a request.

    :param struct svc_rqst \*rqstp:
        The request in question

    :param int space:
        new max space to reserve


.. _`svc_reserve.description`:

Description
-----------

Each request reserves some space on the output queue of the transport
to make sure the reply fits.  This function reduces that reserved
space to be the amount of space used already, plus ``space``\ .


.. _`svc_find_xprt`:

svc_find_xprt
=============

.. c:function:: struct svc_xprt *svc_find_xprt (struct svc_serv *serv, const char *xcl_name, struct net *net, const sa_family_t af, const unsigned short port)

    find an RPC transport instance

    :param struct svc_serv \*serv:
        pointer to svc_serv to search

    :param const char \*xcl_name:
        C string containing transport's class name

    :param struct net \*net:
        owner net pointer

    :param const sa_family_t af:
        Address family of transport's local address

    :param const unsigned short port:
        transport's IP port number


.. _`svc_find_xprt.description`:

Description
-----------

Return the transport instance pointer for the endpoint accepting
connections/peer traffic from the specified transport class,
address family and port.

Specifying 0 for the address family or port is effectively a
wild-card, and will result in matching the first transport in the
service's list that has a matching class name.


.. _`svc_xprt_names`:

svc_xprt_names
==============

.. c:function:: int svc_xprt_names (struct svc_serv *serv, char *buf, const int buflen)

    format a buffer with a list of transport names

    :param struct svc_serv \*serv:
        pointer to an RPC service

    :param char \*buf:
        pointer to a buffer to be filled in

    :param const int buflen:
        length of buffer to be filled in


.. _`svc_xprt_names.description`:

Description
-----------

Fills in ``buf`` with a string containing a list of transport names,
each name terminated with '\n'.

Returns positive length of the filled-in string on success; otherwise
a negative errno value is returned if an error occurs.

