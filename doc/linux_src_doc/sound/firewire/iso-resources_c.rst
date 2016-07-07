.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/iso-resources.c

.. _`fw_iso_resources_init`:

fw_iso_resources_init
=====================

.. c:function:: int fw_iso_resources_init(struct fw_iso_resources *r, struct fw_unit *unit)

    initializes a \ :c:type:`struct fw_iso_resources <fw_iso_resources>`\ 

    :param struct fw_iso_resources \*r:
        the resource manager to initialize

    :param struct fw_unit \*unit:
        the device unit for which the resources will be needed

.. _`fw_iso_resources_init.description`:

Description
-----------

If the device does not support all channel numbers, change \ ``r``\ ->channels_mask
after calling this function.

.. _`fw_iso_resources_destroy`:

fw_iso_resources_destroy
========================

.. c:function:: void fw_iso_resources_destroy(struct fw_iso_resources *r)

    destroy a resource manager

    :param struct fw_iso_resources \*r:
        the resource manager that is no longer needed

.. _`fw_iso_resources_allocate`:

fw_iso_resources_allocate
=========================

.. c:function:: int fw_iso_resources_allocate(struct fw_iso_resources *r, unsigned int max_payload_bytes, int speed)

    allocate isochronous channel and bandwidth

    :param struct fw_iso_resources \*r:
        the resource manager

    :param unsigned int max_payload_bytes:
        the amount of data (including CIP headers) per packet

    :param int speed:
        the speed (e.g., SCODE_400) at which the packets will be sent

.. _`fw_iso_resources_allocate.description`:

Description
-----------

This function allocates one isochronous channel and enough bandwidth for the
specified packet size.

Returns the channel number that the caller must use for streaming, or
a negative error code.  Due to potentionally long delays, this function is
interruptible and can return -ERESTARTSYS.  On success, the caller is
responsible for calling \ :c:func:`fw_iso_resources_update`\  on bus resets, and
\ :c:func:`fw_iso_resources_free`\  when the resources are not longer needed.

.. _`fw_iso_resources_update`:

fw_iso_resources_update
=======================

.. c:function:: int fw_iso_resources_update(struct fw_iso_resources *r)

    update resource allocations after a bus reset

    :param struct fw_iso_resources \*r:
        the resource manager

.. _`fw_iso_resources_update.description`:

Description
-----------

This function must be called from the driver's .update handler to reallocate
any resources that were allocated before the bus reset.  It is safe to call
this function if no resources are currently allocated.

Returns a negative error code on failure.  If this happens, the caller must
stop streaming.

.. _`fw_iso_resources_free`:

fw_iso_resources_free
=====================

.. c:function:: void fw_iso_resources_free(struct fw_iso_resources *r)

    frees allocated resources

    :param struct fw_iso_resources \*r:
        the resource manager

.. _`fw_iso_resources_free.description`:

Description
-----------

This function deallocates the channel and bandwidth, if allocated.

.. This file was automatic generated / don't edit.

