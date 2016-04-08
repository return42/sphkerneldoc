
.. _API-snd-printd:

==========
snd_printd
==========

*man snd_printd(9)*

*4.6.0-rc1*

debug printk


Synopsis
========

.. c:function:: snd_printd( fmt, args... )

Arguments
=========

``fmt``
    format string

``args...``
    variable arguments


Description
===========

Works like ``snd_printk`` for debugging purposes. Ignored when CONFIG_SND_DEBUG is not set.
