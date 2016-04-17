.. -*- coding: utf-8; mode: rst -*-

==========
adau1977.h
==========


.. _`adau1977_micbias`:

enum adau1977_micbias
=====================

.. c:type:: adau1977_micbias

    ADAU1977 MICBIAS pin voltage setting


.. _`adau1977_micbias.definition`:

Definition
----------

.. code-block:: c

    enum adau1977_micbias {
      ADAU1977_MICBIAS_5V0,
      ADAU1977_MICBIAS_5V5,
      ADAU1977_MICBIAS_6V0,
      ADAU1977_MICBIAS_6V5,
      ADAU1977_MICBIAS_7V0,
      ADAU1977_MICBIAS_7V5,
      ADAU1977_MICBIAS_8V0,
      ADAU1977_MICBIAS_8V5,
      ADAU1977_MICBIAS_9V0
    };


.. _`adau1977_micbias.constants`:

Constants
---------

:``ADAU1977_MICBIAS_5V0``:
    MICBIAS is set to 5.0 V

:``ADAU1977_MICBIAS_5V5``:
    MICBIAS is set to 5.5 V

:``ADAU1977_MICBIAS_6V0``:
    MICBIAS is set to 6.0 V

:``ADAU1977_MICBIAS_6V5``:
    MICBIAS is set to 6.5 V

:``ADAU1977_MICBIAS_7V0``:
    MICBIAS is set to 7.0 V

:``ADAU1977_MICBIAS_7V5``:
    MICBIAS is set to 7.5 V

:``ADAU1977_MICBIAS_8V0``:
    MICBIAS is set to 8.0 V

:``ADAU1977_MICBIAS_8V5``:
    MICBIAS is set to 8.5 V

:``ADAU1977_MICBIAS_9V0``:
    MICBIAS is set to 9.0 V


.. _`adau1977_platform_data`:

struct adau1977_platform_data
=============================

.. c:type:: adau1977_platform_data

    Platform configuration data for the ADAU1977


.. _`adau1977_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct adau1977_platform_data {
    enum adau1977_micbias micbias;
  };


.. _`adau1977_platform_data.members`:

Members
-------

:``micbias``:
    Specifies the voltage for the MICBIAS pin


