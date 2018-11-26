.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/svcsock.c

.. _`svc_addsock`:

svc_addsock
===========

.. c:function:: int svc_addsock(struct svc_serv *serv, const int fd, char *name_return, const size_t len)

    add a listener socket to an RPC service

    :param serv:
        pointer to RPC service to which to add a new listener
    :type serv: struct svc_serv \*

    :param fd:
        file descriptor of the new listener
    :type fd: const int

    :param name_return:
        pointer to buffer to fill in with name of listener
    :type name_return: char \*

    :param len:
        size of the buffer
    :type len: const size_t

.. _`svc_addsock.description`:

Description
-----------

Fills in socket name and returns positive length of name if successful.
Name is terminated with '\n'.  On error, returns a negative errno
value.

.. This file was automatic generated / don't edit.

