.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-mlxreg.c

.. _`mlxreg_led_data`:

struct mlxreg_led_data
======================

.. c:type:: struct mlxreg_led_data

    led control data:

.. _`mlxreg_led_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_led_data {
        struct mlxreg_core_data *data;
        struct led_classdev led_cdev;
        u8 base_color;
        void *data_parent;
        char led_cdev_name[MLXREG_CORE_LABEL_MAX_SIZE];
    }

.. _`mlxreg_led_data.members`:

Members
-------

data
    led configuration data;

led_cdev
    *undescribed*

base_color
    base led color (other colors have constant offset from base);

data_parent
    pointer to private device control data of parent;

led_cdev_name
    *undescribed*

.. _`mlxreg_led_priv_data`:

struct mlxreg_led_priv_data
===========================

.. c:type:: struct mlxreg_led_priv_data

    platform private data:

.. _`mlxreg_led_priv_data.definition`:

Definition
----------

.. code-block:: c

    struct mlxreg_led_priv_data {
        struct platform_device *pdev;
        struct mlxreg_core_platform_data *pdata;
        struct mutex access_lock;
    }

.. _`mlxreg_led_priv_data.members`:

Members
-------

pdev
    platform device;

pdata
    platform data;

access_lock
    mutex for attribute IO access;

.. This file was automatic generated / don't edit.

