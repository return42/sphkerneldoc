.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/pmu.c

.. _`omap2_init_pmu`:

omap2_init_pmu
==============

.. c:function:: int omap2_init_pmu(unsigned oh_num, char  *oh_names)

    creates and registers PMU platform device

    :param unsigned oh_num:
        Number of OMAP HWMODs required to create PMU device

    :param char  \*oh_names:
        Array of OMAP HWMODS names required to create PMU device

.. _`omap2_init_pmu.description`:

Description
-----------

Uses OMAP HWMOD framework to create and register an ARM PMU device
from a list of HWMOD names passed. Currently supports OMAP2, OMAP3
and OMAP4 devices.

.. This file was automatic generated / don't edit.

