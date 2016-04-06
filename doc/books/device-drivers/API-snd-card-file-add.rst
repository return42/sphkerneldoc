
.. _API-snd-card-file-add:

=================
snd_card_file_add
=================

*man snd_card_file_add(9)*

*4.6.0-rc1*

add the file to the file list of the card


Synopsis
========

.. c:function:: int snd_card_file_add( struct snd_card * card, struct file * file )

Arguments
=========

``card``
    soundcard structure

``file``
    file pointer


Description
===========

This function adds the file to the file linked-list of the card. This linked-list is used to keep tracking the connection state, and to avoid the release of busy resources by
hotplug.


Return
======

zero or a negative error code.
