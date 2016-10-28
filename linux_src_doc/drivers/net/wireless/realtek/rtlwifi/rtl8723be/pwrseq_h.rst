.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/realtek/rtlwifi/rtl8723be/pwrseq.h

.. _`rtl8723b_trans_cardemu_to_act_steps`:

RTL8723B_TRANS_CARDEMU_TO_ACT_STEPS
===================================

.. c:function::  RTL8723B_TRANS_CARDEMU_TO_ACT_STEPS()

    20130425-JackieLau-RTL8723B_Power_Architecture v05.vsd

.. _`rtl8723b_trans_cardemu_to_act_steps.there-are-6-hw-power-states`:

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

.. This file was automatic generated / don't edit.

