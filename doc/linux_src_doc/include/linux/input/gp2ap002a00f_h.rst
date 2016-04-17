.. -*- coding: utf-8; mode: rst -*-

==============
gp2ap002a00f.h
==============


.. _`gp2a_platform_data`:

struct gp2a_platform_data
=========================

.. c:type:: gp2a_platform_data

    Sharp gp2ap002a00f proximity platform data


.. _`gp2a_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct gp2a_platform_data {
    int vout_gpio;
    bool wakeup;
    int (* hw_setup) (struct i2c_client *client);
    int (* hw_shutdown) (struct i2c_client *client);
  };


.. _`gp2a_platform_data.members`:

Members
-------

:``vout_gpio``:
    The gpio connected to the object detected pin (VOUT)

:``wakeup``:
    Set to true if the proximity can wake the device from suspend

:``hw_setup``:
    Callback for setting up hardware such as gpios and vregs

:``hw_shutdown``:
    Callback for properly shutting down hardware


