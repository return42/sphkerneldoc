.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/9p/transport.h

.. _`p9_trans_module`:

struct p9_trans_module
======================

.. c:type:: struct p9_trans_module

    transport module interface

.. _`p9_trans_module.definition`:

Definition
----------

.. code-block:: c

    struct p9_trans_module {
        struct list_head list;
        char *name;
        int maxsize;
        int def;
        struct module *owner;
        int (*create)(struct p9_client *, const char *, char *);
        void (*close) (struct p9_client *);
        int (*request) (struct p9_client *, struct p9_req_t *req);
        int (*cancel) (struct p9_client *, struct p9_req_t *req);
        int (*cancelled)(struct p9_client *, struct p9_req_t *req);
        int (*zc_request)(struct p9_client *, struct p9_req_t *, struct iov_iter *, struct iov_iter *, int , int, int);
        int (*show_options)(struct seq_file *, struct p9_client *);
    }

.. _`p9_trans_module.members`:

Members
-------

list
    used to maintain a list of currently available transports

name
    the human-readable name of the transport

maxsize
    transport provided maximum packet size

def
    set if this transport should be considered the default

owner
    *undescribed*

create
    member function to create a new connection on this transport

close
    member function to discard a connection on this transport

request
    member function to issue a request to the transport

cancel
    member function to cancel a request (if it hasn't been sent)

cancelled
    member function to notify that a cancelled request will not
    not receive a reply

zc_request
    *undescribed*

show_options
    *undescribed*

.. _`p9_trans_module.description`:

Description
-----------

This is the basic API for a transport module which is registered by the
transport module with the 9P core network module and used by the client
to instantiate a new connection on a transport.

The transport module list is protected by v9fs_trans_lock.

.. This file was automatic generated / don't edit.

