.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/phy-qcom-ufs-i.h

.. _`ufs_qcom_phy_specific_ops`:

struct ufs_qcom_phy_specific_ops
================================

.. c:type:: struct ufs_qcom_phy_specific_ops

    set of pointers to functions which have a specific implementation per phy. Each UFS phy, should implement those functions according to its spec and requirements

.. _`ufs_qcom_phy_specific_ops.definition`:

Definition
----------

.. code-block:: c

    struct ufs_qcom_phy_specific_ops {
        int (*calibrate_phy)(struct ufs_qcom_phy *phy, bool is_rate_B);
        void (*start_serdes)(struct ufs_qcom_phy *phy);
        int (*is_physical_coding_sublayer_ready)(struct ufs_qcom_phy *phy);
        void (*set_tx_lane_enable)(struct ufs_qcom_phy *phy, u32 val);
        void (*power_control)(struct ufs_qcom_phy *phy, bool val);
    }

.. _`ufs_qcom_phy_specific_ops.members`:

Members
-------

calibrate_phy
    pointer to a function that calibrate the phy

start_serdes
    pointer to a function that starts the serdes

is_physical_coding_sublayer_ready
    pointer to a function that
    checks pcs readiness. returns 0 for success and non-zero for error.

set_tx_lane_enable
    pointer to a function that enable tx lanes

power_control
    pointer to a function that controls analog rail of phy
    and writes to QSERDES_RX_SIGDET_CNTRL attribute

.. This file was automatic generated / don't edit.

