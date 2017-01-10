.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/enum.h

.. _`efx_loopback_mode`:

enum efx_loopback_mode
======================

.. c:type:: enum efx_loopback_mode

    loopback modes

.. _`efx_loopback_mode.definition`:

Definition
----------

.. code-block:: c

    enum efx_loopback_mode {
        LOOPBACK_NONE,
        LOOPBACK_DATA,
        LOOPBACK_GMAC,
        LOOPBACK_XGMII,
        LOOPBACK_XGXS,
        LOOPBACK_XAUI,
        LOOPBACK_GMII,
        LOOPBACK_SGMII,
        LOOPBACK_XGBR,
        LOOPBACK_XFI,
        LOOPBACK_XAUI_FAR,
        LOOPBACK_GMII_FAR,
        LOOPBACK_SGMII_FAR,
        LOOPBACK_XFI_FAR,
        LOOPBACK_GPHY,
        LOOPBACK_PHYXS,
        LOOPBACK_PCS,
        LOOPBACK_PMAPMD,
        LOOPBACK_XPORT,
        LOOPBACK_XGMII_WS,
        LOOPBACK_XAUI_WS,
        LOOPBACK_XAUI_WS_FAR,
        LOOPBACK_XAUI_WS_NEAR,
        LOOPBACK_GMII_WS,
        LOOPBACK_XFI_WS,
        LOOPBACK_XFI_WS_FAR,
        LOOPBACK_PHYXS_WS,
        LOOPBACK_MAX
    };

.. _`efx_loopback_mode.constants`:

Constants
---------

LOOPBACK_NONE
    no loopback

LOOPBACK_DATA
    data path loopback

LOOPBACK_GMAC
    loopback within GMAC

LOOPBACK_XGMII
    loopback after XMAC

LOOPBACK_XGXS
    loopback within BPX after XGXS

LOOPBACK_XAUI
    loopback within BPX before XAUI serdes

LOOPBACK_GMII
    loopback within BPX after GMAC

LOOPBACK_SGMII
    loopback within BPX within SGMII

LOOPBACK_XGBR
    loopback within BPX within XGBR

LOOPBACK_XFI
    loopback within BPX before XFI serdes

LOOPBACK_XAUI_FAR
    loopback within BPX after XAUI serdes

LOOPBACK_GMII_FAR
    loopback within BPX before SGMII

LOOPBACK_SGMII_FAR
    loopback within BPX after SGMII

LOOPBACK_XFI_FAR
    loopback after XFI serdes

LOOPBACK_GPHY
    loopback within 1G PHY at unspecified level

LOOPBACK_PHYXS
    loopback within 10G PHY at PHYXS level

LOOPBACK_PCS
    loopback within 10G PHY at PCS level

LOOPBACK_PMAPMD
    loopback within 10G PHY at PMAPMD level

LOOPBACK_XPORT
    cross port loopback

LOOPBACK_XGMII_WS
    wireside loopback excluding XMAC

LOOPBACK_XAUI_WS
    wireside loopback within BPX within XAUI serdes

LOOPBACK_XAUI_WS_FAR
    wireside loopback within BPX including XAUI serdes

LOOPBACK_XAUI_WS_NEAR
    wireside loopback within BPX excluding XAUI serdes

LOOPBACK_GMII_WS
    wireside loopback excluding GMAC

LOOPBACK_XFI_WS
    wireside loopback excluding XFI serdes

LOOPBACK_XFI_WS_FAR
    wireside loopback including XFI serdes

LOOPBACK_PHYXS_WS
    wireside loopback within 10G PHY at PHYXS level

LOOPBACK_MAX
    *undescribed*

.. _`reset_type`:

enum reset_type
===============

.. c:type:: enum reset_type

    reset types

.. _`reset_type.definition`:

Definition
----------

.. code-block:: c

    enum reset_type {
        RESET_TYPE_INVISIBLE,
        RESET_TYPE_RECOVER_OR_ALL,
        RESET_TYPE_ALL,
        RESET_TYPE_WORLD,
        RESET_TYPE_RECOVER_OR_DISABLE,
        RESET_TYPE_DATAPATH,
        RESET_TYPE_MC_BIST,
        RESET_TYPE_DISABLE,
        RESET_TYPE_MAX_METHOD,
        RESET_TYPE_TX_WATCHDOG,
        RESET_TYPE_INT_ERROR,
        RESET_TYPE_DMA_ERROR,
        RESET_TYPE_TX_SKIP,
        RESET_TYPE_MC_FAILURE,
        RESET_TYPE_MCDI_TIMEOUT,
        RESET_TYPE_MAX
    };

.. _`reset_type.constants`:

Constants
---------

RESET_TYPE_INVISIBLE
    Reset datapath and MAC (Falcon only)

RESET_TYPE_RECOVER_OR_ALL
    Try to recover. Apply RESET_TYPE_ALL
    if unsuccessful.

RESET_TYPE_ALL
    Reset datapath, MAC and PHY

RESET_TYPE_WORLD
    Reset as much as possible

RESET_TYPE_RECOVER_OR_DISABLE
    Try to recover. Apply RESET_TYPE_DISABLE if
    unsuccessful.

RESET_TYPE_DATAPATH
    Reset datapath only.

RESET_TYPE_MC_BIST
    MC entering BIST mode.

RESET_TYPE_DISABLE
    Reset datapath, MAC and PHY; leave NIC disabled

RESET_TYPE_MAX_METHOD
    *undescribed*

RESET_TYPE_TX_WATCHDOG
    reset due to TX watchdog

RESET_TYPE_INT_ERROR
    reset due to internal error

RESET_TYPE_DMA_ERROR
    DMA error

RESET_TYPE_TX_SKIP
    hardware completed empty tx descriptors

RESET_TYPE_MC_FAILURE
    MC reboot/assertion

RESET_TYPE_MCDI_TIMEOUT
    MCDI timeout.

RESET_TYPE_MAX
    *undescribed*

.. _`reset_type.description`:

Description
-----------

%RESET_TYPE_INVSIBLE, \ ``RESET_TYPE_ALL``\ , \ ``RESET_TYPE_WORLD``\  and
\ ``RESET_TYPE_DISABLE``\  specify the method/scope of the reset.  The
other valuesspecify reasons, which \ :c:func:`efx_schedule_reset`\  will choose
a method for.

Reset methods are numbered in order of increasing scope.

.. This file was automatic generated / don't edit.

