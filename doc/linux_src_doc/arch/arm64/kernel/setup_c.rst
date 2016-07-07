.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kernel/setup.c

.. _`smp_build_mpidr_hash`:

smp_build_mpidr_hash
====================

.. c:function:: void smp_build_mpidr_hash( void)

    Pre-compute shifts required at each affinity level in order to build a linear index from an MPIDR value. Resulting algorithm is a collision free hash carried out through shifting and ORing

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

