.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/debug.h

.. _`ath_interrupt_stats`:

struct ath_interrupt_stats
==========================

.. c:type:: struct ath_interrupt_stats

    Contains statistics about interrupts

.. _`ath_interrupt_stats.definition`:

Definition
----------

.. code-block:: c

    struct ath_interrupt_stats {
        u32 total;
        u32 rxok;
        u32 rxlp;
        u32 rxhp;
        u32 rxeol;
        u32 rxorn;
        u32 txok;
        u32 txeol;
        u32 txurn;
        u32 mib;
        u32 rxphyerr;
        u32 rx_keycache_miss;
        u32 swba;
        u32 bmiss;
        u32 bnr;
        u32 cst;
        u32 gtt;
        u32 tim;
        u32 cabend;
        u32 dtimsync;
        u32 dtim;
        u32 bb_watchdog;
        u32 tsfoor;
        u32 mci;
        u32 gen_timer;
        u32 sync_cause_all;
        u32 sync_rtc_irq;
        u32 sync_mac_irq;
        u32 eeprom_illegal_access;
        u32 apb_timeout;
        u32 pci_mode_conflict;
        u32 host1_fatal;
        u32 host1_perr;
        u32 trcv_fifo_perr;
        u32 radm_cpl_ep;
        u32 radm_cpl_dllp_abort;
        u32 radm_cpl_tlp_abort;
        u32 radm_cpl_ecrc_err;
        u32 radm_cpl_timeout;
        u32 local_timeout;
        u32 pm_access;
        u32 mac_awake;
        u32 mac_asleep;
        u32 mac_sleep_access;
    }

.. _`ath_interrupt_stats.members`:

Members
-------

total
    Total no. of interrupts generated so far

rxok
    RX with no errors

rxlp
    RX with low priority RX

rxhp
    RX with high priority, uapsd only

rxeol
    RX with no more RXDESC available

rxorn
    RX FIFO overrun

txok
    TX completed at the requested rate

txeol
    *undescribed*

txurn
    TX FIFO underrun

mib
    MIB regs reaching its threshold

rxphyerr
    RX with phy errors

rx_keycache_miss
    RX with key cache misses

swba
    Software Beacon Alert

bmiss
    Beacon Miss

bnr
    Beacon Not Ready

cst
    Carrier Sense TImeout

gtt
    Global TX Timeout

tim
    RX beacon TIM occurrence

cabend
    RX End of CAB traffic

dtimsync
    DTIM sync lossage

dtim
    RX Beacon with DTIM

bb_watchdog
    Baseband watchdog

tsfoor
    TSF out of range, indicates that the corrected TSF received
    from a beacon differs from the PCU's internal TSF by more than a
    (programmable) threshold

mci
    MCI interrupt, specific to MCI based BTCOEX chipsets

gen_timer
    Generic hardware timer interrupt

sync_cause_all
    *undescribed*

sync_rtc_irq
    *undescribed*

sync_mac_irq
    *undescribed*

eeprom_illegal_access
    *undescribed*

apb_timeout
    *undescribed*

pci_mode_conflict
    *undescribed*

host1_fatal
    *undescribed*

host1_perr
    *undescribed*

trcv_fifo_perr
    *undescribed*

radm_cpl_ep
    *undescribed*

radm_cpl_dllp_abort
    *undescribed*

radm_cpl_tlp_abort
    *undescribed*

radm_cpl_ecrc_err
    *undescribed*

radm_cpl_timeout
    *undescribed*

local_timeout
    Internal bus timeout.

pm_access
    *undescribed*

mac_awake
    *undescribed*

mac_asleep
    *undescribed*

mac_sleep_access
    *undescribed*

.. _`ath_tx_stats`:

struct ath_tx_stats
===================

.. c:type:: struct ath_tx_stats

    Statistics about TX

.. _`ath_tx_stats.definition`:

Definition
----------

.. code-block:: c

    struct ath_tx_stats {
        u32 tx_pkts_all;
        u32 tx_bytes_all;
        u32 queued;
        u32 completed;
        u32 xretries;
        u32 a_aggr;
        u32 a_queued_hw;
        u32 a_completed;
        u32 a_retries;
        u32 a_xretries;
        u32 txerr_filtered;
        u32 fifo_underrun;
        u32 xtxop;
        u32 timer_exp;
        u32 desc_cfg_err;
        u32 data_underrun;
        u32 delim_underrun;
        u32 puttxbuf;
        u32 txstart;
        u32 txprocdesc;
        u32 txfailed;
    }

.. _`ath_tx_stats.members`:

Members
-------

tx_pkts_all
    No. of total frames transmitted, including ones that

tx_bytes_all
    No. of total bytes transmitted, including ones that

queued
    Total MPDUs (non-aggr) queued

completed
    Total MPDUs (non-aggr) completed

xretries
    *undescribed*

a_aggr
    Total no. of aggregates queued

a_queued_hw
    Total AMPDUs queued to hardware

a_completed
    Total AMPDUs completed

a_retries
    No. of AMPDUs retried (SW)

a_xretries
    No. of AMPDUs dropped due to xretries

txerr_filtered
    No. of frames with TXERR_FILT flag set.

fifo_underrun
    FIFO underrun occurrences

xtxop
    No. of frames filtered because of TXOP limit

timer_exp
    Transmit timer expiry

desc_cfg_err
    Descriptor configuration errors

data_underrun
    *undescribed*

delim_underrun
    *undescribed*

puttxbuf
    Number of times hardware was given txbuf to write.

txstart
    Number of times hardware was told to start tx.

txprocdesc
    Number of times tx descriptor was processed

txfailed
    Out-of-memory or other errors in xmit path.

.. This file was automatic generated / don't edit.

