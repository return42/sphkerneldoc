.. -*- coding: utf-8; mode: rst -*-

=========
adf_cfg.c
=========


.. _`adf_cfg_dev_add`:

adf_cfg_dev_add
===============

.. c:function:: int adf_cfg_dev_add (struct adf_accel_dev *accel_dev)

    Create an acceleration device configuration table.

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.



.. _`adf_cfg_dev_add.description`:

Description
-----------

Function creates a configuration table for the given acceleration device.
The table stores device specific config values.
To be used by QAT device specific drivers.



.. _`adf_cfg_dev_add.return`:

Return
------

0 on success, error code otherwise.



.. _`adf_cfg_dev_remove`:

adf_cfg_dev_remove
==================

.. c:function:: void adf_cfg_dev_remove (struct adf_accel_dev *accel_dev)

    Clears acceleration device configuration table.

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.



.. _`adf_cfg_dev_remove.description`:

Description
-----------

Function removes configuration table from the given acceleration device
and frees all allocated memory.
To be used by QAT device specific drivers.



.. _`adf_cfg_dev_remove.return`:

Return
------

void



.. _`adf_cfg_add_key_value_param`:

adf_cfg_add_key_value_param
===========================

.. c:function:: int adf_cfg_add_key_value_param (struct adf_accel_dev *accel_dev, const char *section_name, const char *key, const void *val, enum adf_cfg_val_type type)

    Add key-value config entry to config table.

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

    :param const char \*section_name:
        Name of the section where the param will be added

    :param const char \*key:
        The key string

    :param const void \*val:
        Value pain for the given ``key``

    :param enum adf_cfg_val_type type:
        Type - string, int or address



.. _`adf_cfg_add_key_value_param.description`:

Description
-----------

Function adds configuration key - value entry in the appropriate section
in the given acceleration device
To be used by QAT device specific drivers.



.. _`adf_cfg_add_key_value_param.return`:

Return
------

0 on success, error code otherwise.



.. _`adf_cfg_section_add`:

adf_cfg_section_add
===================

.. c:function:: int adf_cfg_section_add (struct adf_accel_dev *accel_dev, const char *name)

    Add config section entry to config table.

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

    :param const char \*name:
        Name of the section



.. _`adf_cfg_section_add.description`:

Description
-----------

Function adds configuration section where key - value entries
will be stored.
To be used by QAT device specific drivers.



.. _`adf_cfg_section_add.return`:

Return
------

0 on success, error code otherwise.

