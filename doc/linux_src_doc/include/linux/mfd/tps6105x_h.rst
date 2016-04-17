.. -*- coding: utf-8; mode: rst -*-

==========
tps6105x.h
==========


.. _`tps6105x_mode`:

enum tps6105x_mode
==================

.. c:type:: tps6105x_mode

    desired mode for the TPS6105x


.. _`tps6105x_mode.definition`:

Definition
----------

.. code-block:: c

    enum tps6105x_mode {
      TPS6105X_MODE_SHUTDOWN,
      TPS6105X_MODE_TORCH,
      TPS6105X_MODE_TORCH_FLASH,
      TPS6105X_MODE_VOLTAGE
    };


.. _`tps6105x_mode.constants`:

Constants
---------

:``TPS6105X_MODE_SHUTDOWN``:
    this instance is inactive, not used for anything

:``TPS6105X_MODE_TORCH``:
-- undescribed --

:``TPS6105X_MODE_TORCH_FLASH``:
    this instance is used as a flashgun, usually
    in a camera

:``TPS6105X_MODE_VOLTAGE``:
    this instance is used as a voltage regulator and
    will register to the regulator framework


.. _`tps6105x_platform_data`:

struct tps6105x_platform_data
=============================

.. c:type:: tps6105x_platform_data

    TPS61905x platform data


.. _`tps6105x_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct tps6105x_platform_data {
    enum tps6105x_mode mode;
    struct regulator_init_data * regulator_data;
  };


.. _`tps6105x_platform_data.members`:

Members
-------

:``mode``:
    what mode this instance shall be operated in,
    this is not selectable at runtime

:``regulator_data``:
    initialization data for the voltage
    regulator if used as a voltage source




.. _`tps6105x`:

struct tps6105x
===============

.. c:type:: tps6105x

    state holder for the TPS6105x drivers


.. _`tps6105x.definition`:

Definition
----------

.. code-block:: c

  struct tps6105x {
    struct regulator_dev * regulator;
    struct regmap * regmap;
  };


.. _`tps6105x.members`:

Members
-------

:``regulator``:
    regulator device if used in voltage mode

:``regmap``:
    used for i2c communcation on accessing registers


