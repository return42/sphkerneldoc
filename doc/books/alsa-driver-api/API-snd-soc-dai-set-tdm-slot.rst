.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-set-tdm-slot:

========================
snd_soc_dai_set_tdm_slot
========================

*man snd_soc_dai_set_tdm_slot(9)*

*4.6.0-rc5*

Configures a DAI for TDM operation


Synopsis
========

.. c:function:: int snd_soc_dai_set_tdm_slot( struct snd_soc_dai * dai, unsigned int tx_mask, unsigned int rx_mask, int slots, int slot_width )

Arguments
=========

``dai``
    The DAI to configure

``tx_mask``
    bitmask representing active TX slots.

``rx_mask``
    bitmask representing active RX slots.

``slots``
    Number of slots in use.

``slot_width``
    Width in bits for each slot.


Description
===========

This function configures the specified DAI for TDM operation. ``slot``
contains the total number of slots of the TDM stream and ``slot_with``
the width of each slot in bit clock cycles. ``tx_mask`` and ``rx_mask``
are bitmasks specifying the active slots of the TDM stream for the
specified DAI, i.e. which slots the DAI should write to or read from. If
a bit is set the corresponding slot is active, if a bit is cleared the
corresponding slot is inactive. Bit 0 maps to the first slot, bit 1 to
the second slot and so on. The first active slot maps to the first
channel of the DAI, the second active slot to the second channel and so
on.

TDM mode can be disabled by passing 0 for ``slots``. In this case
``tx_mask``, ``rx_mask`` and ``slot_width`` will be ignored.

Returns 0 on success, a negative error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
