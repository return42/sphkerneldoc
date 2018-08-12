.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/rockchip/phy-rockchip-typec.c

.. _`rockchip_usb3phy_port_cfg`:

struct rockchip_usb3phy_port_cfg
================================

.. c:type:: struct rockchip_usb3phy_port_cfg

    usb3-phy port configuration.

.. _`rockchip_usb3phy_port_cfg.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_usb3phy_port_cfg {
        unsigned int reg;
        struct usb3phy_reg typec_conn_dir;
        struct usb3phy_reg usb3tousb2_en;
        struct usb3phy_reg external_psm;
        struct usb3phy_reg pipe_status;
        struct usb3phy_reg usb3_host_disable;
        struct usb3phy_reg usb3_host_port;
        struct usb3phy_reg uphy_dp_sel;
    }

.. _`rockchip_usb3phy_port_cfg.members`:

Members
-------

reg
    the base address for usb3-phy config.

typec_conn_dir
    the register of type-c connector direction.

usb3tousb2_en
    the register of type-c force usb2 to usb2 enable.

external_psm
    the register of type-c phy external psm clock.

pipe_status
    the register of type-c phy pipe status.

usb3_host_disable
    the register of type-c usb3 host disable.

usb3_host_port
    the register of type-c usb3 host port.

uphy_dp_sel
    the register of type-c phy DP select control.

.. This file was automatic generated / don't edit.

