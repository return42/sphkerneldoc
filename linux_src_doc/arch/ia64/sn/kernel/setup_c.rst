.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/sn/kernel/setup.c

.. _`early_sn_setup`:

early_sn_setup
==============

.. c:function:: void early_sn_setup( void)

    early setup routine for SN platforms

    :param  void:
        no arguments

.. _`early_sn_setup.description`:

Description
-----------

Sets up an initial console to aid debugging.  Intended primarily
for bringup.  See \ :c:func:`start_kernel`\  in init/main.c.

.. _`sn_setup`:

sn_setup
========

.. c:function:: void sn_setup(char **cmdline_p)

    SN platform setup routine

    :param char \*\*cmdline_p:
        kernel command line

.. _`sn_setup.description`:

Description
-----------

Handles platform setup for SN machines.  This includes determining
the RTC frequency (via a SAL call), initializing secondary CPUs, and
setting up per-node data areas.  The console is also initialized here.

.. _`sn_init_pdas`:

sn_init_pdas
============

.. c:function:: void sn_init_pdas(char **cmdline_p)

    setup node data areas

    :param char \*\*cmdline_p:
        *undescribed*

.. _`sn_init_pdas.description`:

Description
-----------

One time setup for Node Data Area.  Called by \ :c:func:`sn_setup`\ .

.. _`sn_cpu_init`:

sn_cpu_init
===========

.. c:function:: void sn_cpu_init( void)

    initialize per-cpu data areas

    :param  void:
        no arguments

.. _`sn_cpu_init.description`:

Description
-----------

Called during cpu initialization on each cpu as it starts.
Currently, initializes the per-cpu data area for SNIA.
Also sets up a few fields in the nodepda.  Also known as
\ :c:func:`platform_cpu_init`\  by the ia64 machvec code.

.. This file was automatic generated / don't edit.

