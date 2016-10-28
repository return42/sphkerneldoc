.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/speedstep-centrino.c

.. _`centrino_target`:

centrino_target
===============

.. c:function:: int centrino_target(struct cpufreq_policy *policy, unsigned int index)

    set a new CPUFreq policy

    :param struct cpufreq_policy \*policy:
        new policy

    :param unsigned int index:
        index of target frequency

.. _`centrino_target.description`:

Description
-----------

Sets a new CPUFreq policy.

.. _`centrino_init`:

centrino_init
=============

.. c:function:: int centrino_init( void)

    initializes the Enhanced SpeedStep CPUFreq driver

    :param  void:
        no arguments

.. _`centrino_init.description`:

Description
-----------

Initializes the Enhanced SpeedStep support. Returns -ENODEV on
unsupported devices, -ENOENT if there's no voltage table for this
particular CPU model, -EINVAL on problems during initiatization,
and zero on success.

This is quite picky.  Not only does the CPU have to advertise the
"est" flag in the cpuid capability flags, we look for a specific
CPU model and stepping, and we need to have the exact model name in
our voltage tables.  That is, be paranoid about not releasing
someone's valuable magic smoke.

.. This file was automatic generated / don't edit.

