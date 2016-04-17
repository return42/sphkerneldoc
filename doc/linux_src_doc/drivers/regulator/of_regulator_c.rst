.. -*- coding: utf-8; mode: rst -*-

==============
of_regulator.c
==============


.. _`of_get_regulator_init_data`:

of_get_regulator_init_data
==========================

.. c:function:: struct regulator_init_data *of_get_regulator_init_data (struct device *dev, struct device_node *node, const struct regulator_desc *desc)

    extract regulator_init_data structure info

    :param struct device \*dev:
        device requesting for regulator_init_data

    :param struct device_node \*node:
        regulator device node

    :param const struct regulator_desc \*desc:
        regulator description



.. _`of_get_regulator_init_data.description`:

Description
-----------

Populates regulator_init_data structure by extracting data from device
tree node, returns a pointer to the populated struture or NULL if memory
alloc fails.



.. _`of_regulator_match`:

of_regulator_match
==================

.. c:function:: int of_regulator_match (struct device *dev, struct device_node *node, struct of_regulator_match *matches, unsigned int num_matches)

    extract multiple regulator init data from device tree.

    :param struct device \*dev:
        device requesting the data

    :param struct device_node \*node:
        parent device node of the regulators

    :param struct of_regulator_match \*matches:
        match table for the regulators

    :param unsigned int num_matches:
        number of entries in match table



.. _`of_regulator_match.description`:

Description
-----------

This function uses a match table specified by the regulator driver to
parse regulator init data from the device tree. ``node`` is expected to
contain a set of child nodes, each providing the init data for one
regulator. The data parsed from a child node will be matched to a regulator
based on either the deprecated property regulator-compatible if present,
or otherwise the child node's name. Note that the match table is modified
in place and an additional of_node reference is taken for each matched
regulator.

Returns the number of matches found or a negative error code on failure.

