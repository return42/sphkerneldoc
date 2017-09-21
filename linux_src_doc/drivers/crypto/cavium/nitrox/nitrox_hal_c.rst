.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_hal.c

.. _`emu_enable_cores`:

emu_enable_cores
================

.. c:function:: void emu_enable_cores(struct nitrox_device *ndev)

    Enable EMU cluster cores.

    :param struct nitrox_device \*ndev:
        N5 device

.. _`nitrox_config_emu_unit`:

nitrox_config_emu_unit
======================

.. c:function:: void nitrox_config_emu_unit(struct nitrox_device *ndev)

    configure EMU unit.

    :param struct nitrox_device \*ndev:
        N5 device

.. _`nitrox_config_pkt_input_rings`:

nitrox_config_pkt_input_rings
=============================

.. c:function:: void nitrox_config_pkt_input_rings(struct nitrox_device *ndev)

    configure Packet Input Rings

    :param struct nitrox_device \*ndev:
        N5 device

.. _`enable_nps_interrupts`:

enable_nps_interrupts
=====================

.. c:function:: void enable_nps_interrupts(struct nitrox_device *ndev)

    enable NPS interrutps

    :param struct nitrox_device \*ndev:
        N5 device.

.. _`enable_nps_interrupts.description`:

Description
-----------

This includes NPS core, packet in and slc interrupts.

.. _`nitrox_config_rand_unit`:

nitrox_config_rand_unit
=======================

.. c:function:: void nitrox_config_rand_unit(struct nitrox_device *ndev)

    enable N5 random number unit

    :param struct nitrox_device \*ndev:
        N5 device

.. This file was automatic generated / don't edit.

