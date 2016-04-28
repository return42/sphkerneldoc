.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-info-register:

=================
snd_info_register
=================

*man snd_info_register(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
