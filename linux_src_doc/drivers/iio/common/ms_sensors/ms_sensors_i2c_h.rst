.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/ms_sensors/ms_sensors_i2c.h

.. _`ms_ht_dev`:

struct ms_ht_dev
================

.. c:type:: struct ms_ht_dev

    Humidity/Temperature sensor device structure

.. _`ms_ht_dev.definition`:

Definition
----------

.. code-block:: c

    struct ms_ht_dev {
        struct i2c_client *client;
        struct mutex lock;
        u8 res_index;
    }

.. _`ms_ht_dev.members`:

Members
-------

client
    i2c client

lock
    lock protecting the i2c conversion

res_index
    index to selected sensor resolution

.. _`ms_tp_dev`:

struct ms_tp_dev
================

.. c:type:: struct ms_tp_dev

    Temperature/Pressure sensor device structure

.. _`ms_tp_dev.definition`:

Definition
----------

.. code-block:: c

    struct ms_tp_dev {
        struct i2c_client *client;
        struct mutex lock;
        u16 prom[MS_SENSORS_TP_PROM_WORDS_NB + 1];
        u8 res_index;
    }

.. _`ms_tp_dev.members`:

Members
-------

client
    i2c client

lock
    lock protecting the i2c conversion

prom
    array of PROM coefficients used for conversion. Added element
    for CRC computation

res_index
    index to selected sensor resolution

.. This file was automatic generated / don't edit.

