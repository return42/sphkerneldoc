
.. _API-snd-ctl-notify:

==============
snd_ctl_notify
==============

*man snd_ctl_notify(9)*

*4.6.0-rc1*

Send notification to user-space for a control change


Synopsis
========

.. c:function:: void snd_ctl_notify( struct snd_card * card, unsigned int mask, struct snd_ctl_elem_id * id )

Arguments
=========

``card``
    the card to send notification

``mask``
    the event mask, SNDRV_CTL_EVENT_⋆

``id``
    the ctl element id to send notification


Description
===========

This function adds an event record with the given id and mask, appends to the list and wakes up the user-space for notification. This can be called in the atomic context.
