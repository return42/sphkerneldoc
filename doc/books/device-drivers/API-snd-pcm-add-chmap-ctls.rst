.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-add-chmap-ctls:

======================
snd_pcm_add_chmap_ctls
======================

*man snd_pcm_add_chmap_ctls(9)*

*4.6.0-rc5*

create channel-mapping control elements


Synopsis
========

.. c:function:: int snd_pcm_add_chmap_ctls( struct snd_pcm * pcm, int stream, const struct snd_pcm_chmap_elem * chmap, int max_channels, unsigned long private_value, struct snd_pcm_chmap ** info_ret )

Arguments
=========

``pcm``
    the assigned PCM instance

``stream``
    stream direction

``chmap``
    channel map elements (for query)

``max_channels``
    the max number of channels for the stream

``private_value``
    the value passed to each kcontrol's private_value field

``info_ret``
    store struct snd_pcm_chmap instance if non-NULL


Description
===========

Create channel-mapping control elements assigned to the given PCM
stream(s).


Return
======

Zero if successful, or a negative error value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
