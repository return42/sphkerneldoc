
.. _API-snd-printk:

==========
snd_printk
==========

*man snd_printk(9)*

*4.6.0-rc1*

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

Works like ``printk`` but prints the file and the line of the caller when configured with CONFIG_SND_VERBOSE_PRINTK.
