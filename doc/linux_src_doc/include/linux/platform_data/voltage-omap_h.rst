.. -*- coding: utf-8; mode: rst -*-

==============
voltage-omap.h
==============


.. _`omap_volt_data`:

struct omap_volt_data
=====================

.. c:type:: omap_volt_data

    Omap voltage specific data.


.. _`omap_volt_data.definition`:

Definition
----------

.. code-block:: c

  struct omap_volt_data {
    u32 sr_efuse_offs;
    u8 sr_errminlimit;
  };


.. _`omap_volt_data.members`:

Members
-------

:``sr_efuse_offs``:
    The offset of the efuse register(from system
    control module base address) from where to read
    the n-target value for the smartreflex module.

:``sr_errminlimit``:
    Error min limit value for smartreflex. This value
    differs at differnet opp and thus is linked
    with voltage.


