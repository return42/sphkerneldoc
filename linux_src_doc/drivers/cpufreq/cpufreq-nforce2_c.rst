.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/cpufreq-nforce2.c

.. _`nforce2_calc_fsb`:

nforce2_calc_fsb
================

.. c:function:: int nforce2_calc_fsb(int pll)

    calculate FSB

    :param int pll:
        PLL value

.. _`nforce2_calc_fsb.description`:

Description
-----------

Calculates FSB from PLL value

.. _`nforce2_calc_pll`:

nforce2_calc_pll
================

.. c:function:: int nforce2_calc_pll(unsigned int fsb)

    calculate PLL value

    :param unsigned int fsb:
        FSB

.. _`nforce2_calc_pll.description`:

Description
-----------

Calculate PLL value for given FSB

.. _`nforce2_write_pll`:

nforce2_write_pll
=================

.. c:function:: void nforce2_write_pll(int pll)

    write PLL value to chipset

    :param int pll:
        PLL value

.. _`nforce2_write_pll.description`:

Description
-----------

Writes new FSB PLL value to chipset

.. _`nforce2_fsb_read`:

nforce2_fsb_read
================

.. c:function:: unsigned int nforce2_fsb_read(int bootfsb)

    Read FSB

    :param int bootfsb:
        *undescribed*

.. _`nforce2_fsb_read.description`:

Description
-----------

Read FSB from chipset
If bootfsb != 0, return FSB at boot-time

.. _`nforce2_set_fsb`:

nforce2_set_fsb
===============

.. c:function:: int nforce2_set_fsb(unsigned int fsb)

    set new FSB

    :param unsigned int fsb:
        New FSB

.. _`nforce2_set_fsb.description`:

Description
-----------

Sets new FSB

.. _`nforce2_get`:

nforce2_get
===========

.. c:function:: unsigned int nforce2_get(unsigned int cpu)

    get the CPU frequency

    :param unsigned int cpu:
        CPU number

.. _`nforce2_get.description`:

Description
-----------

Returns the CPU frequency

.. _`nforce2_target`:

nforce2_target
==============

.. c:function:: int nforce2_target(struct cpufreq_policy *policy, unsigned int target_freq, unsigned int relation)

    set a new CPUFreq policy

    :param struct cpufreq_policy \*policy:
        new policy

    :param unsigned int target_freq:
        the target frequency

    :param unsigned int relation:
        how that frequency relates to achieved frequency
        (CPUFREQ_RELATION_L or CPUFREQ_RELATION_H)

.. _`nforce2_target.description`:

Description
-----------

Sets a new CPUFreq policy.

.. _`nforce2_verify`:

nforce2_verify
==============

.. c:function:: int nforce2_verify(struct cpufreq_policy *policy)

    verifies a new CPUFreq policy

    :param struct cpufreq_policy \*policy:
        new policy

.. _`nforce2_detect_chipset`:

nforce2_detect_chipset
======================

.. c:function:: int nforce2_detect_chipset( void)

    detect the Southbridge which contains FSB PLL logic

    :param  void:
        no arguments

.. _`nforce2_detect_chipset.description`:

Description
-----------

Detects nForce2 A2 and C1 stepping

.. _`nforce2_init`:

nforce2_init
============

.. c:function:: int nforce2_init( void)

    initializes the nForce2 CPUFreq driver

    :param  void:
        no arguments

.. _`nforce2_init.description`:

Description
-----------

Initializes the nForce2 FSB support. Returns -ENODEV on unsupported
devices, -EINVAL on problems during initialization, and zero on
success.

.. _`nforce2_exit`:

nforce2_exit
============

.. c:function:: void __exit nforce2_exit( void)

    unregisters cpufreq module

    :param  void:
        no arguments

.. _`nforce2_exit.description`:

Description
-----------

Unregisters nForce2 FSB change support.

.. This file was automatic generated / don't edit.

