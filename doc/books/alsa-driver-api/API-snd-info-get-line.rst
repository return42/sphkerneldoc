.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-info-get-line:

=================
snd_info_get_line
=================

*man snd_info_get_line(9)*

*4.6.0-rc5*

read one line from the procfs buffer


Synopsis
========

.. c:function:: int snd_info_get_line( struct snd_info_buffer * buffer, char * line, int len )

Arguments
=========

``buffer``
    the procfs buffer

``line``
    the buffer to store

``len``
    the max. buffer size


Description
===========

Reads one line from the buffer and stores the string.


Return
======

Zero if successful, or 1 if error or EOF.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
