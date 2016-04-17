.. -*- coding: utf-8; mode: rst -*-

=======
setup.c
=======


.. _`setup_cpu`:

setup_cpu
=========

.. c:function:: void setup_cpu (int boot)

    Do all necessary per-cpu, tile-specific initialization.

    :param int boot:
        Is this the boot cpu?



.. _`setup_cpu.description`:

Description
-----------

Called from :c:func:`setup_arch` on the boot cpu, or :c:func:`online_secondary`.

