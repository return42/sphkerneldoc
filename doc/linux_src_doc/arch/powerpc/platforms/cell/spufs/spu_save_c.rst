.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/spu_save.c

.. _`main`:

main
====

.. c:function:: int main( void)

    entry point for SPU-side context save.

    :param  void:
        no arguments

.. _`main.this-code-deviates-from-the-documented-sequence-as-follows`:

This code deviates from the documented sequence as follows
----------------------------------------------------------


1. The EA for LSCSA is passed from PPE in the
signal notification channels.
2. All 128 registers are saved by crt0.o.

.. This file was automatic generated / don't edit.

