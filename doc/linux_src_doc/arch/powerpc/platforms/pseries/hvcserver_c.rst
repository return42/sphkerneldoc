.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/hvcserver.c

.. _`hvcs_free_partner_info`:

hvcs_free_partner_info
======================

.. c:function:: int hvcs_free_partner_info(struct list_head *head)

    free pi allocated by hvcs_get_partner_info

    :param struct list_head \*head:
        list_head pointer for an allocated list of partner info structs to
        free.

.. _`hvcs_free_partner_info.description`:

Description
-----------

This function is used to free the partner info list that was returned by
calling \ :c:func:`hvcs_get_partner_info`\ .

.. _`hvcs_get_partner_info`:

hvcs_get_partner_info
=====================

.. c:function:: int hvcs_get_partner_info(uint32_t unit_address, struct list_head *head, unsigned long *pi_buff)

    Get all of the partner info for a vty-server adapter

    :param uint32_t unit_address:
        The unit_address of the vty-server adapter for which this
        function is fetching partner info.

    :param struct list_head \*head:
        An initialized list_head pointer to an empty list to use to return the
        list of partner info fetched from the hypervisor to the caller.

    :param unsigned long \*pi_buff:
        A page sized buffer pre-allocated prior to calling this function
        that is to be used to be used by firmware as an iterator to keep track
        of the partner info retrieval.

.. _`hvcs_get_partner_info.description`:

Description
-----------

This function returns non-zero on success, or if there is no partner info.

The pi_buff is pre-allocated prior to calling this function because this
function may be called with a spin_lock held and kmalloc of a page is not
recommended as GFP_ATOMIC.

The first long of this buffer is used to store a partner unit address.  The
second long is used to store a partner partition ID and starting at
pi_buff[2] is the 79 character Converged Location Code (diff size than the
unsigned longs, hence the casting mumbo jumbo you see later).

Invocation of this function should always be followed by an invocation of
\ :c:func:`hvcs_free_partner_info`\  using a pointer to the SAME list head instance
that was passed as a parameter to this function.

.. _`hvcs_register_connection`:

hvcs_register_connection
========================

.. c:function:: int hvcs_register_connection(uint32_t unit_address, uint32_t p_partition_ID, uint32_t p_unit_address)

    establish a connection between this vty-server and a vty.

    :param uint32_t unit_address:
        The unit address of the vty-server adapter that is to be
        establish a connection.

    :param uint32_t p_partition_ID:
        The partition ID of the vty adapter that is to be connected.

    :param uint32_t p_unit_address:
        The unit address of the vty adapter to which the vty-server
        is to be connected.

.. _`hvcs_register_connection.description`:

Description
-----------

If this function is called once and -EINVAL is returned it may
indicate that the partner info needs to be refreshed for the
target unit address at which point the caller must invoke
\ :c:func:`hvcs_get_partner_info`\  and then call this function again.  If,
for a second time, -EINVAL is returned then it indicates that
there is probably already a partner connection registered to a
different vty-server adapter.  It is also possible that a second
-EINVAL may indicate that one of the parms is not valid, for
instance if the link was removed between the vty-server adapter
and the vty adapter that you are trying to open.  Don't shoot the
messenger.  Firmware implemented it this way.

.. _`hvcs_free_connection`:

hvcs_free_connection
====================

.. c:function:: int hvcs_free_connection(uint32_t unit_address)

    free the connection between a vty-server and vty

    :param uint32_t unit_address:
        The unit address of the vty-server that is to have its
        connection severed.

.. _`hvcs_free_connection.description`:

Description
-----------

This function is used to free the partner connection between a vty-server
adapter and a vty adapter.

If -EBUSY is returned continue to call this function until 0 is returned.

.. This file was automatic generated / don't edit.

