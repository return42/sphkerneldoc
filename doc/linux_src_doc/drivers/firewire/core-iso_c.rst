.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firewire/core-iso.c

.. _`fw_iso_resource_manage`:

fw_iso_resource_manage
======================

.. c:function:: void fw_iso_resource_manage(struct fw_card *card, int generation, u64 channels_mask, int *channel, int *bandwidth, bool allocate)

    Allocate or deallocate a channel and/or bandwidth

    :param struct fw_card \*card:
        *undescribed*

    :param int generation:
        *undescribed*

    :param u64 channels_mask:
        *undescribed*

    :param int \*channel:
        *undescribed*

    :param int \*bandwidth:
        *undescribed*

    :param bool allocate:
        *undescribed*

.. _`fw_iso_resource_manage.in-parameters`:

In parameters
-------------

card, generation, channels_mask, bandwidth, allocate

.. _`fw_iso_resource_manage.out-parameters`:

Out parameters
--------------

channel, bandwidth
This function blocks (sleeps) during communication with the IRM.

Allocates or deallocates at most one channel out of channels_mask.
channels_mask is a bitfield with MSB for channel 63 and LSB for channel 0.
(Note, the IRM's CHANNELS_AVAILABLE is a big-endian bitfield with MSB for
channel 0 and LSB for channel 63.)
Allocates or deallocates as many bandwidth allocation units as specified.

Returns channel < 0 if no channel was allocated or deallocated.
Returns bandwidth = 0 if no bandwidth was allocated or deallocated.

If generation is stale, deallocations succeed but allocations fail with
channel = -EAGAIN.

If channel allocation fails, no bandwidth will be allocated either.
If bandwidth allocation fails, no channel will be allocated either.
But deallocations of channel and bandwidth are tried independently
of each other's success.

.. This file was automatic generated / don't edit.

