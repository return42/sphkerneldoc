.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-rawmidi-set-ops:

===================
snd_rawmidi_set_ops
===================

*man snd_rawmidi_set_ops(9)*

*4.6.0-rc5*

set the rawmidi operators


Synopsis
========

.. c:function:: void snd_rawmidi_set_ops( struct snd_rawmidi * rmidi, int stream, struct snd_rawmidi_ops * ops )

Arguments
=========

``rmidi``
    the rawmidi instance

``stream``
    the stream direction, SNDRV_RAWMIDI_STREAM_XXX

``ops``
    the operator table


Description
===========

Sets the rawmidi operators for the given stream direction.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
