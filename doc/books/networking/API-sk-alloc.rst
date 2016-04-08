
.. _API-sk-alloc:

========
sk_alloc
========

*man sk_alloc(9)*

*4.6.0-rc1*

All socket objects are allocated here


Synopsis
========

.. c:function:: struct sock ⋆ sk_alloc( struct net * net, int family, gfp_t priority, struct proto * prot, int kern )

Arguments
=========

``net``
    the applicable net namespace

``family``
    protocol family

``priority``
    for allocation (``GFP_KERNEL``, ``GFP_ATOMIC``, etc)

``prot``
    struct proto associated with this new sock instance

``kern``
    is this to be a kernel socket?
