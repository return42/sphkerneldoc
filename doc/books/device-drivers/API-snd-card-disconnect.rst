
.. _API-snd-card-disconnect:

===================
snd_card_disconnect
===================

*man snd_card_disconnect(9)*

*4.6.0-rc1*

disconnect all APIs from the file-operations (user space)


Synopsis
========

.. c:function:: int snd_card_disconnect( struct snd_card * card )

Arguments
=========

``card``
    soundcard structure


Description
===========

Disconnects all APIs from the file-operations (user space).


Return
======

Zero, otherwise a negative error code.


Note
====

The current implementation replaces all active file->f_op with special dummy file operations (they do nothing except release).
