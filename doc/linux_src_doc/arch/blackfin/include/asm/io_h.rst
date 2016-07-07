.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/blackfin/include/asm/io.h

.. _`mmiowb`:

mmiowb
======

.. c:function::  mmiowb( void)

    :param  void:
        no arguments

.. _`mmiowb.description`:

Description
-----------

Ensure ordering of I/O space writes. This will make sure that writes
following the barrier will arrive after all previous writes.

.. This file was automatic generated / don't edit.

