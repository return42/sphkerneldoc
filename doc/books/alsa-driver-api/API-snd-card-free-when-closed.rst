
.. _API-snd-card-free-when-closed:

=========================
snd_card_free_when_closed
=========================

*man snd_card_free_when_closed(9)*

*4.6.0-rc1*

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

Unlike ``snd_card_free``, this function doesn't try to release the card resource immediately, but tries to disconnect at first. When the card is still in use, the function returns
before freeing the resources. The card resources will be freed when the refcount gets to zero.
