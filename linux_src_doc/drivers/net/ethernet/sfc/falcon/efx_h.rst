.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/efx.h

.. _`ef4_filter_insert_filter`:

ef4_filter_insert_filter
========================

.. c:function:: s32 ef4_filter_insert_filter(struct ef4_nic *efx, struct ef4_filter_spec *spec, bool replace_equal)

    add or replace a filter

    :param struct ef4_nic \*efx:
        NIC in which to insert the filter

    :param struct ef4_filter_spec \*spec:
        Specification for the filter

    :param bool replace_equal:
        Flag for whether the specified filter may replace an
        existing filter with equal priority

.. _`ef4_filter_insert_filter.description`:

Description
-----------

On success, return the filter ID.
On failure, return a negative error code.

If existing filters have equal match values to the new filter spec,
then the new filter might replace them or the function might fail,
as follows.

1. If the existing filters have lower priority, or \ ``replace_equal``\ 
is set and they have equal priority, replace them.

2. If the existing filters have higher priority, return -%EPERM.

3. If !ef4_filter_is_mc_recipient(@spec), or the NIC does not
support delivery to multiple recipients, return -%EEXIST.

This implies that filters for multiple multicast recipients must
all be inserted with the same priority and \ ``replace_equal``\  = \ ``false``\ .

.. _`ef4_filter_remove_id_safe`:

ef4_filter_remove_id_safe
=========================

.. c:function:: int ef4_filter_remove_id_safe(struct ef4_nic *efx, enum ef4_filter_priority priority, u32 filter_id)

    remove a filter by ID, carefully

    :param struct ef4_nic \*efx:
        NIC from which to remove the filter

    :param enum ef4_filter_priority priority:
        Priority of filter, as passed to \ ``ef4_filter_insert_filter``\ 

    :param u32 filter_id:
        ID of filter, as returned by \ ``ef4_filter_insert_filter``\ 

.. _`ef4_filter_remove_id_safe.description`:

Description
-----------

This function will range-check \ ``filter_id``\ , so it is safe to call
with a value passed from userland.

.. _`ef4_filter_get_filter_safe`:

ef4_filter_get_filter_safe
==========================

.. c:function:: int ef4_filter_get_filter_safe(struct ef4_nic *efx, enum ef4_filter_priority priority, u32 filter_id, struct ef4_filter_spec *spec)

    retrieve a filter by ID, carefully

    :param struct ef4_nic \*efx:
        NIC from which to remove the filter

    :param enum ef4_filter_priority priority:
        Priority of filter, as passed to \ ``ef4_filter_insert_filter``\ 

    :param u32 filter_id:
        ID of filter, as returned by \ ``ef4_filter_insert_filter``\ 

    :param struct ef4_filter_spec \*spec:
        Buffer in which to store filter specification

.. _`ef4_filter_get_filter_safe.description`:

Description
-----------

This function will range-check \ ``filter_id``\ , so it is safe to call
with a value passed from userland.

.. This file was automatic generated / don't edit.

