.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-free-when-closed:

=========================
snd_card_free_when_closed
=========================

*man snd_card_free_when_closed(9)*

*4.6.0-rc5*

Disconnect the card, free it later eventually


Synopsis
========

.. c:function:: int snd_card_free_when_closed( struct snd_card * card )

Arguments
=========

``card``
    soundcard structure


Description
===========

Unlike ``snd_card_free``, this function doesn't try to release the card
resource immediately, but tries to disconnect at first. When the card is
still in use, the function returns before freeing the resources. The
card resources will be freed when the refcount gets to zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
