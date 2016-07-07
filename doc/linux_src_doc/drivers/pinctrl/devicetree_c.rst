.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/devicetree.c

.. _`pinctrl_dt_map`:

struct pinctrl_dt_map
=====================

.. c:type:: struct pinctrl_dt_map

    mapping table chunk parsed from device tree

.. _`pinctrl_dt_map.definition`:

Definition
----------

.. code-block:: c

    struct pinctrl_dt_map {
        struct list_head node;
        struct pinctrl_dev *pctldev;
        struct pinctrl_map *map;
        unsigned num_maps;
    }

.. _`pinctrl_dt_map.members`:

Members
-------

node
    list node for struct pinctrl's \ ``dt_maps``\  field

pctldev
    the pin controller that allocated this struct, and will free it

map
    *undescribed*

num_maps
    *undescribed*

.. This file was automatic generated / don't edit.

