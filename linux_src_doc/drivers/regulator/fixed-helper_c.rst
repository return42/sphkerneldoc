.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/fixed-helper.c

.. _`regulator_register_always_on`:

regulator_register_always_on
============================

.. c:function:: struct platform_device *regulator_register_always_on(int id, const char *name, struct regulator_consumer_supply *supplies, int num_supplies, int uv)

    register a no-op fixed regulator

    :param int id:
        platform device id

    :param const char \*name:
        name to be used for the regulator

    :param struct regulator_consumer_supply \*supplies:
        consumers for this regulator

    :param int num_supplies:
        number of consumers

    :param int uv:
        voltage in microvolts

.. This file was automatic generated / don't edit.

