.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/realtek/rtlwifi/rtl8192ee/pwrseq.h

.. _`rtl8192e_trans_cardemu_to_act_steps`:

RTL8192E_TRANS_CARDEMU_TO_ACT_STEPS
===================================

.. c:function::  RTL8192E_TRANS_CARDEMU_TO_ACT_STEPS()

    20110607-Paul-RTL8192E_Power_Architecture-R02.vsd

.. _`rtl8192e_trans_cardemu_to_act_steps.there-are-6-hw-power-states`:

There are 6 HW Power States
---------------------------

0: POFF--Power Off
1: PDN--Power Down
2: CARDEMU--Card Emulation
3: ACT--Active Mode
4: LPS--Low Power State
5: SUS--Suspend

The transision from different states are defined below
TRANS_CARDEMU_TO_ACT
TRANS_ACT_TO_CARDEMU
TRANS_CARDEMU_TO_SUS
TRANS_SUS_TO_CARDEMU
TRANS_CARDEMU_TO_PDN
TRANS_ACT_TO_LPS
TRANS_LPS_TO_ACT

TRANS_END

.. _`rtl8192e_trans_cardemu_to_act_steps.pwr-seq-version`:

PWR SEQ Version
---------------

rtl8192E_PwrSeq_V09.h

.. This file was automatic generated / don't edit.

