
.. _API-snd-rawmidi-set-ops:

===================
snd_rawmidi_set_ops
===================

*man snd_rawmidi_set_ops(9)*

*4.6.0-rc1*

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
