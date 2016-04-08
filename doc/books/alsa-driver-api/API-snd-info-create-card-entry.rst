
.. _API-snd-info-create-card-entry:

==========================
snd_info_create_card_entry
==========================

*man snd_info_create_card_entry(9)*

*4.6.0-rc1*

create an info entry for the given card


Synopsis
========

.. c:function:: struct snd_info_entry ⋆ snd_info_create_card_entry( struct snd_card * card, const char * name, struct snd_info_entry * parent )

Arguments
=========

``card``
    the card instance

``name``
    the file name

``parent``
    the parent directory


Description
===========

Creates a new info entry and assigns it to the given card.


Return
======

The pointer of the new instance, or ``NULL`` on failure.
