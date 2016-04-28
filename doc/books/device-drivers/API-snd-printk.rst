.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-printk:

==========
snd_printk
==========

*man snd_printk(9)*

*4.6.0-rc5*

printk wrapper


Synopsis
========

.. c:function:: snd_printk( fmt, args... )

Arguments
=========

``fmt``
    format string

``args...``
    variable arguments


Description
===========

Works like ``printk`` but prints the file and the line of the caller
when configured with CONFIG_SND_VERBOSE_PRINTK.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
