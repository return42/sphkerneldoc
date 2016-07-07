.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-zynq/common.c

.. _`zynq_memory_init`:

zynq_memory_init
================

.. c:function:: void zynq_memory_init( void)

    Initialize special memory

    :param  void:
        no arguments

.. _`zynq_memory_init.description`:

Description
-----------

We need to stop things allocating the low memory as DMA can't work in
the 1st 512K of memory.

.. _`zynq_get_revision`:

zynq_get_revision
=================

.. c:function:: int zynq_get_revision( void)

    Get Zynq silicon revision

    :param  void:
        no arguments

.. _`zynq_get_revision.return`:

Return
------

Silicon version or -1 otherwise

.. _`zynq_init_machine`:

zynq_init_machine
=================

.. c:function:: void zynq_init_machine( void)

    System specific initialization, intended to be called from board specific initialization.

    :param  void:
        no arguments

.. _`zynq_map_io`:

zynq_map_io
===========

.. c:function:: void zynq_map_io( void)

    Create memory mappings needed for early I/O.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

