.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/9p/client.h

.. _`p9_trans_status`:

enum p9_trans_status
====================

.. c:type:: enum p9_trans_status

    different states of underlying transports

.. _`p9_trans_status.definition`:

Definition
----------

.. code-block:: c

    enum p9_trans_status {
        Connected,
        BeginDisconnect,
        Disconnected,
        Hung
    };

.. _`p9_trans_status.constants`:

Constants
---------

Connected
    transport is connected and healthy

BeginDisconnect
    *undescribed*

Disconnected
    transport has been disconnected

Hung
    transport is connected by wedged

.. _`p9_trans_status.description`:

Description
-----------

This enumeration details the various states a transport
instatiation can be in.

.. _`p9_req_status_t`:

enum p9_req_status_t
====================

.. c:type:: enum p9_req_status_t

    status of a request

.. _`p9_req_status_t.definition`:

Definition
----------

.. code-block:: c

    enum p9_req_status_t {
        REQ_STATUS_ALLOC,
        REQ_STATUS_UNSENT,
        REQ_STATUS_SENT,
        REQ_STATUS_RCVD,
        REQ_STATUS_FLSHD,
        REQ_STATUS_ERROR
    };

.. _`p9_req_status_t.constants`:

Constants
---------

REQ_STATUS_ALLOC
    request has been allocated but not sent

REQ_STATUS_UNSENT
    request waiting to be sent

REQ_STATUS_SENT
    request sent to server

REQ_STATUS_RCVD
    response received from server

REQ_STATUS_FLSHD
    request has been flushed

REQ_STATUS_ERROR
    request encountered an error on the client side

.. _`p9_req_t`:

struct p9_req_t
===============

.. c:type:: struct p9_req_t

    request slots

.. _`p9_req_t.definition`:

Definition
----------

.. code-block:: c

    struct p9_req_t {
        int status;
        int t_err;
        struct kref refcount;
        wait_queue_head_t wq;
        struct p9_fcall tc;
        struct p9_fcall rc;
        void *aux;
        struct list_head req_list;
    }

.. _`p9_req_t.members`:

Members
-------

status
    status of this request slot

t_err
    transport error

refcount
    *undescribed*

wq
    wait_queue for the client to block on for this request

tc
    the request fcall structure

rc
    the response fcall structure

aux
    transport specific data (provided for trans_fd migration)

req_list
    link for higher level objects to chain requests

.. _`p9_client`:

struct p9_client
================

.. c:type:: struct p9_client

    per client instance state

.. _`p9_client.definition`:

Definition
----------

.. code-block:: c

    struct p9_client {
        spinlock_t lock;
        unsigned int msize;
        unsigned char proto_version;
        struct p9_trans_module *trans_mod;
        enum p9_trans_status status;
        void *trans;
        struct kmem_cache *fcall_cache;
        union {
            struct {
                int rfd;
                int wfd;
            } fd;
            struct {
                u16 port;
                bool privport;
            } tcp;
        } trans_opts;
        struct idr fids;
        struct idr reqs;
        char name[__NEW_UTS_LEN + 1];
    }

.. _`p9_client.members`:

Members
-------

lock
    protect \ ``fids``\  and \ ``reqs``\ 

msize
    maximum data size negotiated by protocol

proto_version
    9P protocol version to use

trans_mod
    module API instantiated with this client

status
    connection state

trans
    tranport instance state and API

fcall_cache
    *undescribed*

trans_opts
    *undescribed*

fids
    All active FID handles

reqs
    All active requests.

name
    node name used as client id

.. _`p9_client.description`:

Description
-----------

The client structure is used to keep track of various per-client
state that has been instantiated.

.. _`p9_fid`:

struct p9_fid
=============

.. c:type:: struct p9_fid

    file system entity handle

.. _`p9_fid.definition`:

Definition
----------

.. code-block:: c

    struct p9_fid {
        struct p9_client *clnt;
        u32 fid;
        int mode;
        struct p9_qid qid;
        u32 iounit;
        kuid_t uid;
        void *rdir;
        struct hlist_node dlist;
    }

.. _`p9_fid.members`:

Members
-------

clnt
    back pointer to instantiating \ :c:type:`struct p9_client <p9_client>`\ 

fid
    numeric identifier for this handle

mode
    current mode of this fid (enum?)

qid
    the \ :c:type:`struct p9_qid <p9_qid>`\  server identifier this handle points to

iounit
    the server reported maximum transaction size for this file

uid
    the numeric uid of the local user who owns this handle

rdir
    readdir accounting structure (allocated on demand)

dlist
    per-dentry fid tracking

.. _`p9_fid.todo`:

TODO
----

This needs lots of explanation.

.. _`p9_dirent`:

struct p9_dirent
================

.. c:type:: struct p9_dirent

    directory entry structure

.. _`p9_dirent.definition`:

Definition
----------

.. code-block:: c

    struct p9_dirent {
        struct p9_qid qid;
        u64 d_off;
        unsigned char d_type;
        char d_name[256];
    }

.. _`p9_dirent.members`:

Members
-------

qid
    The p9 server qid for this dirent

d_off
    offset to the next dirent

d_type
    type of file

d_name
    file name

.. This file was automatic generated / don't edit.

