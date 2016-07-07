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

.. This file was automatic generated / don't edit.

