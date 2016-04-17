.. -*- coding: utf-8; mode: rst -*-

==========
omap4iss.h
==========


.. _`iss_csiphy_lane`:

struct iss_csiphy_lane
======================

.. c:type:: iss_csiphy_lane

    


.. _`iss_csiphy_lane.definition`:

Definition
----------

.. code-block:: c

  struct iss_csiphy_lane {
    u8 pos;
    u8 pol;
  };


.. _`iss_csiphy_lane.members`:

Members
-------

:``pos``:
    position of the lane

:``pol``:
    polarity of the lane




.. _`iss_csiphy_lanes_cfg`:

struct iss_csiphy_lanes_cfg
===========================

.. c:type:: iss_csiphy_lanes_cfg

    CSI2 lane configuration


.. _`iss_csiphy_lanes_cfg.definition`:

Definition
----------

.. code-block:: c

  struct iss_csiphy_lanes_cfg {
    struct iss_csiphy_lane data[ISS_CSIPHY1_NUM_DATA_LANES];
    struct iss_csiphy_lane clk;
  };


.. _`iss_csiphy_lanes_cfg.members`:

Members
-------

:``data[ISS_CSIPHY1_NUM_DATA_LANES]``:
    Configuration of one or two data lanes

:``clk``:
    Clock lane configuration




.. _`iss_csi2_platform_data`:

struct iss_csi2_platform_data
=============================

.. c:type:: iss_csi2_platform_data

    CSI2 interface platform data


.. _`iss_csi2_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct iss_csi2_platform_data {
    unsigned crc:1;
    unsigned vpclk_div:2;
  };


.. _`iss_csi2_platform_data.members`:

Members
-------

:``crc``:
    Enable the cyclic redundancy check

:``vpclk_div``:
    Video port output clock control


