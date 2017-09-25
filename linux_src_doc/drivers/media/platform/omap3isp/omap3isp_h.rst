.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/omap3isp/omap3isp.h

.. _`isp_parallel_cfg`:

struct isp_parallel_cfg
=======================

.. c:type:: struct isp_parallel_cfg

    Parallel interface configuration

.. _`isp_parallel_cfg.definition`:

Definition
----------

.. code-block:: c

    struct isp_parallel_cfg {
        unsigned int data_lane_shift:3;
        unsigned int clk_pol:1;
        unsigned int hs_pol:1;
        unsigned int vs_pol:1;
        unsigned int fld_pol:1;
        unsigned int data_pol:1;
        unsigned int bt656:1;
    }

.. _`isp_parallel_cfg.members`:

Members
-------

data_lane_shift
    Data lane shifter
    0 - CAMEXT[13:0] -> CAM[13:0]
    2 - CAMEXT[13:2] -> CAM[11:0]
    4 - CAMEXT[13:4] -> CAM[9:0]
    6 - CAMEXT[13:6] -> CAM[7:0]

clk_pol
    Pixel clock polarity
    0 - Sample on rising edge, 1 - Sample on falling edge

hs_pol
    Horizontal synchronization polarity
    0 - Active high, 1 - Active low

vs_pol
    Vertical synchronization polarity
    0 - Active high, 1 - Active low

fld_pol
    Field signal polarity
    0 - Positive, 1 - Negative

data_pol
    Data polarity
    0 - Normal, 1 - One's complement

bt656
    Data contain BT.656 embedded synchronization

.. _`isp_csiphy_lane`:

struct isp_csiphy_lane
======================

.. c:type:: struct isp_csiphy_lane

    CCP2/CSI2 lane position and polarity

.. _`isp_csiphy_lane.definition`:

Definition
----------

.. code-block:: c

    struct isp_csiphy_lane {
        u8 pos;
        u8 pol;
    }

.. _`isp_csiphy_lane.members`:

Members
-------

pos
    position of the lane

pol
    polarity of the lane

.. _`isp_csiphy_lanes_cfg`:

struct isp_csiphy_lanes_cfg
===========================

.. c:type:: struct isp_csiphy_lanes_cfg

    CCP2/CSI2 lane configuration

.. _`isp_csiphy_lanes_cfg.definition`:

Definition
----------

.. code-block:: c

    struct isp_csiphy_lanes_cfg {
        struct isp_csiphy_lane data[ISP_CSIPHY2_NUM_DATA_LANES];
        struct isp_csiphy_lane clk;
    }

.. _`isp_csiphy_lanes_cfg.members`:

Members
-------

data
    Configuration of one or two data lanes

clk
    Clock lane configuration

.. _`isp_ccp2_cfg`:

struct isp_ccp2_cfg
===================

.. c:type:: struct isp_ccp2_cfg

    CCP2 interface configuration

.. _`isp_ccp2_cfg.definition`:

Definition
----------

.. code-block:: c

    struct isp_ccp2_cfg {
        unsigned int strobe_clk_pol:1;
        unsigned int crc:1;
        unsigned int ccp2_mode:1;
        unsigned int phy_layer:1;
        unsigned int vpclk_div:2;
        unsigned int vp_clk_pol:1;
        struct isp_csiphy_lanes_cfg lanecfg;
    }

.. _`isp_ccp2_cfg.members`:

Members
-------

strobe_clk_pol
    Strobe/clock polarity
    0 - Non Inverted, 1 - Inverted

crc
    Enable the cyclic redundancy check

ccp2_mode
    Enable CCP2 compatibility mode
    ISP_CCP2_MODE_MIPI - MIPI-CSI1 mode
    ISP_CCP2_MODE_CCP2 - CCP2 mode

phy_layer
    Physical layer selection
    ISP_CCP2_PHY_DATA_CLOCK - Data/clock physical layer
    ISP_CCP2_PHY_DATA_STROBE - Data/strobe physical layer

vpclk_div
    Video port output clock control

vp_clk_pol
    *undescribed*

lanecfg
    *undescribed*

.. _`isp_csi2_cfg`:

struct isp_csi2_cfg
===================

.. c:type:: struct isp_csi2_cfg

    CSI2 interface configuration

.. _`isp_csi2_cfg.definition`:

Definition
----------

.. code-block:: c

    struct isp_csi2_cfg {
        unsigned crc:1;
        struct isp_csiphy_lanes_cfg lanecfg;
        u8 num_data_lanes;
    }

.. _`isp_csi2_cfg.members`:

Members
-------

crc
    Enable the cyclic redundancy check

lanecfg
    CSI-2 lane configuration

num_data_lanes
    The number of data lanes in use

.. This file was automatic generated / don't edit.

