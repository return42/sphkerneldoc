.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/ti-aemif.h

.. _`aemif_abus_data`:

struct aemif_abus_data
======================

.. c:type:: struct aemif_abus_data

    Async bus configuration parameters.

.. _`aemif_abus_data.definition`:

Definition
----------

.. code-block:: c

    struct aemif_abus_data {
        u32 cs;
    }

.. _`aemif_abus_data.members`:

Members
-------

cs
    *undescribed*

.. _`aemif_abus_data.description`:

Description
-----------

\ ``cs``\  - Chip-select number.

.. _`aemif_platform_data`:

struct aemif_platform_data
==========================

.. c:type:: struct aemif_platform_data

    Data to set up the TI aemif driver.

.. _`aemif_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct aemif_platform_data {
        struct of_dev_auxdata *dev_lookup;
        u32 cs_offset;
        struct aemif_abus_data *abus_data;
        size_t num_abus_data;
        struct platform_device *sub_devices;
        size_t num_sub_devices;
    }

.. _`aemif_platform_data.members`:

Members
-------

dev_lookup
    of_dev_auxdata passed to \ :c:func:`of_platform_populate`\  for aemif
    subdevices.

cs_offset
    Lowest allowed chip-select number.

abus_data
    Array of async bus configuration entries.

num_abus_data
    Number of abus entries.

sub_devices
    Array of platform subdevices.

num_sub_devices
    Number of subdevices.

.. This file was automatic generated / don't edit.

