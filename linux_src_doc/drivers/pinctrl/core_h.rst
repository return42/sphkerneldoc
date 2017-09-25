.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/core.h

.. _`pinctrl_dev`:

struct pinctrl_dev
==================

.. c:type:: struct pinctrl_dev

    pin control class device

.. _`pinctrl_dev.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_dev {
        struct list_head node;
        struct pinctrl_desc *desc;
        struct radix_tree_root pin_desc_tree;
    #ifdef CONFIG_GENERIC_PINCTRL_GROUPS
        struct radix_tree_root pin_group_tree;
        unsigned int num_groups;
    #endif
    #ifdef CONFIG_GENERIC_PINMUX_FUNCTIONS
        struct radix_tree_root pin_function_tree;
        unsigned int num_functions;
    #endif
        struct list_head gpio_ranges;
        struct device *dev;
        struct module *owner;
        void *driver_data;
        struct pinctrl *p;
        struct pinctrl_state *hog_default;
        struct pinctrl_state *hog_sleep;
        struct mutex mutex;
    #ifdef CONFIG_DEBUG_FS
        struct dentry *device_root;
    #endif
    }

.. _`pinctrl_dev.members`:

Members
-------

node
    node to include this pin controller in the global pin controller list

desc
    the pin controller descriptor supplied when initializing this pin
    controller

pin_desc_tree
    each pin descriptor for this pin controller is stored in
    this radix tree

pin_group_tree
    optionally each pin group can be stored in this radix tree

num_groups
    optionally number of groups can be kept here

pin_function_tree
    optionally each function can be stored in this radix tree

num_functions
    optionally number of functions can be kept here

gpio_ranges
    a list of GPIO ranges that is handled by this pin controller,
    ranges are added to this list at runtime

dev
    the device entry for this pin controller

owner
    module providing the pin controller, used for refcounting

driver_data
    driver data for drivers registering to the pin controller
    subsystem

p
    result of \ :c:func:`pinctrl_get`\  for this device

hog_default
    default state for pins hogged by this device

hog_sleep
    sleep state for pins hogged by this device

mutex
    mutex taken on each pin controller specific action

device_root
    debugfs root for this device

.. _`pinctrl`:

struct pinctrl
==============

.. c:type:: struct pinctrl

    per-device pin control state holder

.. _`pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl {
        struct list_head node;
        struct device *dev;
        struct list_head states;
        struct pinctrl_state *state;
        struct list_head dt_maps;
        struct kref users;
    }

.. _`pinctrl.members`:

Members
-------

node
    global list node

dev
    the device using this pin control handle

states
    a list of states for this device

state
    the current state

dt_maps
    the mapping table chunks dynamically parsed from device tree for
    this device, if any

users
    reference count

.. _`pinctrl_state`:

struct pinctrl_state
====================

.. c:type:: struct pinctrl_state

    a pinctrl state for a device

.. _`pinctrl_state.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_state {
        struct list_head node;
        const char *name;
        struct list_head settings;
    }

.. _`pinctrl_state.members`:

Members
-------

node
    list node for struct pinctrl's \ ``states``\  field

name
    the name of this state

settings
    a list of settings for this state

.. _`pinctrl_setting_mux`:

struct pinctrl_setting_mux
==========================

.. c:type:: struct pinctrl_setting_mux

    setting data for MAP_TYPE_MUX_GROUP

.. _`pinctrl_setting_mux.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_setting_mux {
        unsigned group;
        unsigned func;
    }

.. _`pinctrl_setting_mux.members`:

Members
-------

group
    the group selector to program

func
    the function selector to program

.. _`pinctrl_setting_configs`:

struct pinctrl_setting_configs
==============================

.. c:type:: struct pinctrl_setting_configs

    setting data for MAP_TYPE_CONFIGS\_\*

.. _`pinctrl_setting_configs.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_setting_configs {
        unsigned group_or_pin;
        unsigned long *configs;
        unsigned num_configs;
    }

.. _`pinctrl_setting_configs.members`:

Members
-------

group_or_pin
    the group selector or pin ID to program

configs
    a pointer to an array of config parameters/values to program into
    hardware. Each individual pin controller defines the format and meaning
    of config parameters.

num_configs
    the number of entries in array \ ``configs``\ 

.. _`pinctrl_setting`:

struct pinctrl_setting
======================

.. c:type:: struct pinctrl_setting

    an individual mux or config setting

.. _`pinctrl_setting.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_setting {
        struct list_head node;
        enum pinctrl_map_type type;
        struct pinctrl_dev *pctldev;
        const char *dev_name;
        union {
            struct pinctrl_setting_mux mux;
            struct pinctrl_setting_configs configs;
        } data;
    }

.. _`pinctrl_setting.members`:

Members
-------

node
    list node for struct pinctrl_settings's \ ``settings``\  field

type
    the type of setting

pctldev
    pin control device handling to be programmed. Not used for
    PIN_MAP_TYPE_DUMMY_STATE.

dev_name
    the name of the device using this state

mux
    *undescribed*

configs
    *undescribed*

ata
    *undescribed*

.. _`pin_desc`:

struct pin_desc
===============

.. c:type:: struct pin_desc

    pin descriptor for each physical pin in the arch

.. _`pin_desc.definition`:

Definition
----------

.. code-block:: c

    struct pin_desc {
        struct pinctrl_dev *pctldev;
        const char *name;
        bool dynamic_name;
        void *drv_data;
    #ifdef CONFIG_PINMUX
        unsigned mux_usecount;
        const char *mux_owner;
        const struct pinctrl_setting_mux *mux_setting;
        const char *gpio_owner;
    #endif
    }

.. _`pin_desc.members`:

Members
-------

pctldev
    corresponding pin control device

name
    a name for the pin, e.g. the name of the pin/pad/finger on a
    datasheet or such

dynamic_name
    if the name of this pin was dynamically allocated

drv_data
    driver-defined per-pin data. pinctrl core does not touch this

mux_usecount
    If zero, the pin is not claimed, and \ ``owner``\  should be NULL.
    If non-zero, this pin is claimed by \ ``owner``\ . This field is an integer
    rather than a boolean, since \ :c:func:`pinctrl_get`\  might process multiple
    mapping table entries that refer to, and hence claim, the same group
    or pin, and each of these will increment the \ ``usecount``\ .

mux_owner
    The name of device that called \ :c:func:`pinctrl_get`\ .

mux_setting
    The most recent selected mux setting for this pin, if any.

gpio_owner
    If \ :c:func:`pinctrl_request_gpio`\  was called for this pin, this is
    the name of the GPIO that "owns" this pin.

.. _`pinctrl_maps`:

struct pinctrl_maps
===================

.. c:type:: struct pinctrl_maps

    a list item containing part of the mapping table

.. _`pinctrl_maps.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_maps {
        struct list_head node;
        const struct pinctrl_map *maps;
        unsigned num_maps;
    }

.. _`pinctrl_maps.members`:

Members
-------

node
    mapping table list node

maps
    array of mapping table entries

num_maps
    the number of entries in \ ``maps``\ 

.. _`group_desc`:

struct group_desc
=================

.. c:type:: struct group_desc

    generic pin group descriptor

.. _`group_desc.definition`:

Definition
----------

.. code-block:: c

    struct group_desc {
        const char *name;
        int *pins;
        int num_pins;
        void *data;
    }

.. _`group_desc.members`:

Members
-------

name
    name of the pin group

pins
    array of pins that belong to the group

num_pins
    number of pins in the group

data
    pin controller driver specific data

.. This file was automatic generated / don't edit.

