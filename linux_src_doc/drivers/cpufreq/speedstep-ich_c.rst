.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/speedstep-ich.c

.. _`speedstep_find_register`:

speedstep_find_register
=======================

.. c:function:: int speedstep_find_register( void)

    read the PMBASE address

    :param  void:
        no arguments

.. _`speedstep_find_register.return`:

Return
------

-ENODEV if no register could be found

.. _`speedstep_set_state`:

speedstep_set_state
===================

.. c:function:: void speedstep_set_state(unsigned int state)

    set the SpeedStep state

    :param unsigned int state:
        new processor frequency state (SPEEDSTEP_LOW or SPEEDSTEP_HIGH)

.. _`speedstep_set_state.description`:

Description
-----------

Tries to change the SpeedStep state.  Can be called from
smp_call_function_single.

.. _`speedstep_activate`:

speedstep_activate
==================

.. c:function:: int speedstep_activate( void)

    activate SpeedStep control in the chipset

    :param  void:
        no arguments

.. _`speedstep_activate.description`:

Description
-----------

Tries to activate the SpeedStep status and control registers.
Returns -EINVAL on an unsupported chipset, and zero on success.

.. _`speedstep_detect_chipset`:

speedstep_detect_chipset
========================

.. c:function:: unsigned int speedstep_detect_chipset( void)

    detect the Southbridge which contains SpeedStep logic

    :param  void:
        no arguments

.. _`speedstep_detect_chipset.description`:

Description
-----------

Detects ICH2-M, ICH3-M and ICH4-M so far. The pci_dev points to
the LPC bridge / PM module which contains all power-management
functions. Returns the SPEEDSTEP_CHIPSET_-number for the detected
chipset, or zero on failure.

.. _`speedstep_target`:

speedstep_target
================

.. c:function:: int speedstep_target(struct cpufreq_policy *policy, unsigned int index)

    set a new CPUFreq policy

    :param struct cpufreq_policy \*policy:
        new policy

    :param unsigned int index:
        index of target frequency

.. _`speedstep_target.description`:

Description
-----------

Sets a new CPUFreq policy.

.. _`speedstep_init`:

speedstep_init
==============

.. c:function:: int speedstep_init( void)

    initializes the SpeedStep CPUFreq driver

    :param  void:
        no arguments

.. _`speedstep_init.description`:

Description
-----------

Initializes the SpeedStep support. Returns -ENODEV on unsupported
devices, -EINVAL on problems during initiatization, and zero on
success.

.. _`speedstep_exit`:

speedstep_exit
==============

.. c:function:: void __exit speedstep_exit( void)

    unregisters SpeedStep support

    :param  void:
        no arguments

.. _`speedstep_exit.description`:

Description
-----------

Unregisters SpeedStep support.

.. This file was automatic generated / don't edit.

