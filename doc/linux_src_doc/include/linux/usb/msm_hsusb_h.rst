.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/msm_hsusb.h

.. _`msm_otg_platform_data`:

struct msm_otg_platform_data
============================

.. c:type:: struct msm_otg_platform_data

    platform device data for msm_otg driver.

.. _`msm_otg_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct msm_otg_platform_data {
        int *phy_init_seq;
        int phy_init_sz;
        void (*vbus_power)(bool on);
        unsigned power_budget;
        enum usb_dr_mode mode;
        enum otg_control_type otg_control;
        enum msm_usb_phy_type phy_type;
        void (*setup_gpio)(enum usb_otg_state state);
    }

.. _`msm_otg_platform_data.members`:

Members
-------

phy_init_seq
    PHY configuration sequence values. Value of -1 is reserved as
    "do not overwrite default vaule at this address".

phy_init_sz
    PHY configuration sequence size.

vbus_power
    VBUS power on/off routine.

power_budget
    VBUS power budget in mA (0 will be treated as 500mA).

mode
    Supported mode (OTG/peripheral/host).

otg_control
    OTG switch controlled by user/Id pin

phy_type
    *undescribed*

setup_gpio
    *undescribed*

.. _`msm_usb_cable`:

struct msm_usb_cable
====================

.. c:type:: struct msm_usb_cable

    structure for exteternal connector cable state tracking

.. _`msm_usb_cable.definition`:

Definition
----------

.. code-block:: c

    struct msm_usb_cable {
        struct notifier_block nb;
        struct extcon_dev *extcon;
    }

.. _`msm_usb_cable.members`:

Members
-------

nb
    hold event notification callback

extcon
    *undescribed*

.. _`msm_otg`:

struct msm_otg
==============

.. c:type:: struct msm_otg

    OTG driver data. Shared by HCD and DCD.

.. _`msm_otg.definition`:

Definition
----------

.. code-block:: c

    struct msm_otg {
        struct usb_phy phy;
        struct msm_otg_platform_data *pdata;
        int irq;
        struct clk *clk;
        struct clk *pclk;
        struct clk *core_clk;
        void __iomem *regs;
        #define ID 0
        #define B_SESS_VLD 1
        unsigned long inputs;
        struct work_struct sm_work;
        atomic_t in_lpm;
        int async_int;
        unsigned cur_power;
        int phy_number;
        struct delayed_work chg_work;
        enum usb_chg_state chg_state;
        enum usb_chg_type chg_type;
        u8 dcd_retries;
        struct regulator *v3p3;
        struct regulator *v1p8;
        struct regulator *vddcx;
        struct reset_control *phy_rst;
        struct reset_control *link_rst;
        int vdd_levels[3];
        bool manual_pullup;
        struct msm_usb_cable vbus;
        struct msm_usb_cable id;
        struct gpio_desc *switch_gpio;
        struct notifier_block reboot;
    }

.. _`msm_otg.members`:

Members
-------

phy
    *undescribed*

pdata
    otg device platform data.

irq
    IRQ number assigned for HSUSB controller.

clk
    clock struct of usb_hs_clk.

pclk
    clock struct of usb_hs_pclk.

core_clk
    clock struct of usb_hs_core_clk.

regs
    ioremapped register base address.

inputs
    OTG state machine inputs(Id, SessValid etc).

sm_work
    OTG state machine work.

in_lpm
    indicates low power mode (LPM) state.

async_int
    Async interrupt arrived.

cur_power
    The amount of mA available from downstream port.

phy_number
    *undescribed*

chg_work
    Charger detection work.

chg_state
    The state of charger detection process.

chg_type
    The type of charger attached.

dcd_retries
    *undescribed*

v3p3
    *undescribed*

v1p8
    *undescribed*

vddcx
    *undescribed*

phy_rst
    *undescribed*

link_rst
    *undescribed*

manual_pullup
    true if VBUS is not routed to USB controller/phy
    and controller driver therefore enables pull-up explicitly before
    starting controller using usbcmd run/stop bit.

vbus
    VBUS signal state trakining, using extcon framework

id
    ID signal state trakining, using extcon framework

switch_gpio
    Descriptor for GPIO used to control external Dual
    SPDT USB Switch.

reboot
    Used to inform the driver to route USB D+/D- line to Device
    connector

.. This file was automatic generated / don't edit.

