.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-disconnect:

===================
snd_card_disconnect
===================

*man snd_card_disconnect(9)*

*4.6.0-rc5*

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

The current implementation replaces all active file->f_op with special
dummy file operations (they do nothing except release).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
