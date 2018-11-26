.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/speedstep-smi.c

.. _`speedstep_smi_ownership`:

speedstep_smi_ownership
=======================

.. c:function:: int speedstep_smi_ownership( void)

    :param void:
        no arguments
    :type void: 

.. _`speedstep_smi_get_freqs`:

speedstep_smi_get_freqs
=======================

.. c:function:: int speedstep_smi_get_freqs(unsigned int *low, unsigned int *high)

    get SpeedStep preferred & current freq.

    :param low:
        the low frequency value is placed here
    :type low: unsigned int \*

    :param high:
        the high frequency value is placed here
    :type high: unsigned int \*

.. _`speedstep_smi_get_freqs.description`:

Description
-----------

Only available on later SpeedStep-enabled systems, returns false results or
even hangs [cf. bugme.osdl.org # 1422] on earlier systems. Empirical testing
shows that the latter occurs if !(ist_info.event & 0xFFFF).

.. _`speedstep_set_state`:

speedstep_set_state
===================

.. c:function:: void speedstep_set_state(unsigned int state)

    set the SpeedStep state

    :param state:
        new processor frequency state (SPEEDSTEP_LOW or SPEEDSTEP_HIGH)
    :type state: unsigned int

.. _`speedstep_target`:

speedstep_target
================

.. c:function:: int speedstep_target(struct cpufreq_policy *policy, unsigned int index)

    set a new CPUFreq policy

    :param policy:
        new policy
    :type policy: struct cpufreq_policy \*

    :param index:
        index of new freq
    :type index: unsigned int

.. _`speedstep_target.description`:

Description
-----------

Sets a new CPUFreq policy/freq.

.. _`speedstep_init`:

speedstep_init
==============

.. c:function:: int speedstep_init( void)

    initializes the SpeedStep CPUFreq driver

    :param void:
        no arguments
    :type void: 

.. _`speedstep_init.description`:

Description
-----------

Initializes the SpeedStep support. Returns -ENODEV on unsupported
BIOS, -EINVAL on problems during initiatization, and zero on
success.

.. _`speedstep_exit`:

speedstep_exit
==============

.. c:function:: void __exit speedstep_exit( void)

    unregisters SpeedStep support

    :param void:
        no arguments
    :type void: 

.. _`speedstep_exit.description`:

Description
-----------

Unregisters SpeedStep support.

.. This file was automatic generated / don't edit.

