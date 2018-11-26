.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/btcoex.c

.. _`brcmf_btcoex_state`:

enum brcmf_btcoex_state
=======================

.. c:type:: enum brcmf_btcoex_state

    BT coex DHCP state machine states

.. _`brcmf_btcoex_state.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_btcoex_state {
        BRCMF_BT_DHCP_IDLE,
        BRCMF_BT_DHCP_START,
        BRCMF_BT_DHCP_OPPR_WIN,
        BRCMF_BT_DHCP_FLAG_FORCE_TIMEOUT
    };

.. _`brcmf_btcoex_state.constants`:

Constants
---------

BRCMF_BT_DHCP_IDLE
    DCHP is idle

BRCMF_BT_DHCP_START
    DHCP started, wait before
    boosting wifi priority

BRCMF_BT_DHCP_OPPR_WIN
    graceful DHCP opportunity ended,
    boost wifi priority

BRCMF_BT_DHCP_FLAG_FORCE_TIMEOUT
    wifi priority boost end,
    restore defaults

.. _`brcmf_btcoex_info`:

struct brcmf_btcoex_info
========================

.. c:type:: struct brcmf_btcoex_info

    BT coex related information

.. _`brcmf_btcoex_info.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_btcoex_info {
        struct brcmf_cfg80211_vif *vif;
        struct timer_list timer;
        u16 timeout;
        bool timer_on;
        bool dhcp_done;
        enum brcmf_btcoex_state bt_state;
        struct work_struct work;
        struct brcmf_cfg80211_info *cfg;
        u32 reg66;
        u32 reg41;
        u32 reg68;
        bool saved_regs_part1;
        u32 reg50;
        u32 reg51;
        u32 reg64;
        u32 reg65;
        u32 reg71;
        bool saved_regs_part2;
    }

.. _`brcmf_btcoex_info.members`:

Members
-------

vif
    interface for which request was done.

timer
    timer for DHCP state machine

timeout
    configured timeout.

timer_on
    DHCP timer active

dhcp_done
    DHCP finished before T1/T2 timer expiration

bt_state
    DHCP state machine state

work
    DHCP state machine work

cfg
    driver private data for cfg80211 interface

reg66
    saved value of btc_params 66

reg41
    saved value of btc_params 41

reg68
    saved value of btc_params 68

saved_regs_part1
    flag indicating regs 50,51,64,65,71
    have been saved

reg50
    *undescribed*

reg51
    saved value of btc_params 51

reg64
    saved value of btc_params 64

reg65
    saved value of btc_params 65

reg71
    saved value of btc_params 71

saved_regs_part2
    *undescribed*

.. _`brcmf_btcoex_params_write`:

brcmf_btcoex_params_write
=========================

.. c:function:: s32 brcmf_btcoex_params_write(struct brcmf_if *ifp, u32 addr, u32 data)

    write btc_params firmware variable

    :param ifp:
        interface
    :type ifp: struct brcmf_if \*

    :param addr:
        btc_params register number
    :type addr: u32

    :param data:
        data to write
    :type data: u32

.. _`brcmf_btcoex_params_read`:

brcmf_btcoex_params_read
========================

.. c:function:: s32 brcmf_btcoex_params_read(struct brcmf_if *ifp, u32 addr, u32 *data)

    read btc_params firmware variable

    :param ifp:
        interface
    :type ifp: struct brcmf_if \*

    :param addr:
        btc_params register number
    :type addr: u32

    :param data:
        read data
    :type data: u32 \*

.. _`brcmf_btcoex_boost_wifi`:

brcmf_btcoex_boost_wifi
=======================

.. c:function:: void brcmf_btcoex_boost_wifi(struct brcmf_btcoex_info *btci, bool trump_sco)

    control BT SCO/eSCO parameters

    :param btci:
        BT coex info
    :type btci: struct brcmf_btcoex_info \*

    :param trump_sco:
        true - set SCO/eSCO parameters for compatibility
        during DHCP window
        false - restore saved parameter values
    :type trump_sco: bool

.. _`brcmf_btcoex_boost_wifi.description`:

Description
-----------

Enhanced BT COEX settings for eSCO compatibility during DHCP window

.. _`brcmf_btcoex_is_sco_active`:

brcmf_btcoex_is_sco_active
==========================

.. c:function:: bool brcmf_btcoex_is_sco_active(struct brcmf_if *ifp)

    check if SCO/eSCO is active

    :param ifp:
        interface
    :type ifp: struct brcmf_if \*

.. _`brcmf_btcoex_is_sco_active.return`:

Return
------

true if SCO/eSCO session is active

.. _`btcmf_btcoex_save_part1`:

btcmf_btcoex_save_part1
=======================

.. c:function:: void btcmf_btcoex_save_part1(struct brcmf_btcoex_info *btci)

    save first step parameters.

    :param btci:
        *undescribed*
    :type btci: struct brcmf_btcoex_info \*

.. _`brcmf_btcoex_restore_part1`:

brcmf_btcoex_restore_part1
==========================

.. c:function:: void brcmf_btcoex_restore_part1(struct brcmf_btcoex_info *btci)

    restore first step parameters.

    :param btci:
        *undescribed*
    :type btci: struct brcmf_btcoex_info \*

.. _`brcmf_btcoex_timerfunc`:

brcmf_btcoex_timerfunc
======================

.. c:function:: void brcmf_btcoex_timerfunc(struct timer_list *t)

    BT coex timer callback

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`brcmf_btcoex_handler`:

brcmf_btcoex_handler
====================

.. c:function:: void brcmf_btcoex_handler(struct work_struct *work)

    BT coex state machine work handler

    :param work:
        work
    :type work: struct work_struct \*

.. _`brcmf_btcoex_attach`:

brcmf_btcoex_attach
===================

.. c:function:: int brcmf_btcoex_attach(struct brcmf_cfg80211_info *cfg)

    initialize BT coex data

    :param cfg:
        driver private cfg80211 data
    :type cfg: struct brcmf_cfg80211_info \*

.. _`brcmf_btcoex_attach.return`:

Return
------

0 on success

.. _`brcmf_btcoex_detach`:

brcmf_btcoex_detach
===================

.. c:function:: void brcmf_btcoex_detach(struct brcmf_cfg80211_info *cfg)

    clean BT coex data

    :param cfg:
        driver private cfg80211 data
    :type cfg: struct brcmf_cfg80211_info \*

.. _`brcmf_btcoex_set_mode`:

brcmf_btcoex_set_mode
=====================

.. c:function:: int brcmf_btcoex_set_mode(struct brcmf_cfg80211_vif *vif, enum brcmf_btcoex_mode mode, u16 duration)

    set BT coex mode

    :param vif:
        *undescribed*
    :type vif: struct brcmf_cfg80211_vif \*

    :param mode:
        Wifi-Bluetooth coexistence mode
    :type mode: enum brcmf_btcoex_mode

    :param duration:
        *undescribed*
    :type duration: u16

.. _`brcmf_btcoex_set_mode.return`:

Return
------

0 on success

.. This file was automatic generated / don't edit.

