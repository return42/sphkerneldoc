.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/dsa/vitesse-vsc73xx.c

.. _`vsc73xx`:

struct vsc73xx
==============

.. c:type:: struct vsc73xx

    VSC73xx state container

.. _`vsc73xx.definition`:

Definition
----------

.. code-block:: c

    struct vsc73xx {
        struct device *dev;
        struct gpio_desc *reset;
        struct spi_device *spi;
        struct dsa_switch *ds;
        struct gpio_chip gc;
        u16 chipid;
        u8 addr[ETH_ALEN];
        struct mutex lock;
    }

.. _`vsc73xx.members`:

Members
-------

dev
    *undescribed*

reset
    *undescribed*

spi
    *undescribed*

ds
    *undescribed*

gc
    *undescribed*

chipid
    *undescribed*

addr
    *undescribed*

lock
    *undescribed*

.. This file was automatic generated / don't edit.

