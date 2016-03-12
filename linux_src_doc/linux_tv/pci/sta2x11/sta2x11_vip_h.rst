.. -*- coding: utf-8; mode: rst -*-

=============
sta2x11_vip.h
=============



.. _xref_struct_vip_config:

struct vip_config
=================

.. c:type:: struct vip_config

    video input configuration data



Definition
----------

.. code-block:: c

  struct vip_config {
    const char * pwr_name;
    int pwr_pin;
    const char * reset_name;
    int reset_pin;
  };



Members
-------

:``const char * pwr_name``:
    ADV powerdown name

:``int pwr_pin``:
    ADV powerdown pin

:``const char * reset_name``:
    ADV reset name

:``int reset_pin``:
    ADV reset pin



