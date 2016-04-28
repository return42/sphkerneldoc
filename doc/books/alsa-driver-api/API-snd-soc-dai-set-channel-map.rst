.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-set-channel-map:

===========================
snd_soc_dai_set_channel_map
===========================

*man snd_soc_dai_set_channel_map(9)*

*4.6.0-rc5*

configure DAI audio channel map


Synopsis
========

.. c:function:: int snd_soc_dai_set_channel_map( struct snd_soc_dai * dai, unsigned int tx_num, unsigned int * tx_slot, unsigned int rx_num, unsigned int * rx_slot )

Arguments
=========

``dai``
    DAI

``tx_num``
    how many TX channels

``tx_slot``
    pointer to an array which imply the TX slot number channel 0~num-1
    uses

``rx_num``
    how many RX channels

``rx_slot``
    pointer to an array which imply the RX slot number channel 0~num-1
    uses


Description
===========

configure the relationship between channel number and TDM slot number.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
