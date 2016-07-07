.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtmultipath.c

.. _`rpc_xprt_switch_add_xprt`:

rpc_xprt_switch_add_xprt
========================

.. c:function:: void rpc_xprt_switch_add_xprt(struct rpc_xprt_switch *xps, struct rpc_xprt *xprt)

    Add a new rpc_xprt to an rpc_xprt_switch

    :param struct rpc_xprt_switch \*xps:
        pointer to struct rpc_xprt_switch

    :param struct rpc_xprt \*xprt:
        pointer to struct rpc_xprt

.. _`rpc_xprt_switch_add_xprt.description`:

Description
-----------

Adds xprt to the end of the list of struct rpc_xprt in xps.

.. _`rpc_xprt_switch_remove_xprt`:

rpc_xprt_switch_remove_xprt
===========================

.. c:function:: void rpc_xprt_switch_remove_xprt(struct rpc_xprt_switch *xps, struct rpc_xprt *xprt)

    Removes an rpc_xprt from a rpc_xprt_switch

    :param struct rpc_xprt_switch \*xps:
        pointer to struct rpc_xprt_switch

    :param struct rpc_xprt \*xprt:
        pointer to struct rpc_xprt

.. _`rpc_xprt_switch_remove_xprt.description`:

Description
-----------

Removes xprt from the list of struct rpc_xprt in xps.

.. _`xprt_switch_alloc`:

xprt_switch_alloc
=================

.. c:function:: struct rpc_xprt_switch *xprt_switch_alloc(struct rpc_xprt *xprt, gfp_t gfp_flags)

    Allocate a new struct rpc_xprt_switch

    :param struct rpc_xprt \*xprt:
        pointer to struct rpc_xprt

    :param gfp_t gfp_flags:
        allocation flags

.. _`xprt_switch_alloc.description`:

Description
-----------

On success, returns an initialised struct rpc_xprt_switch, containing
the entry xprt. Returns NULL on failure.

.. _`xprt_switch_get`:

xprt_switch_get
===============

.. c:function:: struct rpc_xprt_switch *xprt_switch_get(struct rpc_xprt_switch *xps)

    Return a reference to a rpc_xprt_switch

    :param struct rpc_xprt_switch \*xps:
        pointer to struct rpc_xprt_switch

.. _`xprt_switch_get.description`:

Description
-----------

Returns a reference to xps unless the refcount is already zero.

.. _`xprt_switch_put`:

xprt_switch_put
===============

.. c:function:: void xprt_switch_put(struct rpc_xprt_switch *xps)

    Release a reference to a rpc_xprt_switch

    :param struct rpc_xprt_switch \*xps:
        pointer to struct rpc_xprt_switch

.. _`xprt_switch_put.description`:

Description
-----------

Release the reference to xps, and free it once the refcount is zero.

.. _`rpc_xprt_switch_set_roundrobin`:

rpc_xprt_switch_set_roundrobin
==============================

.. c:function:: void rpc_xprt_switch_set_roundrobin(struct rpc_xprt_switch *xps)

    Set a round-robin policy on rpc_xprt_switch

    :param struct rpc_xprt_switch \*xps:
        pointer to struct rpc_xprt_switch

.. _`rpc_xprt_switch_set_roundrobin.description`:

Description
-----------

Sets a round-robin default policy for iterators acting on xps.

.. _`xprt_iter_init`:

xprt_iter_init
==============

.. c:function:: void xprt_iter_init(struct rpc_xprt_iter *xpi, struct rpc_xprt_switch *xps)

    Initialise an xprt iterator

    :param struct rpc_xprt_iter \*xpi:
        pointer to rpc_xprt_iter

    :param struct rpc_xprt_switch \*xps:
        pointer to rpc_xprt_switch

.. _`xprt_iter_init.description`:

Description
-----------

Initialises the iterator to use the default iterator ops
as set in xps. This function is mainly intended for internal
use in the rpc_client.

.. _`xprt_iter_init_listall`:

xprt_iter_init_listall
======================

.. c:function:: void xprt_iter_init_listall(struct rpc_xprt_iter *xpi, struct rpc_xprt_switch *xps)

    Initialise an xprt iterator

    :param struct rpc_xprt_iter \*xpi:
        pointer to rpc_xprt_iter

    :param struct rpc_xprt_switch \*xps:
        pointer to rpc_xprt_switch

.. _`xprt_iter_init_listall.description`:

Description
-----------

Initialises the iterator to iterate once through the entire list
of entries in xps.

.. _`xprt_iter_xchg_switch`:

xprt_iter_xchg_switch
=====================

.. c:function:: struct rpc_xprt_switch *xprt_iter_xchg_switch(struct rpc_xprt_iter *xpi, struct rpc_xprt_switch *newswitch)

    Atomically swap out the rpc_xprt_switch

    :param struct rpc_xprt_iter \*xpi:
        pointer to rpc_xprt_iter

    :param struct rpc_xprt_switch \*newswitch:
        *undescribed*

.. _`xprt_iter_xchg_switch.description`:

Description
-----------

Swaps out the existing xpi->xpi_xpswitch with a new value.

.. _`xprt_iter_destroy`:

xprt_iter_destroy
=================

.. c:function:: void xprt_iter_destroy(struct rpc_xprt_iter *xpi)

    Destroys the xprt iterator \ ``xpi``\  pointer to rpc_xprt_iter

    :param struct rpc_xprt_iter \*xpi:
        *undescribed*

.. _`xprt_iter_xprt`:

xprt_iter_xprt
==============

.. c:function:: struct rpc_xprt *xprt_iter_xprt(struct rpc_xprt_iter *xpi)

    Returns the rpc_xprt pointed to by the cursor

    :param struct rpc_xprt_iter \*xpi:
        pointer to rpc_xprt_iter

.. _`xprt_iter_xprt.description`:

Description
-----------

Returns a pointer to the struct rpc_xprt that is currently
pointed to by the cursor.
Caller must be holding \ :c:func:`rcu_read_lock`\ .

.. _`xprt_iter_get_xprt`:

xprt_iter_get_xprt
==================

.. c:function:: struct rpc_xprt *xprt_iter_get_xprt(struct rpc_xprt_iter *xpi)

    Returns the rpc_xprt pointed to by the cursor

    :param struct rpc_xprt_iter \*xpi:
        pointer to rpc_xprt_iter

.. _`xprt_iter_get_xprt.description`:

Description
-----------

Returns a reference to the struct rpc_xprt that is currently
pointed to by the cursor.

.. _`xprt_iter_get_next`:

xprt_iter_get_next
==================

.. c:function:: struct rpc_xprt *xprt_iter_get_next(struct rpc_xprt_iter *xpi)

    Returns the next rpc_xprt following the cursor

    :param struct rpc_xprt_iter \*xpi:
        pointer to rpc_xprt_iter

.. _`xprt_iter_get_next.description`:

Description
-----------

Returns a reference to the struct rpc_xprt that immediately follows the
entry pointed to by the cursor.

.. This file was automatic generated / don't edit.

