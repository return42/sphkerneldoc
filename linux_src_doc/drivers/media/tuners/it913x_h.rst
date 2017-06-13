.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/tuners/it913x.h

.. _`it913x_platform_data`:

struct it913x_platform_data
===========================

.. c:type:: struct it913x_platform_data

    Platform data for the it913x driver

.. _`it913x_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct it913x_platform_data {
        struct regmap *regmap;
        struct dvb_frontend *fe;
    #define IT913X_ROLE_SINGLE 0
    #define IT913X_ROLE_DUAL_MASTER 1
    #define IT913X_ROLE_DUAL_SLAVE 2
        unsigned int role:2;
    }

.. _`it913x_platform_data.members`:

Members
-------

regmap
    af9033 demod driver regmap.

fe
    *undescribed*

role
    Chip role, single or dual configuration.

.. This file was automatic generated / don't edit.

