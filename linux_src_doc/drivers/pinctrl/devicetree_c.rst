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

.. _`pinctrl_get_list_and_count`:

pinctrl_get_list_and_count
==========================

.. c:function:: int pinctrl_get_list_and_count(const struct device_node *np, const char *list_name, const __be32 **list, int *cells_size, int *nr_elements)

    Gets the list and it's cell size and number

    :param np:
        pointer to device node with the property
    :type np: const struct device_node \*

    :param list_name:
        property that contains the list
    :type list_name: const char \*

    :param list:
        pointer for the list found
    :type list: const __be32 \*\*

    :param cells_size:
        pointer for the cell size found
    :type cells_size: int \*

    :param nr_elements:
        pointer for the number of elements found
    :type nr_elements: int \*

.. _`pinctrl_get_list_and_count.description`:

Description
-----------

Typically np is a single pinctrl entry containing the list.

.. _`pinctrl_count_index_with_args`:

pinctrl_count_index_with_args
=============================

.. c:function:: int pinctrl_count_index_with_args(const struct device_node *np, const char *list_name)

    Count number of elements in a pinctrl entry

    :param np:
        pointer to device node with the property
    :type np: const struct device_node \*

    :param list_name:
        property that contains the list
    :type list_name: const char \*

.. _`pinctrl_count_index_with_args.description`:

Description
-----------

Counts the number of elements in a pinctrl array consisting of an index
within the controller and a number of u32 entries specified for each
entry. Note that device_node is always for the parent pin controller device.

.. _`pinctrl_copy_args`:

pinctrl_copy_args
=================

.. c:function:: int pinctrl_copy_args(const struct device_node *np, const __be32 *list, int index, int nr_cells, int nr_elem, struct of_phandle_args *out_args)

    Populates of_phandle_args based on index

    :param np:
        pointer to device node with the property
    :type np: const struct device_node \*

    :param list:
        pointer to a list with the elements
    :type list: const __be32 \*

    :param index:
        entry within the list of elements
    :type index: int

    :param nr_cells:
        number of cells in the list
    :type nr_cells: int

    :param nr_elem:
        number of elements for each entry in the list
    :type nr_elem: int

    :param out_args:
        returned values
    :type out_args: struct of_phandle_args \*

.. _`pinctrl_copy_args.description`:

Description
-----------

Populates the of_phandle_args based on the index in the list.

.. _`pinctrl_parse_index_with_args`:

pinctrl_parse_index_with_args
=============================

.. c:function:: int pinctrl_parse_index_with_args(const struct device_node *np, const char *list_name, int index, struct of_phandle_args *out_args)

    Find a node pointed by index in a list

    :param np:
        pointer to device node with the property
    :type np: const struct device_node \*

    :param list_name:
        property that contains the list
    :type list_name: const char \*

    :param index:
        index within the list
    :type index: int

    :param out_args:
        *undescribed*
    :type out_args: struct of_phandle_args \*

.. _`pinctrl_parse_index_with_args.description`:

Description
-----------

Finds the selected element in a pinctrl array consisting of an index
within the controller and a number of u32 entries specified for each
entry. Note that device_node is always for the parent pin controller device.

.. This file was automatic generated / don't edit.

