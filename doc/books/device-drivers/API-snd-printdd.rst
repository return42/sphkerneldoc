
.. _API-snd-printdd:

===========
snd_printdd
===========

*man snd_printdd(9)*

*4.6.0-rc1*

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

Works like ``snd_printk`` for debugging purposes. Ignored when CONFIG_SND_DEBUG_VERBOSE is not set.
