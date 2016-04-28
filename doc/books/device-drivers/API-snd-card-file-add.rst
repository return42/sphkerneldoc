.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-file-add:

=================
snd_card_file_add
=================

*man snd_card_file_add(9)*

*4.6.0-rc5*

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

This function adds the file to the file linked-list of the card. This
linked-list is used to keep tracking the connection state, and to avoid
the release of busy resources by hotplug.


Return
======

zero or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
