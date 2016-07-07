.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sunrpc/auth.h

.. _`get_rpccred_rcu`:

get_rpccred_rcu
===============

.. c:function:: struct rpc_cred *get_rpccred_rcu(struct rpc_cred *cred)

    get a reference to a cred using rcu-protected pointer

    :param struct rpc_cred \*cred:
        cred of which to take a reference

.. _`get_rpccred_rcu.description`:

Description
-----------

In some cases, we may have a pointer to a credential to which we
want to take a reference, but don't already have one. Because these
objects are freed using RCU, we can access the cr_count while its
on its way to destruction and only take a reference if it's not already
zero.

.. This file was automatic generated / don't edit.

