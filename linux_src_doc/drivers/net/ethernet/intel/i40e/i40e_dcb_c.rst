.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_dcb.c

.. _`i40e_get_dcbx_status`:

i40e_get_dcbx_status
====================

.. c:function:: i40e_status i40e_get_dcbx_status(struct i40e_hw *hw, u16 *status)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param status:
        Embedded DCBX Engine Status
    :type status: u16 \*

.. _`i40e_get_dcbx_status.description`:

Description
-----------

Get the DCBX status from the Firmware

.. _`i40e_parse_ieee_etscfg_tlv`:

i40e_parse_ieee_etscfg_tlv
==========================

.. c:function:: void i40e_parse_ieee_etscfg_tlv(struct i40e_lldp_org_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        IEEE 802.1Qaz ETS CFG TLV
    :type tlv: struct i40e_lldp_org_tlv \*

    :param dcbcfg:
        Local store to update ETS CFG data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_ieee_etscfg_tlv.description`:

Description
-----------

Parses IEEE 802.1Qaz ETS CFG TLV

.. _`i40e_parse_ieee_etsrec_tlv`:

i40e_parse_ieee_etsrec_tlv
==========================

.. c:function:: void i40e_parse_ieee_etsrec_tlv(struct i40e_lldp_org_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        IEEE 802.1Qaz ETS REC TLV
    :type tlv: struct i40e_lldp_org_tlv \*

    :param dcbcfg:
        Local store to update ETS REC data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_ieee_etsrec_tlv.description`:

Description
-----------

Parses IEEE 802.1Qaz ETS REC TLV

.. _`i40e_parse_ieee_pfccfg_tlv`:

i40e_parse_ieee_pfccfg_tlv
==========================

.. c:function:: void i40e_parse_ieee_pfccfg_tlv(struct i40e_lldp_org_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        IEEE 802.1Qaz PFC CFG TLV
    :type tlv: struct i40e_lldp_org_tlv \*

    :param dcbcfg:
        Local store to update PFC CFG data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_ieee_pfccfg_tlv.description`:

Description
-----------

Parses IEEE 802.1Qaz PFC CFG TLV

.. _`i40e_parse_ieee_app_tlv`:

i40e_parse_ieee_app_tlv
=======================

.. c:function:: void i40e_parse_ieee_app_tlv(struct i40e_lldp_org_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        IEEE 802.1Qaz APP TLV
    :type tlv: struct i40e_lldp_org_tlv \*

    :param dcbcfg:
        Local store to update APP PRIO data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_ieee_app_tlv.description`:

Description
-----------

Parses IEEE 802.1Qaz APP PRIO TLV

.. _`i40e_parse_ieee_tlv`:

i40e_parse_ieee_tlv
===================

.. c:function:: void i40e_parse_ieee_tlv(struct i40e_lldp_org_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        IEEE 802.1Qaz TLV
    :type tlv: struct i40e_lldp_org_tlv \*

    :param dcbcfg:
        Local store to update ETS REC data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_ieee_tlv.description`:

Description
-----------

Get the TLV subtype and send it to parsing function
based on the subtype value

.. _`i40e_parse_cee_pgcfg_tlv`:

i40e_parse_cee_pgcfg_tlv
========================

.. c:function:: void i40e_parse_cee_pgcfg_tlv(struct i40e_cee_feat_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        CEE DCBX PG CFG TLV
    :type tlv: struct i40e_cee_feat_tlv \*

    :param dcbcfg:
        Local store to update ETS CFG data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_cee_pgcfg_tlv.description`:

Description
-----------

Parses CEE DCBX PG CFG TLV

.. _`i40e_parse_cee_pfccfg_tlv`:

i40e_parse_cee_pfccfg_tlv
=========================

.. c:function:: void i40e_parse_cee_pfccfg_tlv(struct i40e_cee_feat_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        CEE DCBX PFC CFG TLV
    :type tlv: struct i40e_cee_feat_tlv \*

    :param dcbcfg:
        Local store to update PFC CFG data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_cee_pfccfg_tlv.description`:

Description
-----------

Parses CEE DCBX PFC CFG TLV

.. _`i40e_parse_cee_app_tlv`:

i40e_parse_cee_app_tlv
======================

.. c:function:: void i40e_parse_cee_app_tlv(struct i40e_cee_feat_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        CEE DCBX APP TLV
    :type tlv: struct i40e_cee_feat_tlv \*

    :param dcbcfg:
        Local store to update APP PRIO data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_cee_app_tlv.description`:

Description
-----------

Parses CEE DCBX APP PRIO TLV

.. _`i40e_parse_cee_tlv`:

i40e_parse_cee_tlv
==================

.. c:function:: void i40e_parse_cee_tlv(struct i40e_lldp_org_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        CEE DCBX TLV
    :type tlv: struct i40e_lldp_org_tlv \*

    :param dcbcfg:
        Local store to update DCBX config data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_cee_tlv.description`:

Description
-----------

Get the TLV subtype and send it to parsing function
based on the subtype value

.. _`i40e_parse_org_tlv`:

i40e_parse_org_tlv
==================

.. c:function:: void i40e_parse_org_tlv(struct i40e_lldp_org_tlv *tlv, struct i40e_dcbx_config *dcbcfg)

    :param tlv:
        Organization specific TLV
    :type tlv: struct i40e_lldp_org_tlv \*

    :param dcbcfg:
        Local store to update ETS REC data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_parse_org_tlv.description`:

Description
-----------

Currently only IEEE 802.1Qaz TLV is supported, all others
will be returned

.. _`i40e_lldp_to_dcb_config`:

i40e_lldp_to_dcb_config
=======================

.. c:function:: i40e_status i40e_lldp_to_dcb_config(u8 *lldpmib, struct i40e_dcbx_config *dcbcfg)

    :param lldpmib:
        LLDPDU to be parsed
    :type lldpmib: u8 \*

    :param dcbcfg:
        store for LLDPDU data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_lldp_to_dcb_config.description`:

Description
-----------

Parse DCB configuration from the LLDPDU

.. _`i40e_aq_get_dcb_config`:

i40e_aq_get_dcb_config
======================

.. c:function:: i40e_status i40e_aq_get_dcb_config(struct i40e_hw *hw, u8 mib_type, u8 bridgetype, struct i40e_dcbx_config *dcbcfg)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param mib_type:
        mib type for the query
    :type mib_type: u8

    :param bridgetype:
        bridge type for the query (remote)
    :type bridgetype: u8

    :param dcbcfg:
        store for LLDPDU data
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_aq_get_dcb_config.description`:

Description
-----------

Query DCB configuration from the Firmware

.. _`i40e_cee_to_dcb_v1_config`:

i40e_cee_to_dcb_v1_config
=========================

.. c:function:: void i40e_cee_to_dcb_v1_config(struct i40e_aqc_get_cee_dcb_cfg_v1_resp *cee_cfg, struct i40e_dcbx_config *dcbcfg)

    :param cee_cfg:
        pointer to CEE v1 response configuration struct
    :type cee_cfg: struct i40e_aqc_get_cee_dcb_cfg_v1_resp \*

    :param dcbcfg:
        DCB configuration struct
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_cee_to_dcb_v1_config.description`:

Description
-----------

Convert CEE v1 configuration from firmware to DCB configuration

.. _`i40e_cee_to_dcb_config`:

i40e_cee_to_dcb_config
======================

.. c:function:: void i40e_cee_to_dcb_config(struct i40e_aqc_get_cee_dcb_cfg_resp *cee_cfg, struct i40e_dcbx_config *dcbcfg)

    :param cee_cfg:
        pointer to CEE configuration struct
    :type cee_cfg: struct i40e_aqc_get_cee_dcb_cfg_resp \*

    :param dcbcfg:
        DCB configuration struct
    :type dcbcfg: struct i40e_dcbx_config \*

.. _`i40e_cee_to_dcb_config.description`:

Description
-----------

Convert CEE configuration from firmware to DCB configuration

.. _`i40e_get_ieee_dcb_config`:

i40e_get_ieee_dcb_config
========================

.. c:function:: i40e_status i40e_get_ieee_dcb_config(struct i40e_hw *hw)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_get_ieee_dcb_config.description`:

Description
-----------

Get IEEE mode DCB configuration from the Firmware

.. _`i40e_get_dcb_config`:

i40e_get_dcb_config
===================

.. c:function:: i40e_status i40e_get_dcb_config(struct i40e_hw *hw)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_get_dcb_config.description`:

Description
-----------

Get DCB configuration from the Firmware

.. _`i40e_init_dcb`:

i40e_init_dcb
=============

.. c:function:: i40e_status i40e_init_dcb(struct i40e_hw *hw)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_init_dcb.description`:

Description
-----------

Update DCB configuration from the Firmware

.. _`_i40e_read_lldp_cfg`:

\_i40e_read_lldp_cfg
====================

.. c:function:: i40e_status _i40e_read_lldp_cfg(struct i40e_hw *hw, struct i40e_lldp_variables *lldp_cfg, u8 module, u32 word_offset)

    generic read of LLDP Configuration data from NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param lldp_cfg:
        pointer to hold lldp configuration variables
    :type lldp_cfg: struct i40e_lldp_variables \*

    :param module:
        address of the module pointer
    :type module: u8

    :param word_offset:
        offset of LLDP configuration
    :type word_offset: u32

.. _`_i40e_read_lldp_cfg.description`:

Description
-----------

Reads the LLDP configuration data from NVM using passed addresses

.. _`i40e_read_lldp_cfg`:

i40e_read_lldp_cfg
==================

.. c:function:: i40e_status i40e_read_lldp_cfg(struct i40e_hw *hw, struct i40e_lldp_variables *lldp_cfg)

    read LLDP Configuration data from NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param lldp_cfg:
        pointer to hold lldp configuration variables
    :type lldp_cfg: struct i40e_lldp_variables \*

.. _`i40e_read_lldp_cfg.description`:

Description
-----------

Reads the LLDP configuration data from NVM

.. This file was automatic generated / don't edit.

