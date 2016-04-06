
.. _API-snd-info-register:

=================
snd_info_register
=================

*man snd_info_register(9)*

*4.6.0-rc1*

register the info entry


Synopsis
========

.. c:function:: int snd_info_register( struct snd_info_entry * entry )

Arguments
=========

``entry``
    the info entry


Description
===========

Registers the proc info entry.


Return
======

Zero if successful, or a negative error code on failure.
