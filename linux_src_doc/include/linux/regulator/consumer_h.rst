.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regulator/consumer.h

.. _`pre_voltage_change_data`:

struct pre_voltage_change_data
==============================

.. c:type:: struct pre_voltage_change_data

    Data sent with PRE_VOLTAGE_CHANGE event

.. _`pre_voltage_change_data.definition`:

Definition
----------

.. code-block:: c

    struct pre_voltage_change_data {
        unsigned long old_uV;
        unsigned long min_uV;
        unsigned long max_uV;
    }

.. _`pre_voltage_change_data.members`:

Members
-------

old_uV
    Current voltage before change.

min_uV
    Min voltage we'll change to.

max_uV
    Max voltage we'll change to.

.. _`regulator_bulk_data`:

struct regulator_bulk_data
==========================

.. c:type:: struct regulator_bulk_data

    Data used for bulk regulator operations.

.. _`regulator_bulk_data.definition`:

Definition
----------

.. code-block:: c

    struct regulator_bulk_data {
        const char *supply;
        struct regulator *consumer;
    }

.. _`regulator_bulk_data.members`:

Members
-------

supply
    The name of the supply.  Initialised by the user before
    using the bulk regulator APIs.

consumer
    The regulator consumer for the supply.  This will be managed
    by the bulk API.

.. _`regulator_bulk_data.description`:

Description
-----------

The regulator APIs provide a series of \ :c:func:`regulator_bulk_`\  API calls as
a convenience to consumers which require multiple supplies.  This
structure is used to manage data for these calls.

.. This file was automatic generated / don't edit.

