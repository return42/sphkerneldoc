.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/gx-suspmod.c

.. _`gx_detect_chipset`:

gx_detect_chipset
=================

.. c:function:: struct pci_dev *gx_detect_chipset( void)

    :param void:
        no arguments
    :type void: 

.. _`gx_get_cpuspeed`:

gx_get_cpuspeed
===============

.. c:function:: unsigned int gx_get_cpuspeed(unsigned int cpu)

    :param cpu:
        *undescribed*
    :type cpu: unsigned int

.. _`gx_get_cpuspeed.description`:

Description
-----------

Finds out at which efficient frequency the Cyrix MediaGX/NatSemi
Geode CPU runs.

.. _`gx_validate_speed`:

gx_validate_speed
=================

.. c:function:: unsigned int gx_validate_speed(unsigned int khz, u8 *on_duration, u8 *off_duration)

    determine current cpu speed

    :param khz:
        *undescribed*
    :type khz: unsigned int

    :param on_duration:
        *undescribed*
    :type on_duration: u8 \*

    :param off_duration:
        *undescribed*
    :type off_duration: u8 \*

.. _`gx_set_cpuspeed`:

gx_set_cpuspeed
===============

.. c:function:: void gx_set_cpuspeed(struct cpufreq_policy *policy, unsigned int khz)

    set cpu speed in khz.

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param khz:
        *undescribed*
    :type khz: unsigned int

.. This file was automatic generated / don't edit.

