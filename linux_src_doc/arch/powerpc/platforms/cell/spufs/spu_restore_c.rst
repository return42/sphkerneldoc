.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/spu_restore.c

.. _`main`:

main
====

.. c:function:: int main( void)

    entry point for SPU-side context restore.

    :param  void:
        no arguments

.. _`main.description`:

Description
-----------

This code deviates from the documented sequence in the

.. _`main.following-aspects`:

following aspects
-----------------


1. The EA for LSCSA is passed from PPE in the
signal notification channels.
2. The register spill area is pulled by SPU
into LS, rather than pushed by PPE.
3. All 128 registers are restored by \ :c:func:`exit`\ .
4. The \ :c:func:`exit`\  function is modified at run
time in order to properly restore the
SPU_Status register.

.. This file was automatic generated / don't edit.

