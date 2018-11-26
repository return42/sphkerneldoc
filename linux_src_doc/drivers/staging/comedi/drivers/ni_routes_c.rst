.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/ni_routes.c

.. _`ni_assign_device_routes`:

ni_assign_device_routes
=======================

.. c:function:: int ni_assign_device_routes(const char *device_family, const char *board_name, struct ni_route_tables *tables)

    Assign the proper lookup table for NI signal routing to the specified NI device.

    :param device_family:
        *undescribed*
    :type device_family: const char \*

    :param board_name:
        *undescribed*
    :type board_name: const char \*

    :param tables:
        *undescribed*
    :type tables: struct ni_route_tables \*

.. _`ni_assign_device_routes.return`:

Return
------

-ENODATA if assignment was not successful; 0 if successful.

.. _`ni_count_valid_routes`:

ni_count_valid_routes
=====================

.. c:function:: unsigned int ni_count_valid_routes(const struct ni_route_tables *tables)

    Count the number of valid routes.

    :param tables:
        Routing tables for which to count all valid routes.
    :type tables: const struct ni_route_tables \*

.. _`ni_get_valid_routes`:

ni_get_valid_routes
===================

.. c:function:: unsigned int ni_get_valid_routes(const struct ni_route_tables *tables, unsigned int n_pairs, unsigned int *pair_data)

    Implements INSN_DEVICE_CONFIG_GET_ROUTES.

    :param tables:
        pointer to relevant set of routing tables.
    :type tables: const struct ni_route_tables \*

    :param n_pairs:
        Number of pairs for which memory is allocated by the user.  If
        the user specifies '0', only the number of available pairs is
        returned.
    :type n_pairs: unsigned int

    :param pair_data:
        Pointer to memory allocated to return pairs back to user.  Each
        even, odd indexed member of this array will hold source,
        destination of a route pair respectively.
    :type pair_data: unsigned int \*

.. _`ni_get_valid_routes.return`:

Return
------

the number of valid routes if n_pairs == 0; otherwise, the number of
valid routes copied.

.. _`ni_is_cmd_dest`:

ni_is_cmd_dest
==============

.. c:function:: bool ni_is_cmd_dest(int dest)

    Determine whether the given destination is only configurable via a comedi_cmd struct.

    :param dest:
        Destination to test.
    :type dest: int

.. _`ni_sort_device_routes`:

ni_sort_device_routes
=====================

.. c:function:: void ni_sort_device_routes(struct ni_device_routes *valid_routes)

    Sort the list of valid device signal routes in preparation for use.

    :param valid_routes:
        pointer to ni_device_routes struct to sort.
    :type valid_routes: struct ni_device_routes \*

.. _`ni_find_route_set`:

ni_find_route_set
=================

.. c:function:: const struct ni_route_set *ni_find_route_set(const int destination, const struct ni_device_routes *valid_routes)

    Finds the proper route set with the specified destination.

    :param destination:
        Destination of which to search for the route set.
    :type destination: const int

    :param valid_routes:
        Pointer to device routes within which to search.
    :type valid_routes: const struct ni_device_routes \*

.. _`ni_find_route_set.return`:

Return
------

NULL if no route_set is found with the specified \ ``destination``\ ;
otherwise, a pointer to the route_set if found.

.. _`ni_route_set_has_source`:

ni_route_set_has_source
=======================

.. c:function:: bool ni_route_set_has_source(const struct ni_route_set *routes, const int source)

    Determines whether the given source is in included given route_set.

    :param routes:
        *undescribed*
    :type routes: const struct ni_route_set \*

    :param source:
        *undescribed*
    :type source: const int

.. _`ni_route_set_has_source.return`:

Return
------

true if found; false otherwise.

.. _`ni_lookup_route_register`:

ni_lookup_route_register
========================

.. c:function:: s8 ni_lookup_route_register(int src, int dest, const struct ni_route_tables *tables)

    Look up a register value for a particular route without checking whether the route is valid for the particular device.

    :param src:
        global-identifier for route source
    :type src: int

    :param dest:
        global-identifier for route destination
    :type dest: int

    :param tables:
        pointer to relevant set of routing tables.
    :type tables: const struct ni_route_tables \*

.. _`ni_lookup_route_register.return`:

Return
------

-EINVAL if the specified route is not valid for this device family.

.. _`ni_route_to_register`:

ni_route_to_register
====================

.. c:function:: s8 ni_route_to_register(const int src, const int dest, const struct ni_route_tables *tables)

    Validates and converts the specified signal route (src-->dest) to the value used at the appropriate register.

    :param src:
        global-identifier for route source
    :type src: const int

    :param dest:
        global-identifier for route destination
    :type dest: const int

    :param tables:
        pointer to relevant set of routing tables.
    :type tables: const struct ni_route_tables \*

.. _`ni_route_to_register.description`:

Description
-----------

Generally speaking, most routes require the first six bits and a few require
7 bits.  Special handling is given for the return value when the route is to
be handled by the RTSI sub-device.  In this case, the returned register may
not be sufficient to define the entire route path, but rather may only
indicate the intermediate route.  For example, if the route must go through
the RGOUT0 pin, the (src->RGOUT0) register value will be returned.
Similarly, if the route must go through the NI_RTSI_BRD lines, the BIT(6)

.. _`ni_route_to_register.if-route-does-not-need-rtsi_brd-lines`:

if route does not need RTSI_BRD lines
-------------------------------------


bits 0:7 : register value
for a route that must go through RGOUT0 pin, this will be equal
to the (src->RGOUT0) register value.

.. _`ni_route_to_register.else`:

else
----

\* route is (src->RTSI_BRD(x), RTSI_BRD(x)->TRIGGER_LINE(i)) \*
bits 0:5 : zero
bits 6   : set to 1
bits 7:7 : zero

.. _`ni_route_to_register.return`:

Return
------

register value to be used for source at destination with special
cases given above; Otherwise, -1 if the specified route is not valid for
this particular device.

.. _`ni_find_route_source`:

ni_find_route_source
====================

.. c:function:: int ni_find_route_source(const u8 src_sel_reg_value, int dest, const struct ni_route_tables *tables)

    Finds the signal source corresponding to a signal route (src-->dest) of the specified routing register value and the specified route destination on the specified device.

    :param src_sel_reg_value:
        *undescribed*
    :type src_sel_reg_value: const u8

    :param dest:
        *undescribed*
    :type dest: int

    :param tables:
        *undescribed*
    :type tables: const struct ni_route_tables \*

.. _`ni_find_route_source.description`:

Description
-----------

Note that this function does \_not\_ validate the source based on device
routes.

.. _`ni_find_route_source.return`:

Return
------

The NI signal value (e.g. NI_PFI(0) or PXI_Clk10) if found.
If the source was not found (i.e. the register value is not
valid for any routes to the destination), -EINVAL is returned.

.. This file was automatic generated / don't edit.

