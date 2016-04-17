.. -*- coding: utf-8; mode: rst -*-

========
of_mtd.c
========


.. _`of_get_nand_ecc_mode`:

of_get_nand_ecc_mode
====================

.. c:function:: int of_get_nand_ecc_mode (struct device_node *np)

    Get nand ecc mode for given device_node

    :param struct device_node \*np:
        Pointer to the given device_node



.. _`of_get_nand_ecc_mode.description`:

Description
-----------

The function gets ecc mode string from property 'nand-ecc-mode',
and return its index in nand_ecc_modes table, or errno in error case.



.. _`of_get_nand_ecc_step_size`:

of_get_nand_ecc_step_size
=========================

.. c:function:: int of_get_nand_ecc_step_size (struct device_node *np)

    Get ECC step size associated to the required ECC strength (see below).

    :param struct device_node \*np:
        Pointer to the given device_node



.. _`of_get_nand_ecc_step_size.description`:

Description
-----------

return the ECC step size, or errno in error case.



.. _`of_get_nand_ecc_strength`:

of_get_nand_ecc_strength
========================

.. c:function:: int of_get_nand_ecc_strength (struct device_node *np)

    Get required ECC strength over the correspnding step size as defined by 'nand-ecc-size'

    :param struct device_node \*np:
        Pointer to the given device_node



.. _`of_get_nand_ecc_strength.description`:

Description
-----------

return the ECC strength, or errno in error case.



.. _`of_get_nand_bus_width`:

of_get_nand_bus_width
=====================

.. c:function:: int of_get_nand_bus_width (struct device_node *np)

    Get nand bus witdh for given device_node

    :param struct device_node \*np:
        Pointer to the given device_node



.. _`of_get_nand_bus_width.description`:

Description
-----------

return bus width option, or errno in error case.



.. _`of_get_nand_on_flash_bbt`:

of_get_nand_on_flash_bbt
========================

.. c:function:: bool of_get_nand_on_flash_bbt (struct device_node *np)

    Get nand on flash bbt for given device_node

    :param struct device_node \*np:
        Pointer to the given device_node



.. _`of_get_nand_on_flash_bbt.description`:

Description
-----------

return true if present false other wise

