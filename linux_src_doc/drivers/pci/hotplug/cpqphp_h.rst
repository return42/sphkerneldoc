.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/cpqphp.h

.. _`get_controller_speed`:

get_controller_speed
====================

.. c:function:: u8 get_controller_speed(struct controller *ctrl)

    find the current frequency/mode of controller.

    :param ctrl:
        controller to get frequency/mode for.
    :type ctrl: struct controller \*

.. _`get_controller_speed.description`:

Description
-----------

Returns controller speed.

.. _`get_adapter_speed`:

get_adapter_speed
=================

.. c:function:: u8 get_adapter_speed(struct controller *ctrl, u8 hp_slot)

    find the max supported frequency/mode of adapter.

    :param ctrl:
        hotplug controller.
    :type ctrl: struct controller \*

    :param hp_slot:
        hotplug slot where adapter is installed.
    :type hp_slot: u8

.. _`get_adapter_speed.description`:

Description
-----------

Returns adapter speed.

.. This file was automatic generated / don't edit.

