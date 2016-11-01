.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/phy-rockchip-inno-usb2.c

.. _`rockchip_usb2phy_port_cfg`:

struct rockchip_usb2phy_port_cfg
================================

.. c:type:: struct rockchip_usb2phy_port_cfg

    usb-phy port configuration.

.. _`rockchip_usb2phy_port_cfg.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_usb2phy_port_cfg {
        struct usb2phy_reg phy_sus;
        struct usb2phy_reg ls_det_en;
        struct usb2phy_reg ls_det_st;
        struct usb2phy_reg ls_det_clr;
        struct usb2phy_reg utmi_ls;
        struct usb2phy_reg utmi_hstdet;
    }

.. _`rockchip_usb2phy_port_cfg.members`:

Members
-------

phy_sus
    phy suspend register.

ls_det_en
    linestate detection enable register.

ls_det_st
    linestate detection state register.

ls_det_clr
    linestate detection clear register.

utmi_ls
    utmi linestate state register.

utmi_hstdet
    utmi host disconnect register.

.. _`rockchip_usb2phy_cfg`:

struct rockchip_usb2phy_cfg
===========================

.. c:type:: struct rockchip_usb2phy_cfg

    usb-phy configuration.

.. _`rockchip_usb2phy_cfg.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_usb2phy_cfg {
        unsigned int reg;
        unsigned int num_ports;
        struct usb2phy_reg clkout_ctl;
        const struct rockchip_usb2phy_port_cfg port_cfgs[USB2PHY_NUM_PORTS];
    }

.. _`rockchip_usb2phy_cfg.members`:

Members
-------

reg
    the address offset of grf for usb-phy config.

num_ports
    specify how many ports that the phy has.

clkout_ctl
    keep on/turn off output clk of phy.

.. _`rockchip_usb2phy_port`:

struct rockchip_usb2phy_port
============================

.. c:type:: struct rockchip_usb2phy_port

    usb-phy port data.

.. _`rockchip_usb2phy_port.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_usb2phy_port {
        struct phy *phy;
        unsigned int port_id;
        bool suspended;
        int ls_irq;
        struct mutex mutex;
        struct delayed_work sm_work;
        const struct rockchip_usb2phy_port_cfg *port_cfg;
    }

.. _`rockchip_usb2phy_port.members`:

Members
-------

phy
    *undescribed*

port_id
    flag for otg port or host port.

suspended
    phy suspended flag.

ls_irq
    IRQ number assigned for linestate detection.

mutex
    for register updating in sm_work.

sm_work
    OTG state machine work.

port_cfg
    *undescribed*

.. _`rockchip_usb2phy`:

struct rockchip_usb2phy
=======================

.. c:type:: struct rockchip_usb2phy

    usb2.0 phy driver data.

.. _`rockchip_usb2phy.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_usb2phy {
        struct device *dev;
        struct regmap *grf;
        struct clk *clk;
        struct clk *clk480m;
        struct clk_hw clk480m_hw;
        const struct rockchip_usb2phy_cfg *phy_cfg;
        struct rockchip_usb2phy_port ports[USB2PHY_NUM_PORTS];
    }

.. _`rockchip_usb2phy.members`:

Members
-------

dev
    *undescribed*

grf
    General Register Files regmap.

clk
    clock struct of phy input clk.

clk480m
    clock struct of phy output clk.

clk480m_hw
    *undescribed*

phy_cfg
    phy register configuration, assigned by driver data.

ports
    phy port instance.

.. This file was automatic generated / don't edit.

