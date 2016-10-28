.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/svcsock.c

.. _`svc_addsock`:

svc_addsock
===========

.. c:function:: int svc_addsock(struct svc_serv *serv, const int fd, char *name_return, const size_t len)

    add a listener socket to an RPC service

    :param struct svc_serv \*serv:
        pointer to RPC service to which to add a new listener

    :param const int fd:
        file descriptor of the new listener

    :param char \*name_return:
        pointer to buffer to fill in with name of listener

    :param const size_t len:
        size of the buffer

.. _`svc_addsock.description`:

Description
-----------

Fills in socket name and returns positive length of name if successful.
Name is terminated with '\n'.  On error, returns a negative errno
value.

.. This file was automatic generated / don't edit.

