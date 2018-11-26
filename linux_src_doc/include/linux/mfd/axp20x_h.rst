.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/axp20x.h

.. _`axp20x_match_device`:

axp20x_match_device
===================

.. c:function:: int axp20x_match_device(struct axp20x_dev *axp20x)

    Setup axp20x variant related fields

    :param axp20x:
        axp20x device to setup (.dev field must be set)
    :type axp20x: struct axp20x_dev \*

.. _`axp20x_match_device.description`:

Description
-----------

This lets the axp20x core configure the mfd cells and register maps
for later use.

.. _`axp20x_device_probe`:

axp20x_device_probe
===================

.. c:function:: int axp20x_device_probe(struct axp20x_dev *axp20x)

    Probe a configured axp20x device

    :param axp20x:
        axp20x device to probe (must be configured)
    :type axp20x: struct axp20x_dev \*

.. _`axp20x_device_probe.description`:

Description
-----------

This function lets the axp20x core register the axp20x mfd devices
and irqchip. The axp20x device passed in must be fully configured
with axp20x_match_device, its irq set, and regmap created.

.. _`axp20x_device_remove`:

axp20x_device_remove
====================

.. c:function:: int axp20x_device_remove(struct axp20x_dev *axp20x)

    Remove a axp20x device

    :param axp20x:
        axp20x device to remove
    :type axp20x: struct axp20x_dev \*

.. _`axp20x_device_remove.description`:

Description
-----------

This tells the axp20x core to remove the associated mfd devices

.. This file was automatic generated / don't edit.

