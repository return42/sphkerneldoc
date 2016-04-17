.. -*- coding: utf-8; mode: rst -*-

==============
phy-qcom-ufs.h
==============


.. _`ufs_qcom_phy_enable_ref_clk`:

ufs_qcom_phy_enable_ref_clk
===========================

.. c:function:: int ufs_qcom_phy_enable_ref_clk (struct phy *phy)

    Enable the phy ref clock.

    :param struct phy \*phy:
        reference to a generic phy



.. _`ufs_qcom_phy_enable_ref_clk.description`:

Description
-----------

returns 0 for success, and non-zero for error.



.. _`ufs_qcom_phy_disable_ref_clk`:

ufs_qcom_phy_disable_ref_clk
============================

.. c:function:: void ufs_qcom_phy_disable_ref_clk (struct phy *phy)

    Disable the phy ref clock.

    :param struct phy \*phy:
        reference to a generic phy.



.. _`ufs_qcom_phy_enable_dev_ref_clk`:

ufs_qcom_phy_enable_dev_ref_clk
===============================

.. c:function:: void ufs_qcom_phy_enable_dev_ref_clk (struct phy *phy)

    Enable the device ref clock.

    :param struct phy \*phy:
        reference to a generic phy.



.. _`ufs_qcom_phy_disable_dev_ref_clk`:

ufs_qcom_phy_disable_dev_ref_clk
================================

.. c:function:: void ufs_qcom_phy_disable_dev_ref_clk (struct phy *phy)

    Disable the device ref clock.

    :param struct phy \*phy:
        reference to a generic phy.

