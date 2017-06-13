.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-rockchip.c

.. _`iomux_gpio_only`:

IOMUX_GPIO_ONLY
===============

.. c:function::  IOMUX_GPIO_ONLY()

.. _`rockchip_pin_drv_type`:

enum rockchip_pin_drv_type
==========================

.. c:type:: enum rockchip_pin_drv_type


.. _`rockchip_pin_drv_type.definition`:

Definition
----------

.. code-block:: c

    enum rockchip_pin_drv_type {
        DRV_TYPE_IO_DEFAULT,
        DRV_TYPE_IO_1V8_OR_3V0,
        DRV_TYPE_IO_1V8_ONLY,
        DRV_TYPE_IO_1V8_3V0_AUTO,
        DRV_TYPE_IO_3V3_ONLY,
        DRV_TYPE_MAX
    };

.. _`rockchip_pin_drv_type.constants`:

Constants
---------

DRV_TYPE_IO_DEFAULT
    *undescribed*

DRV_TYPE_IO_1V8_OR_3V0
    *undescribed*

DRV_TYPE_IO_1V8_ONLY
    *undescribed*

DRV_TYPE_IO_1V8_3V0_AUTO
    *undescribed*

DRV_TYPE_IO_3V3_ONLY
    *undescribed*

DRV_TYPE_MAX
    *undescribed*

.. _`rockchip_pin_pull_type`:

enum rockchip_pin_pull_type
===========================

.. c:type:: enum rockchip_pin_pull_type


.. _`rockchip_pin_pull_type.definition`:

Definition
----------

.. code-block:: c

    enum rockchip_pin_pull_type {
        PULL_TYPE_IO_DEFAULT,
        PULL_TYPE_IO_1V8_ONLY,
        PULL_TYPE_MAX
    };

.. _`rockchip_pin_pull_type.constants`:

Constants
---------

PULL_TYPE_IO_DEFAULT
    *undescribed*

PULL_TYPE_IO_1V8_ONLY
    *undescribed*

PULL_TYPE_MAX
    *undescribed*

.. _`rockchip_pin_group`:

struct rockchip_pin_group
=========================

.. c:type:: struct rockchip_pin_group

    represent group of pins of a pinmux function.

.. _`rockchip_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_pin_group {
        const char *name;
        unsigned int npins;
        unsigned int *pins;
        struct rockchip_pin_config *data;
    }

.. _`rockchip_pin_group.members`:

Members
-------

name
    name of the pin group, used to lookup the group.

npins
    number of pins included in this group.

pins
    the pins included in this group.

data
    *undescribed*

.. _`rockchip_pmx_func`:

struct rockchip_pmx_func
========================

.. c:type:: struct rockchip_pmx_func

    represent a pin function.

.. _`rockchip_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_pmx_func {
        const char *name;
        const char **groups;
        u8 ngroups;
    }

.. _`rockchip_pmx_func.members`:

Members
-------

name
    name of the pin function, used to lookup the function.

groups
    one or more names of pin groups that provide this function.

ngroups
    *undescribed*

.. _`rockchip_mux_recalced_data`:

struct rockchip_mux_recalced_data
=================================

.. c:type:: struct rockchip_mux_recalced_data

    represent a pin iomux data.

.. _`rockchip_mux_recalced_data.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_mux_recalced_data {
        u8 num;
        u8 pin;
        u8 reg;
        u8 bit;
        u8 mask;
    }

.. _`rockchip_mux_recalced_data.members`:

Members
-------

num
    bank number.

pin
    pin number.

reg
    register offset.

bit
    index at register.

mask
    mask bit

.. This file was automatic generated / don't edit.

