.. -*- coding: utf-8; mode: rst -*-

===========
transport.h
===========


.. _`p9_trans_module`:

struct p9_trans_module
======================

.. c:type:: p9_trans_module

    transport module interface


.. _`p9_trans_module.definition`:

Definition
----------

.. code-block:: c

  struct p9_trans_module {
    struct list_head list;
    char * name;
    int maxsize;
    int def;
    int (* create) (struct p9_client *, const char *, char *);
    void (* close) (struct p9_client *);
    int (* request) (struct p9_client *, struct p9_req_t *req);
    int (* cancel) (struct p9_client *, struct p9_req_t *req);
    int (* cancelled) (struct p9_client *, struct p9_req_t *req);
  };


.. _`p9_trans_module.members`:

Members
-------

:``list``:
    used to maintain a list of currently available transports

:``name``:
    the human-readable name of the transport

:``maxsize``:
    transport provided maximum packet size

:``def``:
    set if this transport should be considered the default

:``create``:
    member function to create a new connection on this transport

:``close``:
    member function to discard a connection on this transport

:``request``:
    member function to issue a request to the transport

:``cancel``:
    member function to cancel a request (if it hasn't been sent)

:``cancelled``:
    member function to notify that a cancelled request will not
    not receive a reply




.. _`p9_trans_module.description`:

Description
-----------

This is the basic API for a transport module which is registered by the
transport module with the 9P core network module and used by the client
to instantiate a new connection on a transport.

The transport module list is protected by v9fs_trans_lock.

