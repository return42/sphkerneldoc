.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/i2c-mux-pinctrl.h

.. _`i2c_mux_pinctrl_platform_data`:

struct i2c_mux_pinctrl_platform_data
====================================

.. c:type:: struct i2c_mux_pinctrl_platform_data

    Platform data for i2c-mux-pinctrl

.. _`i2c_mux_pinctrl_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct i2c_mux_pinctrl_platform_data {
        int parent_bus_num;
        int base_bus_num;
        int bus_count;
        const char **pinctrl_states;
        const char *pinctrl_state_idle;
    }

.. _`i2c_mux_pinctrl_platform_data.members`:

Members
-------

parent_bus_num
    Parent I2C bus number

base_bus_num
    Base I2C bus number for the child busses. 0 for dynamic.

bus_count
    Number of child busses. Also the number of elements in
    \ ``pinctrl_states``\ 

pinctrl_states
    The names of the pinctrl state to select for each child bus

pinctrl_state_idle
    The pinctrl state to select when no child bus is being
    accessed. If NULL, the most recently used pinctrl state will be left
    selected.

.. This file was automatic generated / don't edit.

