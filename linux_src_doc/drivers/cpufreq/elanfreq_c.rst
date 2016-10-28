.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/elanfreq.c

.. _`elanfreq_get_cpu_frequency`:

elanfreq_get_cpu_frequency
==========================

.. c:function:: unsigned int elanfreq_get_cpu_frequency(unsigned int cpu)

    determine current cpu speed

    :param unsigned int cpu:
        *undescribed*

.. _`elanfreq_get_cpu_frequency.description`:

Description
-----------

Finds out at which frequency the CPU of the Elan SOC runs
at the moment. Frequencies from 1 to 33 MHz are generated
the normal way, 66 and 99 MHz are called "Hyperspeed Mode"
and have the rest of the chip running with 33 MHz.

.. _`elanfreq_setup`:

elanfreq_setup
==============

.. c:function:: int elanfreq_setup(char *str)

    elanfreq command line parameter parsing

    :param char \*str:
        *undescribed*

.. _`elanfreq_setup.description`:

Description
-----------

elanfreq command line parameter.  Use:
elanfreq=66000
to set the maximum CPU frequency to 66 MHz. Note that in
case you do not give this boot parameter, the maximum
frequency will fall back to \_current\_ CPU frequency which
might be lower. If you build this as a module, use the
max_freq module parameter instead.

.. This file was automatic generated / don't edit.

