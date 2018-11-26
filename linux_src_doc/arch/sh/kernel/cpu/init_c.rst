.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/cpu/init.c

.. _`cpu_init`:

cpu_init
========

.. c:function:: void cpu_init( void)

    :param void:
        no arguments
    :type void: 

.. _`cpu_init.description`:

Description
-----------

This is our initial entry point for each CPU, and is invoked on the
boot CPU prior to calling \ :c:func:`start_kernel`\ . For SMP, a combination of
this and \ :c:func:`start_secondary`\  will bring up each processor to a ready
state prior to hand forking the idle loop.

We do all of the basic processor init here, including setting up
the caches, FPU, DSP, etc. By the time \ :c:func:`start_kernel`\  is hit (and
subsequently \ :c:func:`platform_setup`\ ) things like determining the CPU
subtype and initial configuration will all be done.

Each processor family is still responsible for doing its own probing
and cache configuration in \ :c:func:`cpu_probe`\ .

.. This file was automatic generated / don't edit.

