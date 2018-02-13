.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/smiapp/smiapp-quirk.h

.. _`smiapp_quirk`:

struct smiapp_quirk
===================

.. c:type:: struct smiapp_quirk

    quirks for sensors that deviate from SMIA++ standard

.. _`smiapp_quirk.definition`:

Definition
----------

.. code-block:: c

    struct smiapp_quirk {
        int (*limits)(struct smiapp_sensor *sensor);
        int (*post_poweron)(struct smiapp_sensor *sensor);
        int (*pre_streamon)(struct smiapp_sensor *sensor);
        int (*post_streamoff)(struct smiapp_sensor *sensor);
        unsigned long (*pll_flags)(struct smiapp_sensor *sensor);
        int (*init)(struct smiapp_sensor *sensor);
        int (*reg_access)(struct smiapp_sensor *sensor, bool write, u32 *reg, u32 *val);
        unsigned long flags;
    }

.. _`smiapp_quirk.members`:

Members
-------

limits
    Replace sensor->limits with values which can't be read from
    sensor registers. Called the first time the sensor is powered up.

post_poweron
    Called always after the sensor has been fully powered on.

pre_streamon
    Called just before streaming is enabled.

post_streamoff
    *undescribed*

pll_flags
    Return flags for the PLL calculator.

init
    Quirk initialisation, called the last in \ :c:func:`probe`\ . This is
    also appropriate for adding sensor specific controls, for instance.

reg_access
    Register access quirk. The quirk may divert the access
    to another register, or no register at all.

flags
    *undescribed*

.. _`smiapp_quirk.description`:

Description
-----------

\ ``write``\ : Is this read (false) or write (true) access?
\ ``reg``\ : Pointer to the register to access
\ ``value``\ : Register value, set by the caller on write, or
by the quirk on read

\ ``return``\ : 0 on success, -ENOIOCTLCMD if no register
access may be done by the caller (default read
value is zero), else negative error code on error

.. This file was automatic generated / don't edit.

