.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/media/omap4iss.h

.. _`iss_csiphy_lane`:

struct iss_csiphy_lane
======================

.. c:type:: struct iss_csiphy_lane

    CSI2 lane position and polarity

.. _`iss_csiphy_lane.definition`:

Definition
----------

.. code-block:: c

    struct iss_csiphy_lane {
        u8 pos;
        u8 pol;
    }

.. _`iss_csiphy_lane.members`:

Members
-------

pos
    position of the lane

pol
    polarity of the lane

.. _`iss_csiphy_lanes_cfg`:

struct iss_csiphy_lanes_cfg
===========================

.. c:type:: struct iss_csiphy_lanes_cfg

    CSI2 lane configuration

.. _`iss_csiphy_lanes_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iss_csiphy_lanes_cfg {
        struct iss_csiphy_lane data[ISS_CSIPHY1_NUM_DATA_LANES];
        struct iss_csiphy_lane clk;
    }

.. _`iss_csiphy_lanes_cfg.members`:

Members
-------

data
    Configuration of one or two data lanes

clk
    Clock lane configuration

.. _`iss_csi2_platform_data`:

struct iss_csi2_platform_data
=============================

.. c:type:: struct iss_csi2_platform_data

    CSI2 interface platform data

.. _`iss_csi2_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct iss_csi2_platform_data {
        unsigned crc:1;
        unsigned vpclk_div:2;
        struct iss_csiphy_lanes_cfg lanecfg;
    }

.. _`iss_csi2_platform_data.members`:

Members
-------

crc
    Enable the cyclic redundancy check

vpclk_div
    Video port output clock control

lanecfg
    *undescribed*

.. This file was automatic generated / don't edit.

