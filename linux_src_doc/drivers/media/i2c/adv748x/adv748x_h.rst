.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/adv748x/adv748x.h

.. _`adv748x_ports`:

enum adv748x_ports
==================

.. c:type:: enum adv748x_ports

    Device tree port number definitions

.. _`adv748x_ports.definition`:

Definition
----------

.. code-block:: c

    enum adv748x_ports {
        ADV748X_PORT_AIN0,
        ADV748X_PORT_AIN1,
        ADV748X_PORT_AIN2,
        ADV748X_PORT_AIN3,
        ADV748X_PORT_AIN4,
        ADV748X_PORT_AIN5,
        ADV748X_PORT_AIN6,
        ADV748X_PORT_AIN7,
        ADV748X_PORT_HDMI,
        ADV748X_PORT_TTL,
        ADV748X_PORT_TXA,
        ADV748X_PORT_TXB,
        ADV748X_PORT_MAX
    };

.. _`adv748x_ports.constants`:

Constants
---------

ADV748X_PORT_AIN0
    *undescribed*

ADV748X_PORT_AIN1
    *undescribed*

ADV748X_PORT_AIN2
    *undescribed*

ADV748X_PORT_AIN3
    *undescribed*

ADV748X_PORT_AIN4
    *undescribed*

ADV748X_PORT_AIN5
    *undescribed*

ADV748X_PORT_AIN6
    *undescribed*

ADV748X_PORT_AIN7
    *undescribed*

ADV748X_PORT_HDMI
    *undescribed*

ADV748X_PORT_TTL
    *undescribed*

ADV748X_PORT_TXA
    *undescribed*

ADV748X_PORT_TXB
    *undescribed*

ADV748X_PORT_MAX
    *undescribed*

.. _`adv748x_ports.description`:

Description
-----------

The ADV748X ports define the mapping between subdevices
and the device tree specification

.. _`adv748x_state`:

struct adv748x_state
====================

.. c:type:: struct adv748x_state

    State of ADV748X

.. _`adv748x_state.definition`:

Definition
----------

.. code-block:: c

    struct adv748x_state {
        struct device *dev;
        struct i2c_client *client;
        struct mutex mutex;
        struct device_node *endpoints[ADV748X_PORT_MAX];
        struct i2c_client *i2c_clients[ADV748X_PAGE_MAX];
        struct regmap *regmap[ADV748X_PAGE_MAX];
        struct adv748x_hdmi hdmi;
        struct adv748x_afe afe;
        struct adv748x_csi2 txa;
        struct adv748x_csi2 txb;
    }

.. _`adv748x_state.members`:

Members
-------

dev
    (OF) device

client
    I2C client

mutex
    protect global state

endpoints
    parsed device node endpoints for each port

i2c_clients
    *undescribed*

regmap
    *undescribed*

hdmi
    state of HDMI receiver context

afe
    state of AFE receiver context

txa
    state of TXA transmitter context

txb
    state of TXB transmitter context

.. _`adv748x_state.description`:

Description
-----------

@i2c_addresses       I2C Page addresses
\ ``i2c_clients``\          I2C clients for the page accesses
\ ``regmap``\               regmap configuration pages.

.. This file was automatic generated / don't edit.

