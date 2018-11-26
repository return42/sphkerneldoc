.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/of_regulator.c

.. _`of_get_regulator_init_data`:

of_get_regulator_init_data
==========================

.. c:function:: struct regulator_init_data *of_get_regulator_init_data(struct device *dev, struct device_node *node, const struct regulator_desc *desc)

    extract regulator_init_data structure info

    :param dev:
        device requesting for regulator_init_data
    :type dev: struct device \*

    :param node:
        regulator device node
    :type node: struct device_node \*

    :param desc:
        regulator description
    :type desc: const struct regulator_desc \*

.. _`of_get_regulator_init_data.description`:

Description
-----------

Populates regulator_init_data structure by extracting data from device
tree node, returns a pointer to the populated struture or NULL if memory
alloc fails.

.. _`of_regulator_match`:

of_regulator_match
==================

.. c:function:: int of_regulator_match(struct device *dev, struct device_node *node, struct of_regulator_match *matches, unsigned int num_matches)

    extract multiple regulator init data from device tree.

    :param dev:
        device requesting the data
    :type dev: struct device \*

    :param node:
        parent device node of the regulators
    :type node: struct device_node \*

    :param matches:
        match table for the regulators
    :type matches: struct of_regulator_match \*

    :param num_matches:
        number of entries in match table
    :type num_matches: unsigned int

.. _`of_regulator_match.description`:

Description
-----------

This function uses a match table specified by the regulator driver to
parse regulator init data from the device tree. \ ``node``\  is expected to
contain a set of child nodes, each providing the init data for one
regulator. The data parsed from a child node will be matched to a regulator
based on either the deprecated property regulator-compatible if present,
or otherwise the child node's name. Note that the match table is modified
in place and an additional of_node reference is taken for each matched
regulator.

Returns the number of matches found or a negative error code on failure.

.. _`of_check_coupling_data`:

of_check_coupling_data
======================

.. c:function:: bool of_check_coupling_data(struct regulator_dev *rdev)

    Parse rdev's coupling properties and check data consistency \ ``rdev``\  - pointer to regulator_dev whose data is checked

    :param rdev:
        *undescribed*
    :type rdev: struct regulator_dev \*

.. _`of_check_coupling_data.function-checks-if-all-the-following-conditions-are-met`:

Function checks if all the following conditions are met
-------------------------------------------------------

- rdev's max_spread is greater than 0
- all coupled regulators have the same max_spread
- all coupled regulators have the same number of regulator_dev phandles
- all regulators are linked to each other

Returns true if all conditions are met.

.. _`of_parse_coupled_regulator`:

of_parse_coupled_regulator
==========================

.. c:function:: struct regulator_dev *of_parse_coupled_regulator(struct regulator_dev *rdev, int index)

    Get regulator_dev pointer from rdev's property

    :param rdev:
        Pointer to regulator_dev, whose DTS is used as a source to parse
        "regulator-coupled-with" property
    :type rdev: struct regulator_dev \*

    :param index:
        Index in phandles array
    :type index: int

.. _`of_parse_coupled_regulator.description`:

Description
-----------

Returns the regulator_dev pointer parsed from DTS. If it has not been yet
registered, returns NULL

.. This file was automatic generated / don't edit.

