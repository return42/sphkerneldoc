.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-printdd:

===========
snd_printdd
===========

*man snd_printdd(9)*

*4.6.0-rc5*

debug printk


Synopsis
========

.. c:function:: snd_printdd( format, args... )

Arguments
=========

``format``
    format string

``args...``
    variable arguments


Description
===========

Works like ``snd_printk`` for debugging purposes. Ignored when
CONFIG_SND_DEBUG_VERBOSE is not set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
