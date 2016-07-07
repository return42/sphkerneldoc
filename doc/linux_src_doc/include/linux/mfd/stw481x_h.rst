.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/stw481x.h

.. _`stw481x`:

struct stw481x
==============

.. c:type:: struct stw481x

    state holder for the Stw481x drivers

.. _`stw481x.definition`:

Definition
----------

.. code-block:: c

    struct stw481x {
        struct i2c_client *client;
        struct regmap *map;
    }

.. _`stw481x.members`:

Members
-------

client
    *undescribed*

map
    regmap handle to access device registers

.. This file was automatic generated / don't edit.

