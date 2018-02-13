.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/x25/x25_route.c

.. _`__x25_remove_route`:

\__x25_remove_route
===================

.. c:function:: void __x25_remove_route(struct x25_route *rt)

    remove route from x25_route_list

    :param struct x25_route \*rt:
        route to remove

.. _`__x25_remove_route.description`:

Description
-----------

Remove route from x25_route_list. If it was there.
Caller must hold x25_route_list_lock.

.. _`x25_get_route`:

x25_get_route
=============

.. c:function:: struct x25_route *x25_get_route(struct x25_address *addr)

    Find a route given an X.25 address. \ ``addr``\  - address to find a route for

    :param struct x25_address \*addr:
        *undescribed*

.. _`x25_get_route.description`:

Description
-----------

Find a route given an X.25 address.

.. This file was automatic generated / don't edit.

