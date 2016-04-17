.. -*- coding: utf-8; mode: rst -*-

=============
gpio-ts5500.h
=============


.. _`ts5500_dio_platform_data`:

struct ts5500_dio_platform_data
===============================

.. c:type:: ts5500_dio_platform_data

    TS-5500 pin block configuration


.. _`ts5500_dio_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct ts5500_dio_platform_data {
    int base;
    bool strap;
  };


.. _`ts5500_dio_platform_data.members`:

Members
-------

:``base``:
    The GPIO base number to use.

:``strap``:
    The only pin connected to an interrupt in a block is input-only.
    If you need a bidirectional line which can trigger an IRQ, you
    may strap it with an in/out pin. This flag indicates this case.


