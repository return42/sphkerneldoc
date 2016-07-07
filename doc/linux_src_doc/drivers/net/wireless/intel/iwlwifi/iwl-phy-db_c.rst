.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-phy-db.c

.. _`iwl_phy_db`:

struct iwl_phy_db
=================

.. c:type:: struct iwl_phy_db

    stores phy configuration and calibration data.

.. _`iwl_phy_db.definition`:

Definition
----------

.. code-block:: c

    struct iwl_phy_db {
        struct iwl_phy_db_entry cfg;
        struct iwl_phy_db_entry calib_nch;
        int n_group_papd;
        struct iwl_phy_db_entry *calib_ch_group_papd;
        int n_group_txp;
        struct iwl_phy_db_entry *calib_ch_group_txp;
        struct iwl_trans *trans;
    }

.. _`iwl_phy_db.members`:

Members
-------

cfg
    phy configuration.

calib_nch
    non channel specific calibration data.

n_group_papd
    number of entries in papd channel group.

calib_ch_group_papd
    calibration data related to papd channel group.

n_group_txp
    number of entries in tx power channel group.

calib_ch_group_txp
    calibration data related to tx power chanel group.

trans
    *undescribed*

.. This file was automatic generated / don't edit.

