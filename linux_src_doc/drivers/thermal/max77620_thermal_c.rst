.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/max77620_thermal.c

.. _`max77620_thermal_read_temp`:

max77620_thermal_read_temp
==========================

.. c:function:: int max77620_thermal_read_temp(void *data, int *temp)

    Read PMIC die temperatue.

    :param data:
        Device specific data.
    :type data: void \*

    :param temp:
        *undescribed*
    :type temp: int \*

.. _`max77620_thermal_read_temp.temp`:

temp
----

Temperature in millidegrees Celsius

The actual temperature of PMIC die is not available from PMIC.
PMIC only tells the status if it has crossed or not the threshold level
of 120degC or 140degC.
If threshold has not been crossed then assume die temperature as 100degC
else 120degC or 140deG based on the PMIC die temp threshold status.

Return 0 on success otherwise error number to show reason of failure.

.. This file was automatic generated / don't edit.

