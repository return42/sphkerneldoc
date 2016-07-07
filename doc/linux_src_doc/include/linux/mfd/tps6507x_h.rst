.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/tps6507x.h

.. _`tps6507x_board`:

struct tps6507x_board
=====================

.. c:type:: struct tps6507x_board

    packages regulator and touchscreen init data

.. _`tps6507x_board.definition`:

Definition
----------

.. code-block:: c

    struct tps6507x_board {
        struct regulator_init_data *tps6507x_pmic_init_data;
        struct touchscreen_init_data *tps6507x_ts_init_data;
    }

.. _`tps6507x_board.members`:

Members
-------

tps6507x_pmic_init_data
    *undescribed*

tps6507x_ts_init_data
    *undescribed*

.. _`tps6507x_board.description`:

Description
-----------

Board data may be used to initialize regulator and touchscreen.

.. _`tps6507x_dev`:

struct tps6507x_dev
===================

.. c:type:: struct tps6507x_dev

    tps6507x sub-driver chip access routines @\ :c:func:`read_dev`\  - I2C register read function @\ :c:func:`write_dev`\  - I2C register write function

.. _`tps6507x_dev.definition`:

Definition
----------

.. code-block:: c

    struct tps6507x_dev {
        struct device *dev;
        struct i2c_client *i2c_client;
        int (* read_dev) (struct tps6507x_dev *tps6507x, char reg, int size,void *dest);
        int (* write_dev) (struct tps6507x_dev *tps6507x, char reg, int size,void *src);
        struct tps6507x_pmic *pmic;
    }

.. _`tps6507x_dev.members`:

Members
-------

dev
    *undescribed*

i2c_client
    *undescribed*

read_dev
    *undescribed*

write_dev
    *undescribed*

pmic
    *undescribed*

.. _`tps6507x_dev.description`:

Description
-----------

Device data may be used to access the TPS6507x chip

.. This file was automatic generated / don't edit.

