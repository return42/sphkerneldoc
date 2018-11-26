.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firewire/core-iso.c

.. _`fw_iso_resource_manage`:

fw_iso_resource_manage
======================

.. c:function:: void fw_iso_resource_manage(struct fw_card *card, int generation, u64 channels_mask, int *channel, int *bandwidth, bool allocate)

    Allocate or deallocate a channel and/or bandwidth

    :param card:
        card interface for this action
    :type card: struct fw_card \*

    :param generation:
        bus generation
    :type generation: int

    :param channels_mask:
        bitmask for channel allocation
    :type channels_mask: u64

    :param channel:
        pointer for returning channel allocation result
    :type channel: int \*

    :param bandwidth:
        pointer for returning bandwidth allocation result
    :type bandwidth: int \*

    :param allocate:
        whether to allocate (true) or deallocate (false)
    :type allocate: bool

.. _`fw_iso_resource_manage.description`:

Description
-----------

In parameters: card, generation, channels_mask, bandwidth, allocate
Out parameters: channel, bandwidth

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

