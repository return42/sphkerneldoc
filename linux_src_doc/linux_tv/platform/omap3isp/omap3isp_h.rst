.. -*- coding: utf-8; mode: rst -*-

==========
omap3isp.h
==========



.. _xref_struct_isp_parallel_cfg:

struct isp_parallel_cfg
=======================

.. c:type:: struct isp_parallel_cfg

    Parallel interface configuration



Definition
----------

.. code-block:: c

  struct isp_parallel_cfg {
    unsigned int data_lane_shift:2;
    unsigned int clk_pol:1;
    unsigned int hs_pol:1;
    unsigned int vs_pol:1;
    unsigned int fld_pol:1;
    unsigned int data_pol:1;
  };



Members
-------

:``unsigned int:2 data_lane_shift``:
    Data lane shifter
    		0 - CAMEXT[13:0] -> CAM[13:0]
    		1 - CAMEXT[13:2] -> CAM[11:0]
    		2 - CAMEXT[13:4] -> CAM[9:0]
    		3 - CAMEXT[13:6] -> CAM[7:0]

:``unsigned int:1 clk_pol``:
    Pixel clock polarity
    		0 - Sample on rising edge, 1 - Sample on falling edge

:``unsigned int:1 hs_pol``:
    Horizontal synchronization polarity
    		0 - Active high, 1 - Active low

:``unsigned int:1 vs_pol``:
    Vertical synchronization polarity
    		0 - Active high, 1 - Active low

:``unsigned int:1 fld_pol``:
    Field signal polarity
    		0 - Positive, 1 - Negative

:``unsigned int:1 data_pol``:
    Data polarity
    		0 - Normal, 1 - One's complement





.. _xref_struct_isp_csiphy_lane:

struct isp_csiphy_lane
======================

.. c:type:: struct isp_csiphy_lane

    



Definition
----------

.. code-block:: c

  struct isp_csiphy_lane {
    u8 pos;
    u8 pol;
  };



Members
-------

:``u8 pos``:
    position of the lane

:``u8 pol``:
    polarity of the lane





.. _xref_struct_isp_csiphy_lanes_cfg:

struct isp_csiphy_lanes_cfg
===========================

.. c:type:: struct isp_csiphy_lanes_cfg

    CCP2/CSI2 lane configuration



Definition
----------

.. code-block:: c

  struct isp_csiphy_lanes_cfg {
    struct isp_csiphy_lane data[ISP_CSIPHY2_NUM_DATA_LANES];
    struct isp_csiphy_lane clk;
  };



Members
-------

:``struct isp_csiphy_lane data[ISP_CSIPHY2_NUM_DATA_LANES]``:
    Configuration of one or two data lanes

:``struct isp_csiphy_lane clk``:
    Clock lane configuration





.. _xref_struct_isp_ccp2_cfg:

struct isp_ccp2_cfg
===================

.. c:type:: struct isp_ccp2_cfg

    CCP2 interface configuration



Definition
----------

.. code-block:: c

  struct isp_ccp2_cfg {
    unsigned int strobe_clk_pol:1;
    unsigned int crc:1;
    unsigned int ccp2_mode:1;
    unsigned int phy_layer:1;
    unsigned int vpclk_div:2;
  };



Members
-------

:``unsigned int:1 strobe_clk_pol``:
    Strobe/clock polarity
    		0 - Non Inverted, 1 - Inverted

:``unsigned int:1 crc``:
    Enable the cyclic redundancy check

:``unsigned int:1 ccp2_mode``:
    Enable CCP2 compatibility mode
    		ISP_CCP2_MODE_MIPI - MIPI-CSI1 mode
    		ISP_CCP2_MODE_CCP2 - CCP2 mode

:``unsigned int:1 phy_layer``:
    Physical layer selection
    		ISP_CCP2_PHY_DATA_CLOCK - Data/clock physical layer
    		ISP_CCP2_PHY_DATA_STROBE - Data/strobe physical layer

:``unsigned int:2 vpclk_div``:
    Video port output clock control





.. _xref_struct_isp_csi2_cfg:

struct isp_csi2_cfg
===================

.. c:type:: struct isp_csi2_cfg

    CSI2 interface configuration



Definition
----------

.. code-block:: c

  struct isp_csi2_cfg {
    unsigned crc:1;
  };



Members
-------

:``unsigned:1 crc``:
    Enable the cyclic redundancy check



