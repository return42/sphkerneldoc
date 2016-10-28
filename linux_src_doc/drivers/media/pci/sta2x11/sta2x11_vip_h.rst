.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/pci/sta2x11/sta2x11_vip.h

.. _`vip_config`:

struct vip_config
=================

.. c:type:: struct vip_config

    video input configuration data

.. _`vip_config.definition`:

Definition
----------

.. code-block:: c

    struct vip_config {
        const char *pwr_name;
        int pwr_pin;
        const char *reset_name;
        int reset_pin;
        int i2c_id;
        int i2c_addr;
    }

.. _`vip_config.members`:

Members
-------

pwr_name
    ADV powerdown name

pwr_pin
    ADV powerdown pin

reset_name
    ADV reset name

reset_pin
    ADV reset pin

i2c_id
    *undescribed*

i2c_addr
    *undescribed*

.. This file was automatic generated / don't edit.

