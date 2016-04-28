.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-file-remove:

====================
snd_card_file_remove
====================

*man snd_card_file_remove(9)*

*4.6.0-rc5*

remove the file from the file list


Synopsis
========

.. c:function:: int snd_card_file_remove( struct snd_card * card, struct file * file )

Arguments
=========

``card``
    soundcard structure

``file``
    file pointer


Description
===========

This function removes the file formerly added to the card via
``snd_card_file_add`` function. If all files are removed and
``snd_card_free_when_closed`` was called beforehand, it processes the
pending release of resources.


Return
======

Zero or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
