.. -*- coding: utf-8; mode: rst -*-

==========
apds990x.h
==========


.. _`apds990x_platform_data`:

struct apds990x_platform_data
=============================

.. c:type:: apds990x_platform_data

    platform data for apsd990x.c driver


.. _`apds990x_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct apds990x_platform_data {
    struct apds990x_chip_factors cf;
    u8 ppcount;
    int (* setup_resources) (void);
    int (* release_resources) (void);
  };


.. _`apds990x_platform_data.members`:

Members
-------

:``cf``:
    chip factor data

:``ppcount``:
    number of IR pulses used for proximity estimation

:``setup_resources``:
    interrupt line setup call back function

:``release_resources``:
    interrupt line release call back function




.. _`apds990x_platform_data.description`:

Description
-----------

Proximity detection result depends heavily on correct ppcount, pdrive
and cover window.

