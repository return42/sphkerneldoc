.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/asihpi/asihpi.c

.. _`snd_printddd`:

snd_printddd
============

.. c:function::  snd_printddd( format,  args...)

    very verbose debug printk

    :param  format:
        format string

    :param  args...:
        variable arguments

.. _`snd_printddd.description`:

Description
-----------

Works like \ :c:func:`snd_printk`\  for debugging purposes.
Ignored when CONFIG_SND_DEBUG_VERBOSE is not set.
Must set snd module debug parameter to 3 to enable at runtime.

.. This file was automatic generated / don't edit.

