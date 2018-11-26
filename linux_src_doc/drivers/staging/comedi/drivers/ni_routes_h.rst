.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/ni_routes.h

.. _`ni_route_set`:

struct ni_route_set
===================

.. c:type:: struct ni_route_set

    Set of destinations with a common source.

.. _`ni_route_set.definition`:

Definition
----------

.. code-block:: c

    struct ni_route_set {
        int dest;
        int n_src;
        int *src;
    }

.. _`ni_route_set.members`:

Members
-------

dest
    Destination of all sources in this route set.

n_src
    Number of sources for this route set.

src
    List of sources that all map to the same destination.

.. _`ni_device_routes`:

struct ni_device_routes
=======================

.. c:type:: struct ni_device_routes

    List of all src->dest sets for a particular device.

.. _`ni_device_routes.definition`:

Definition
----------

.. code-block:: c

    struct ni_device_routes {
        const char *device;
        int n_route_sets;
        struct ni_route_set *routes;
    }

.. _`ni_device_routes.members`:

Members
-------

device
    Name of board/device (e.g. pxi-6733).

n_route_sets
    Number of route sets that are valid for this device.

routes
    List of route sets that are valid for this device.

.. _`ni_route_tables`:

struct ni_route_tables
======================

.. c:type:: struct ni_route_tables

    Register values and valid routes for a device.

.. _`ni_route_tables.definition`:

Definition
----------

.. code-block:: c

    struct ni_route_tables {
        const struct ni_device_routes *valid_routes;
        const u8 *route_values;
    }

.. _`ni_route_tables.members`:

Members
-------

valid_routes
    Pointer to a all valid route sets for a single device.

route_values
    Pointer to register values for all routes for the family to
    which the device belongs.

.. _`ni_route_tables.description`:

Description
-----------

Link to the valid src->dest routes and the register values used to assign
such routes for that particular device.

.. _`route_is_valid`:

route_is_valid
==============

.. c:function:: bool route_is_valid(const int src, const int dest, const struct ni_route_tables *tables)

    Determines whether the specified signal route (src-->dest) is valid for the given NI comedi_device.

    :param src:
        global-identifier for route source
    :type src: const int

    :param dest:
        global-identifier for route destination
    :type dest: const int

    :param tables:
        pointer to relevant set of routing tables.
    :type tables: const struct ni_route_tables \*

.. _`route_is_valid.return`:

Return
------

True if the route is valid, otherwise false.

.. _`route_register_is_valid`:

route_register_is_valid
=======================

.. c:function:: bool route_register_is_valid(const u8 src_sel_reg_value, const int dest, const struct ni_route_tables *tables)

    Determines whether the register value for the specified route destination on the specified device is valid.

    :param src_sel_reg_value:
        *undescribed*
    :type src_sel_reg_value: const u8

    :param dest:
        *undescribed*
    :type dest: const int

    :param tables:
        *undescribed*
    :type tables: const struct ni_route_tables \*

.. _`ni_get_reg_value_roffs`:

ni_get_reg_value_roffs
======================

.. c:function:: s8 ni_get_reg_value_roffs(int src, const int dest, const struct ni_route_tables *tables, const int direct_reg_offset)

    Determines the proper register value for a particular valid NI signal/terminal route.

    :param src:
        Either a direct register value or one of NI\_\* signal names.
    :type src: int

    :param dest:
        global-identifier for route destination
    :type dest: const int

    :param tables:
        pointer to relevant set of routing tables.
    :type tables: const struct ni_route_tables \*

    :param direct_reg_offset:
        Compatibility compensation argument.  This argument allows us to
        arbitrarily apply an offset to src if src is a direct register
        value reference.  This is necessary to be compatible with
        definitions of register values as previously exported directly
        to user space.
    :type direct_reg_offset: const int

.. _`ni_get_reg_value_roffs.return`:

Return
------

the register value (>0) to be used at the destination if the src is
valid for the given destination; -1 otherwise.

.. _`ni_check_trigger_arg_roffs`:

ni_check_trigger_arg_roffs
==========================

.. c:function:: int ni_check_trigger_arg_roffs(int src, const int dest, const struct ni_route_tables *tables, const int direct_reg_offset)

    Checks the trigger argument (\*\_arg) of an NI device to ensure that the \*\_arg value corresponds to \_either\_ a valid register value to define a trigger source, \_or\_ a valid NI signal/terminal name that has a valid route to the destination on the particular device.

    :param src:
        Either a direct register value or one of NI\_\* signal names.
    :type src: int

    :param dest:
        global-identifier for route destination
    :type dest: const int

    :param tables:
        pointer to relevant set of routing tables.
    :type tables: const struct ni_route_tables \*

    :param direct_reg_offset:
        Compatibility compensation argument.  This argument allows us to
        arbitrarily apply an offset to src if src is a direct register
        value reference.  This is necessary to be compatible with
        definitions of register values as previously exported directly
        to user space.
    :type direct_reg_offset: const int

.. _`ni_check_trigger_arg_roffs.return`:

Return
------

0 if the src (either register value or NI signal/terminal name) is
valid for the destination; -EINVAL otherwise.

.. This file was automatic generated / don't edit.

