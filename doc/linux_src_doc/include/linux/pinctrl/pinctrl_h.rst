.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pinctrl/pinctrl.h

.. _`pinctrl_pin_desc`:

struct pinctrl_pin_desc
=======================

.. c:type:: struct pinctrl_pin_desc

    boards/machines provide information on their pins, pads or other muxable units in this struct

.. _`pinctrl_pin_desc.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_pin_desc {
        unsigned number;
        const char *name;
        void *drv_data;
    }

.. _`pinctrl_pin_desc.members`:

Members
-------

number
    unique pin number from the global pin number space

name
    a name for this pin

drv_data
    driver-defined per-pin data. pinctrl core does not touch this

.. _`pinctrl_gpio_range`:

struct pinctrl_gpio_range
=========================

.. c:type:: struct pinctrl_gpio_range

    each pin controller can provide subranges of the GPIO number space to be handled by the controller

.. _`pinctrl_gpio_range.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_gpio_range {
        struct list_head node;
        const char *name;
        unsigned int id;
        unsigned int base;
        unsigned int pin_base;
        unsigned const *pins;
        unsigned int npins;
        struct gpio_chip *gc;
    }

.. _`pinctrl_gpio_range.members`:

Members
-------

node
    list node for internal use

name
    a name for the chip in this range

id
    an ID number for the chip in this range

base
    base offset of the GPIO range

pin_base
    base pin number of the GPIO range if pins == NULL

pins
    enumeration of pins in GPIO range or NULL

npins
    number of pins in the GPIO range, including the base number

gc
    an optional pointer to a gpio_chip

.. _`pinctrl_ops`:

struct pinctrl_ops
==================

.. c:type:: struct pinctrl_ops

    global pin control operations, to be implemented by pin controller drivers.

.. _`pinctrl_ops.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_ops {
        int (* get_groups_count) (struct pinctrl_dev *pctldev);
        const char *(* get_group_name) (struct pinctrl_dev *pctldev,unsigned selector);
        int (* get_group_pins) (struct pinctrl_dev *pctldev,unsigned selector,const unsigned **pins,unsigned *num_pins);
        void (* pin_dbg_show) (struct pinctrl_dev *pctldev, struct seq_file *s,unsigned offset);
        int (* dt_node_to_map) (struct pinctrl_dev *pctldev,struct device_node *np_config,struct pinctrl_map **map, unsigned *num_maps);
        void (* dt_free_map) (struct pinctrl_dev *pctldev,struct pinctrl_map *map, unsigned num_maps);
    }

.. _`pinctrl_ops.members`:

Members
-------

get_groups_count
    Returns the count of total number of groups registered.

get_group_name
    return the group name of the pin group

get_group_pins
    return an array of pins corresponding to a certain
    group selector \ ``pins``\ , and the size of the array in \ ``num_pins``\ 

pin_dbg_show
    optional debugfs display hook that will provide per-device
    info for a certain pin in debugfs

dt_node_to_map
    parse a device tree "pin configuration node", and create
    mapping table entries for it. These are returned through the \ ``map``\  and
    \ ``num_maps``\  output parameters. This function is optional, and may be
    omitted for pinctrl drivers that do not support device tree.

dt_free_map
    free mapping table entries created via \ ``dt_node_to_map``\ . The
    top-level \ ``map``\  pointer must be freed, along with any dynamically
    allocated members of the mapping table entries themselves. This
    function is optional, and may be omitted for pinctrl drivers that do
    not support device tree.

.. _`pinctrl_desc`:

struct pinctrl_desc
===================

.. c:type:: struct pinctrl_desc

    pin controller descriptor, register this to pin control subsystem

.. _`pinctrl_desc.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_desc {
        const char *name;
        const struct pinctrl_pin_desc *pins;
        unsigned int npins;
        const struct pinctrl_ops *pctlops;
        const struct pinmux_ops *pmxops;
        const struct pinconf_ops *confops;
        struct module *owner;
        #ifdef CONFIG_GENERIC_PINCONF
        unsigned int num_custom_params;
        const struct pinconf_generic_params *custom_params;
        const struct pin_config_item *custom_conf_items;
        #endif
    }

.. _`pinctrl_desc.members`:

Members
-------

name
    name for the pin controller

pins
    an array of pin descriptors describing all the pins handled by
    this pin controller

npins
    number of descriptors in the array, usually just \ :c:func:`ARRAY_SIZE`\ 
    of the pins field above

pctlops
    pin control operation vtable, to support global concepts like
    grouping of pins, this is optional.

pmxops
    pinmux operations vtable, if you support pinmuxing in your driver

confops
    pin config operations vtable, if you support pin configuration in
    your driver

owner
    module providing the pin controller, used for refcounting

num_custom_params
    Number of driver-specific custom parameters to be parsed
    from the hardware description

custom_params
    List of driver_specific custom parameters to be parsed from
    the hardware description

custom_conf_items
    Information how to print \ ``params``\  in debugfs, must be
    the same size as the \ ``custom_params``\ , i.e. \ ``num_custom_params``\ 

.. This file was automatic generated / don't edit.

