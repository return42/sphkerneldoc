.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/fixed-helper.c

.. _`regulator_register_always_on`:

regulator_register_always_on
============================

.. c:function:: struct platform_device *regulator_register_always_on(int id, const char *name, struct regulator_consumer_supply *supplies, int num_supplies, int uv)

    register a no-op fixed regulator

    :param id:
        platform device id
    :type id: int

    :param name:
        name to be used for the regulator
    :type name: const char \*

    :param supplies:
        consumers for this regulator
    :type supplies: struct regulator_consumer_supply \*

    :param num_supplies:
        number of consumers
    :type num_supplies: int

    :param uv:
        voltage in microvolts
    :type uv: int

.. This file was automatic generated / don't edit.

