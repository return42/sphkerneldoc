.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/accel/kxsd9.c

.. _`kxsd9_state`:

struct kxsd9_state
==================

.. c:type:: struct kxsd9_state

    device related storage

.. _`kxsd9_state.definition`:

Definition
----------

.. code-block:: c

    struct kxsd9_state {
        struct device *dev;
        struct regmap *map;
        struct iio_mount_matrix orientation;
        struct regulator_bulk_data regs[2];
        u8 scale;
    }

.. _`kxsd9_state.members`:

Members
-------

dev
    pointer to the parent device

map
    regmap to the device

orientation
    mounting matrix, flipped axis etc

regs
    regulators for this device, VDD and IOVDD

scale
    the current scaling setting

.. This file was automatic generated / don't edit.

