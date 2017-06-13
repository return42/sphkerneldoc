.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/include/asm/io.h

.. _`___ia64_mmiowb`:

___ia64_mmiowb
==============

.. c:function:: void ___ia64_mmiowb( void)

    I/O write barrier

    :param  void:
        no arguments

.. _`___ia64_mmiowb.description`:

Description
-----------

Ensure ordering of I/O space writes.  This will make sure that writes
following the barrier will arrive after all previous writes.  For most
ia64 platforms, this is a simple 'mf.a' instruction.

See Documentation/driver-api/device-io.rst for more information.

.. This file was automatic generated / don't edit.

