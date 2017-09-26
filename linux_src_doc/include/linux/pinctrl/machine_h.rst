.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pinctrl/machine.h

.. _`pinctrl_map_mux`:

struct pinctrl_map_mux
======================

.. c:type:: struct pinctrl_map_mux

    mapping table content for MAP_TYPE_MUX_GROUP

.. _`pinctrl_map_mux.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_map_mux {
        const char *group;
        const char *function;
    }

.. _`pinctrl_map_mux.members`:

Members
-------

group
    the name of the group whose mux function is to be configured. This
    field may be left NULL, and the first applicable group for the function
    will be used.

function
    the mux function to select for the group

.. _`pinctrl_map_configs`:

struct pinctrl_map_configs
==========================

.. c:type:: struct pinctrl_map_configs

    mapping table content for MAP_TYPE_CONFIGS\_\*

.. _`pinctrl_map_configs.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_map_configs {
        const char *group_or_pin;
        unsigned long *configs;
        unsigned num_configs;
    }

.. _`pinctrl_map_configs.members`:

Members
-------

group_or_pin
    the name of the pin or group whose configuration parameters
    are to be configured.

configs
    a pointer to an array of config parameters/values to program into
    hardware. Each individual pin controller defines the format and meaning
    of config parameters.

num_configs
    the number of entries in array \ ``configs``\ 

.. _`pinctrl_map`:

struct pinctrl_map
==================

.. c:type:: struct pinctrl_map

    boards/machines shall provide this map for devices

.. _`pinctrl_map.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_map {
        const char *dev_name;
        const char *name;
        enum pinctrl_map_type type;
        const char *ctrl_dev_name;
        union {
            struct pinctrl_map_mux mux;
            struct pinctrl_map_configs configs;
        } data;
    }

.. _`pinctrl_map.members`:

Members
-------

dev_name
    the name of the device using this specific mapping, the name
    must be the same as in your struct device\*. If this name is set to the
    same name as the pin controllers own \ :c:func:`dev_name`\ , the map entry will be
    hogged by the driver itself upon registration

name
    the name of this specific map entry for the particular machine.
    This is the parameter passed to \ :c:func:`pinmux_lookup_state`\ 

type
    the type of mapping table entry

ctrl_dev_name
    the name of the device controlling this specific mapping,
    the name must be the same as in your struct device\*. This field is not
    used for PIN_MAP_TYPE_DUMMY_STATE

data
    Data specific to the mapping type

mux
    *undescribed*

configs
    *undescribed*

.. This file was automatic generated / don't edit.

