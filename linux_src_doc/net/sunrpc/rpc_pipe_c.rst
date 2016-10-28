.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/rpc_pipe.c

.. _`rpc_queue_upcall`:

rpc_queue_upcall
================

.. c:function:: int rpc_queue_upcall(struct rpc_pipe *pipe, struct rpc_pipe_msg *msg)

    queue an upcall message to userspace

    :param struct rpc_pipe \*pipe:
        upcall pipe on which to queue given message

    :param struct rpc_pipe_msg \*msg:
        message to queue

.. _`rpc_queue_upcall.description`:

Description
-----------

Call with an \ ``inode``\  created by \ :c:func:`rpc_mkpipe`\  to queue an upcall.
A userspace process may then later read the upcall by performing a
read on an open file for this inode.  It is up to the caller to
initialize the fields of \ ``msg``\  (other than \ ``msg``\ ->list) appropriately.

.. _`rpc_mkpipe_dentry`:

rpc_mkpipe_dentry
=================

.. c:function:: struct dentry *rpc_mkpipe_dentry(struct dentry *parent, const char *name, void *private, struct rpc_pipe *pipe)

    make an rpc_pipefs file for kernel<->userspace communication

    :param struct dentry \*parent:
        dentry of directory to create new "pipe" in

    :param const char \*name:
        name of pipe

    :param void \*private:
        private data to associate with the pipe, for the caller's use

    :param struct rpc_pipe \*pipe:
        \ :c:type:`struct rpc_pipe <rpc_pipe>` containing input parameters

.. _`rpc_mkpipe_dentry.description`:

Description
-----------

Data is made available for userspace to read by calls to
\ :c:func:`rpc_queue_upcall`\ .  The actual reads will result in calls to
\ ``ops``\ ->upcall, which will be called with the file pointer,
message, and userspace buffer to copy to.

Writes can come at any time, and do not necessarily have to be
responses to upcalls.  They will result in calls to \ ``msg``\ ->downcall.

The \ ``private``\  argument passed here will be available to all these methods
from the file pointer, via RPC_I(file_inode(file))->private.

.. _`rpc_unlink`:

rpc_unlink
==========

.. c:function:: int rpc_unlink(struct dentry *dentry)

    remove a pipe

    :param struct dentry \*dentry:
        dentry for the pipe, as returned from rpc_mkpipe

.. _`rpc_unlink.description`:

Description
-----------

After this call, lookups will no longer find the pipe, and any
attempts to read or write using preexisting opens of the pipe will
return -EPIPE.

.. _`rpc_init_pipe_dir_head`:

rpc_init_pipe_dir_head
======================

.. c:function:: void rpc_init_pipe_dir_head(struct rpc_pipe_dir_head *pdh)

    initialise a struct rpc_pipe_dir_head

    :param struct rpc_pipe_dir_head \*pdh:
        pointer to struct rpc_pipe_dir_head

.. _`rpc_init_pipe_dir_object`:

rpc_init_pipe_dir_object
========================

.. c:function:: void rpc_init_pipe_dir_object(struct rpc_pipe_dir_object *pdo, const struct rpc_pipe_dir_object_ops *pdo_ops, void *pdo_data)

    initialise a struct rpc_pipe_dir_object

    :param struct rpc_pipe_dir_object \*pdo:
        pointer to struct rpc_pipe_dir_object

    :param const struct rpc_pipe_dir_object_ops \*pdo_ops:
        pointer to const struct rpc_pipe_dir_object_ops

    :param void \*pdo_data:
        pointer to caller-defined data

.. _`rpc_add_pipe_dir_object`:

rpc_add_pipe_dir_object
=======================

.. c:function:: int rpc_add_pipe_dir_object(struct net *net, struct rpc_pipe_dir_head *pdh, struct rpc_pipe_dir_object *pdo)

    associate a rpc_pipe_dir_object to a directory

    :param struct net \*net:
        pointer to struct net

    :param struct rpc_pipe_dir_head \*pdh:
        pointer to struct rpc_pipe_dir_head

    :param struct rpc_pipe_dir_object \*pdo:
        pointer to struct rpc_pipe_dir_object

.. _`rpc_remove_pipe_dir_object`:

rpc_remove_pipe_dir_object
==========================

.. c:function:: void rpc_remove_pipe_dir_object(struct net *net, struct rpc_pipe_dir_head *pdh, struct rpc_pipe_dir_object *pdo)

    remove a rpc_pipe_dir_object from a directory

    :param struct net \*net:
        pointer to struct net

    :param struct rpc_pipe_dir_head \*pdh:
        pointer to struct rpc_pipe_dir_head

    :param struct rpc_pipe_dir_object \*pdo:
        pointer to struct rpc_pipe_dir_object

.. _`rpc_find_or_alloc_pipe_dir_object`:

rpc_find_or_alloc_pipe_dir_object
=================================

.. c:function:: struct rpc_pipe_dir_object *rpc_find_or_alloc_pipe_dir_object(struct net *net, struct rpc_pipe_dir_head *pdh, int (*match)(struct rpc_pipe_dir_object *, void *), struct rpc_pipe_dir_object *(*alloc)(void *), void *data)

    :param struct net \*net:
        pointer to struct net

    :param struct rpc_pipe_dir_head \*pdh:
        pointer to struct rpc_pipe_dir_head

    :param int (\*match)(struct rpc_pipe_dir_object \*, void \*):
        match struct rpc_pipe_dir_object to data

    :param struct rpc_pipe_dir_object \*(\*alloc)(void \*):
        allocate a new struct rpc_pipe_dir_object

    :param void \*data:
        user defined data for \ :c:func:`match`\  and \ :c:func:`alloc`\ 

.. _`rpc_create_client_dir`:

rpc_create_client_dir
=====================

.. c:function:: struct dentry *rpc_create_client_dir(struct dentry *dentry, const char *name, struct rpc_clnt *rpc_client)

    Create a new rpc_client directory in rpc_pipefs

    :param struct dentry \*dentry:
        the parent of new directory

    :param const char \*name:
        the name of new directory

    :param struct rpc_clnt \*rpc_client:
        rpc client to associate with this directory

.. _`rpc_create_client_dir.description`:

Description
-----------

This creates a directory at the given \ ``path``\  associated with
\ ``rpc_clnt``\ , which will contain a file named "info" with some basic
information about the client, together with any "pipes" that may
later be created using \ :c:func:`rpc_mkpipe`\ .

.. _`rpc_remove_client_dir`:

rpc_remove_client_dir
=====================

.. c:function:: int rpc_remove_client_dir(struct rpc_clnt *rpc_client)

    Remove a directory created with \ :c:func:`rpc_create_client_dir`\ 

    :param struct rpc_clnt \*rpc_client:
        rpc_client for the pipe

.. _`rpc_gssd_dummy_populate`:

rpc_gssd_dummy_populate
=======================

.. c:function:: struct dentry *rpc_gssd_dummy_populate(struct dentry *root, struct rpc_pipe *pipe_data)

    create a dummy gssd pipe

    :param struct dentry \*root:
        root of the rpc_pipefs filesystem

    :param struct rpc_pipe \*pipe_data:
        pipe data created when netns is initialized

.. _`rpc_gssd_dummy_populate.description`:

Description
-----------

Create a dummy set of directories and a pipe that gssd can hold open to
indicate that it is up and running.

.. This file was automatic generated / don't edit.

