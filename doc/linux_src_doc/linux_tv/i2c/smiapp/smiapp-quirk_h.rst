.. -*- coding: utf-8; mode: rst -*-

==============
smiapp-quirk.h
==============



.. _xref_struct_smiapp_quirk:

struct smiapp_quirk
===================

.. c:type:: struct smiapp_quirk

    quirks for sensors that deviate from SMIA++ standard



Definition
----------

.. code-block:: c

  struct smiapp_quirk {
    int (* limits) (struct smiapp_sensor *sensor);
    int (* post_poweron) (struct smiapp_sensor *sensor);
    int (* pre_streamon) (struct smiapp_sensor *sensor);
    unsigned long (* pll_flags) (struct smiapp_sensor *sensor);
    int (* init) (struct smiapp_sensor *sensor);
    int (* reg_access) (struct smiapp_sensor *sensor, bool write, u32 *reg,u32 *val);
  };



Members
-------

:``int (*)(struct smiapp_sensor *sensor) limits``:
    Replace sensor->limits with values which can't be read from
    	    sensor registers. Called the first time the sensor is powered up.

:``int (*)(struct smiapp_sensor *sensor) post_poweron``:
    Called always after the sensor has been fully powered on.

:``int (*)(struct smiapp_sensor *sensor) pre_streamon``:
    Called just before streaming is enabled.

:``unsigned long (*)(struct smiapp_sensor *sensor) pll_flags``:
    Return flags for the PLL calculator.

:``int (*)(struct smiapp_sensor *sensor) init``:
    Quirk initialisation, called the last in :c:func:`probe`. This is
    	  also appropriate for adding sensor specific controls, for instance.

:``int (*)(struct smiapp_sensor *sensor, bool write, u32 *reg,u32 *val) reg_access``:
    Register access quirk. The quirk may divert the access
    		to another register, or no register at all.



