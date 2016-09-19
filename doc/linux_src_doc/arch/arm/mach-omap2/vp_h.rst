.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/vp.h

.. _`omap_vp_ops`:

struct omap_vp_ops
==================

.. c:type:: struct omap_vp_ops

    per-VP operations

.. _`omap_vp_ops.definition`:

Definition
----------

.. code-block:: c

    struct omap_vp_ops {
        u32 (*check_txdone)(u8 vp_id);
        void (*clear_txdone)(u8 vp_id);
    }

.. _`omap_vp_ops.members`:

Members
-------

check_txdone
    check for VP transaction done

clear_txdone
    clear VP transaction done status

.. _`omap_vp_common`:

struct omap_vp_common
=====================

.. c:type:: struct omap_vp_common

    register data common to all VDDs

.. _`omap_vp_common.definition`:

Definition
----------

.. code-block:: c

    struct omap_vp_common {
        u32 vpconfig_erroroffset_mask;
        u32 vpconfig_errorgain_mask;
        u32 vpconfig_initvoltage_mask;
        u8 vpconfig_timeouten;
        u8 vpconfig_initvdd;
        u8 vpconfig_forceupdate;
        u8 vpconfig_vpenable;
        u8 vstepmin_stepmin_shift;
        u8 vstepmin_smpswaittimemin_shift;
        u8 vstepmax_stepmax_shift;
        u8 vstepmax_smpswaittimemax_shift;
        u8 vlimitto_vddmin_shift;
        u8 vlimitto_vddmax_shift;
        u8 vlimitto_timeout_shift;
        u8 vpvoltage_mask;
        const struct omap_vp_ops *ops;
    }

.. _`omap_vp_common.members`:

Members
-------

vpconfig_erroroffset_mask
    ERROROFFSET bitmask in the PRM_VP\*\_CONFIG reg

vpconfig_errorgain_mask
    ERRORGAIN bitmask in the PRM_VP\*\_CONFIG reg

vpconfig_initvoltage_mask
    INITVOLTAGE bitmask in the PRM_VP\*\_CONFIG reg

vpconfig_timeouten
    TIMEOUT bitmask in the PRM_VP\*\_CONFIG reg

vpconfig_initvdd
    INITVDD bitmask in the PRM_VP\*\_CONFIG reg

vpconfig_forceupdate
    FORCEUPDATE bitmask in the PRM_VP\*\_CONFIG reg

vpconfig_vpenable
    VPENABLE bitmask in the PRM_VP\*\_CONFIG reg

vstepmin_stepmin_shift
    VSTEPMIN field shift in the PRM_VP\*\_VSTEPMIN reg

vstepmin_smpswaittimemin_shift
    SMPSWAITTIMEMIN field shift in PRM_VP\*\_VSTEPMIN reg

vstepmax_stepmax_shift
    VSTEPMAX field shift in the PRM_VP\*\_VSTEPMAX reg

vstepmax_smpswaittimemax_shift
    SMPSWAITTIMEMAX field shift in PRM_VP\*\_VSTEPMAX reg

vlimitto_vddmin_shift
    VDDMIN field shift in PRM_VP\*\_VLIMITTO reg

vlimitto_vddmax_shift
    VDDMAX field shift in PRM_VP\*\_VLIMITTO reg

vlimitto_timeout_shift
    TIMEOUT field shift in PRM_VP\*\_VLIMITTO reg

vpvoltage_mask
    VPVOLTAGE field mask in PRM_VP\*\_VOLTAGE reg

ops
    *undescribed*

.. _`omap_vp_instance`:

struct omap_vp_instance
=======================

.. c:type:: struct omap_vp_instance

    VP register offsets (per-VDD)

.. _`omap_vp_instance.definition`:

Definition
----------

.. code-block:: c

    struct omap_vp_instance {
        const struct omap_vp_common *common;
        u8 vpconfig;
        u8 vstepmin;
        u8 vstepmax;
        u8 vlimitto;
        u8 vstatus;
        u8 voltage;
        u8 id;
        bool enabled;
    }

.. _`omap_vp_instance.members`:

Members
-------

common
    pointer to struct omap_vp_common \* for this SoC

vpconfig
    PRM_VP\*\_CONFIG reg offset from PRM start

vstepmin
    PRM_VP\*\_VSTEPMIN reg offset from PRM start

vstepmax
    *undescribed*

vlimitto
    PRM_VP\*\_VLIMITTO reg offset from PRM start

vstatus
    PRM_VP\*\_VSTATUS reg offset from PRM start

voltage
    PRM_VP\*\_VOLTAGE reg offset from PRM start

id
    Unique identifier for VP instance.

enabled
    flag to keep track of whether vp is enabled or not

.. _`omap_vp_instance.description`:

Description
-----------

XXX vp_common is probably not needed since it is per-SoC

.. This file was automatic generated / don't edit.

