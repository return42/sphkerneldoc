.. -*- coding: utf-8; mode: rst -*-

==============
setup-common.c
==============


.. _`smp_setup_cpu_maps`:

smp_setup_cpu_maps
==================

.. c:function:: void smp_setup_cpu_maps ( void)

    initialize the following cpu maps: cpu_possible_mask cpu_present_mask

    :param void:
        no arguments



.. _`smp_setup_cpu_maps.description`:

Description
-----------


Having the possible map set up early allows us to restrict allocations
of things like irqstacks to nr_cpu_ids rather than NR_CPUS.

We do not initialize the online map here; cpus set their own bits in
cpu_online_mask as they come up.

This function is valid only for Open Firmware systems.  finish_device_tree
must be called before using this.

While we're here, we may as well set the "physical" cpu ids in the paca.



.. _`smp_setup_cpu_maps.note`:

NOTE
----

This must match the parsing done in early_init_dt_scan_cpus.

