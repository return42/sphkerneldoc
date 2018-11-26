.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/motorola/phy-mapphone-mdm6600.c

.. _`phy_mdm6600_cmd`:

phy_mdm6600_cmd
===============

.. c:function:: void phy_mdm6600_cmd(struct phy_mdm6600 *ddata, int val)

    send a command request to mdm6600

    :param ddata:
        device driver data
    :type ddata: struct phy_mdm6600 \*

    :param val:
        *undescribed*
    :type val: int

.. _`phy_mdm6600_cmd.description`:

Description
-----------

Configures the three command request GPIOs to the specified value.

.. _`phy_mdm6600_status`:

phy_mdm6600_status
==================

.. c:function:: void phy_mdm6600_status(struct work_struct *work)

    read mdm6600 status lines

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`phy_mdm6600_wakeirq_thread`:

phy_mdm6600_wakeirq_thread
==========================

.. c:function:: irqreturn_t phy_mdm6600_wakeirq_thread(int irq, void *data)

    handle mode1 line OOB wake after booting

    :param irq:
        interrupt
    :type irq: int

    :param data:
        interrupt handler data
    :type data: void \*

.. _`phy_mdm6600_wakeirq_thread.description`:

Description
-----------

GPIO mode1 is used initially as output to configure the USB boot
mode for mdm6600. After booting it is used as input for OOB wake
signal from mdm6600 to the SoC. Just use it for debug info only
for now.

.. _`phy_mdm6600_init_irq`:

phy_mdm6600_init_irq
====================

.. c:function:: void phy_mdm6600_init_irq(struct phy_mdm6600 *ddata)

    initialize mdm6600 status IRQ lines

    :param ddata:
        device driver data
    :type ddata: struct phy_mdm6600 \*

.. _`phy_mdm6600_init_lines`:

phy_mdm6600_init_lines
======================

.. c:function:: int phy_mdm6600_init_lines(struct phy_mdm6600 *ddata)

    initialize mdm6600 GPIO lines

    :param ddata:
        device driver data
    :type ddata: struct phy_mdm6600 \*

.. _`phy_mdm6600_device_power_on`:

phy_mdm6600_device_power_on
===========================

.. c:function:: int phy_mdm6600_device_power_on(struct phy_mdm6600 *ddata)

    power on mdm6600 device

    :param ddata:
        device driver data
    :type ddata: struct phy_mdm6600 \*

.. _`phy_mdm6600_device_power_on.description`:

Description
-----------

To get the integrated USB phy in MDM6600 takes some hoops. We must ensure
the shared USB bootmode GPIOs are configured, then request modem start-up,
reset and power-up.. And then we need to recycle the shared USB bootmode
GPIOs as they are also used for Out of Band (OOB) wake for the USB and
TS 27.010 serial mux.

.. _`phy_mdm6600_device_power_off`:

phy_mdm6600_device_power_off
============================

.. c:function:: void phy_mdm6600_device_power_off(struct phy_mdm6600 *ddata)

    power off mdm6600 device

    :param ddata:
        device driver data
    :type ddata: struct phy_mdm6600 \*

.. This file was automatic generated / don't edit.

