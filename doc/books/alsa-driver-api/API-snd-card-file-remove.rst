
.. _API-snd-card-file-remove:

====================
snd_card_file_remove
====================

*man snd_card_file_remove(9)*

*4.6.0-rc1*

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

This function removes the file formerly added to the card via ``snd_card_file_add`` function. If all files are removed and ``snd_card_free_when_closed`` was called beforehand, it
processes the pending release of resources.


Return
======

Zero or a negative error code.
