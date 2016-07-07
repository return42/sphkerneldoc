.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/pixcir_i2c_ts.h

.. _`pixcir_i2c_chip_data`:

struct pixcir_i2c_chip_data
===========================

.. c:type:: struct pixcir_i2c_chip_data

    chip related data

.. _`pixcir_i2c_chip_data.definition`:

Definition
----------

.. code-block:: c

    struct pixcir_i2c_chip_data {
        u8 max_fingers;
        bool has_hw_ids;
    }

.. _`pixcir_i2c_chip_data.members`:

Members
-------

max_fingers
    Max number of fingers reported simultaneously by h/w

has_hw_ids
    Hardware supports finger tracking IDs

.. This file was automatic generated / don't edit.

