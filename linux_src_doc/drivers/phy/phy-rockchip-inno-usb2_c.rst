.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/phy-rockchip-inno-usb2.c

.. _`rockchip_chg_det_reg`:

struct rockchip_chg_det_reg
===========================

.. c:type:: struct rockchip_chg_det_reg

    usb charger detect registers

.. _`rockchip_chg_det_reg.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_chg_det_reg {
        struct usb2phy_reg cp_det;
        struct usb2phy_reg dcp_det;
        struct usb2phy_reg dp_det;
        struct usb2phy_reg idm_sink_en;
        struct usb2phy_reg idp_sink_en;
        struct usb2phy_reg idp_src_en;
        struct usb2phy_reg rdm_pdwn_en;
        struct usb2phy_reg vdm_src_en;
        struct usb2phy_reg vdp_src_en;
        struct usb2phy_reg opmode;
    }

.. _`rockchip_chg_det_reg.members`:

Members
-------

cp_det
    charging port detected successfully.

dcp_det
    dedicated charging port detected successfully.

dp_det
    assert data pin connect successfully.

idm_sink_en
    open dm sink curren.

idp_sink_en
    open dp sink current.

idp_src_en
    open dm source current.

rdm_pdwn_en
    open dm pull down resistor.

vdm_src_en
    open dm voltage source.

vdp_src_en
    open dp voltage source.

opmode
    utmi operational mode.

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
        struct usb2phy_reg bvalid_det_en;
        struct usb2phy_reg bvalid_det_st;
        struct usb2phy_reg bvalid_det_clr;
        struct usb2phy_reg ls_det_en;
        struct usb2phy_reg ls_det_st;
        struct usb2phy_reg ls_det_clr;
        struct usb2phy_reg utmi_avalid;
        struct usb2phy_reg utmi_bvalid;
        struct usb2phy_reg utmi_ls;
        struct usb2phy_reg utmi_hstdet;
    }

.. _`rockchip_usb2phy_port_cfg.members`:

Members
-------

phy_sus
    phy suspend register.

bvalid_det_en
    vbus valid rise detection enable register.

bvalid_det_st
    vbus valid rise detection status register.

bvalid_det_clr
    vbus valid rise detection clear register.

ls_det_en
    linestate detection enable register.

ls_det_st
    linestate detection state register.

ls_det_clr
    linestate detection clear register.

utmi_avalid
    utmi vbus avalid status register.

utmi_bvalid
    utmi vbus bvalid status register.

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
        const struct rockchip_chg_det_reg chg_det;
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

chg_det
    charger detection registers.

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
        bool utmi_avalid;
        bool vbus_attached;
        int bvalid_irq;
        int ls_irq;
        struct mutex mutex;
        struct delayed_work chg_work;
        struct delayed_work otg_sm_work;
        struct delayed_work sm_work;
        const struct rockchip_usb2phy_port_cfg *port_cfg;
        struct notifier_block event_nb;
        enum usb_otg_state state;
        enum usb_dr_mode mode;
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

utmi_avalid
    utmi avalid status usage flag.
    true    - use avalid to get vbus status
    flase   - use bvalid to get vbus status

vbus_attached
    otg device vbus status.

bvalid_irq
    IRQ number assigned for vbus valid rise detection.

ls_irq
    IRQ number assigned for linestate detection.

mutex
    for register updating in sm_work.

chg_work
    charge detect work.

otg_sm_work
    OTG state machine work.

sm_work
    HOST state machine work.

port_cfg
    *undescribed*

event_nb
    hold event notification callback.

state
    define OTG enumeration states before device reset.

mode
    the dr_mode of the controller.

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
        enum usb_chg_state chg_state;
        enum power_supply_type chg_type;
        u8 dcd_retries;
        struct extcon_dev *edev;
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

chg_state
    states involved in USB charger detection.

chg_type
    USB charger types.

dcd_retries
    The retry count used to track Data contact
    detection process.

edev
    extcon device for notification registration

phy_cfg
    phy register configuration, assigned by driver data.

ports
    phy port instance.

.. This file was automatic generated / don't edit.

