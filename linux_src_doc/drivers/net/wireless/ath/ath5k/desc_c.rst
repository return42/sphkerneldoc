.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/desc.c

.. _`hardware-descriptor-functions`:

Hardware descriptor functions
=============================

Here we handle the processing of the low-level hw descriptors
that hw reads and writes via DMA for each TX and RX attempt (that means
we can also have descriptors for failed TX/RX tries). We have two kind of
descriptors for RX and TX, control descriptors tell the hw how to send or
receive a packet where to read/write it from/to etc and status descriptors
that contain information about how the packet was sent or received (errors
included).

Descriptor format is not exactly the same for each MAC chip version so we
have function pointers on \ :c:type:`struct ath5k_hw <ath5k_hw>`\  we initialize at runtime based on
the chip used.

.. _`ath5k_hw_setup_2word_tx_desc`:

ath5k_hw_setup_2word_tx_desc
============================

.. c:function:: int ath5k_hw_setup_2word_tx_desc(struct ath5k_hw *ah, struct ath5k_desc *desc, unsigned int pkt_len, unsigned int hdr_len, int padsize, enum ath5k_pkt_type type, unsigned int tx_power, unsigned int tx_rate0, unsigned int tx_tries0, unsigned int key_index, unsigned int antenna_mode, unsigned int flags, unsigned int rtscts_rate, unsigned int rtscts_duration)

    Initialize a 2-word tx control descriptor

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param pkt_len:
        Frame length in bytes
    :type pkt_len: unsigned int

    :param hdr_len:
        Header length in bytes (only used on AR5210)
    :type hdr_len: unsigned int

    :param padsize:
        Any padding we've added to the frame length
    :type padsize: int

    :param type:
        One of enum ath5k_pkt_type
    :type type: enum ath5k_pkt_type

    :param tx_power:
        Tx power in 0.5dB steps
    :type tx_power: unsigned int

    :param tx_rate0:
        HW idx for transmission rate
    :type tx_rate0: unsigned int

    :param tx_tries0:
        Max number of retransmissions
    :type tx_tries0: unsigned int

    :param key_index:
        Index on key table to use for encryption
    :type key_index: unsigned int

    :param antenna_mode:
        Which antenna to use (0 for auto)
    :type antenna_mode: unsigned int

    :param flags:
        One of AR5K_TXDESC\_\* flags (desc.h)
    :type flags: unsigned int

    :param rtscts_rate:
        HW idx for RTS/CTS transmission rate
    :type rtscts_rate: unsigned int

    :param rtscts_duration:
        What to put on duration field on the header of RTS/CTS
    :type rtscts_duration: unsigned int

.. _`ath5k_hw_setup_2word_tx_desc.description`:

Description
-----------

Internal function to initialize a 2-Word TX control descriptor
found on AR5210 and AR5211 MACs chips.

Returns 0 on success or -EINVAL on false input

.. _`ath5k_hw_setup_4word_tx_desc`:

ath5k_hw_setup_4word_tx_desc
============================

.. c:function:: int ath5k_hw_setup_4word_tx_desc(struct ath5k_hw *ah, struct ath5k_desc *desc, unsigned int pkt_len, unsigned int hdr_len, int padsize, enum ath5k_pkt_type type, unsigned int tx_power, unsigned int tx_rate0, unsigned int tx_tries0, unsigned int key_index, unsigned int antenna_mode, unsigned int flags, unsigned int rtscts_rate, unsigned int rtscts_duration)

    Initialize a 4-word tx control descriptor

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param pkt_len:
        Frame length in bytes
    :type pkt_len: unsigned int

    :param hdr_len:
        Header length in bytes (only used on AR5210)
    :type hdr_len: unsigned int

    :param padsize:
        Any padding we've added to the frame length
    :type padsize: int

    :param type:
        One of enum ath5k_pkt_type
    :type type: enum ath5k_pkt_type

    :param tx_power:
        Tx power in 0.5dB steps
    :type tx_power: unsigned int

    :param tx_rate0:
        HW idx for transmission rate
    :type tx_rate0: unsigned int

    :param tx_tries0:
        Max number of retransmissions
    :type tx_tries0: unsigned int

    :param key_index:
        Index on key table to use for encryption
    :type key_index: unsigned int

    :param antenna_mode:
        Which antenna to use (0 for auto)
    :type antenna_mode: unsigned int

    :param flags:
        One of AR5K_TXDESC\_\* flags (desc.h)
    :type flags: unsigned int

    :param rtscts_rate:
        HW idx for RTS/CTS transmission rate
    :type rtscts_rate: unsigned int

    :param rtscts_duration:
        What to put on duration field on the header of RTS/CTS
    :type rtscts_duration: unsigned int

.. _`ath5k_hw_setup_4word_tx_desc.description`:

Description
-----------

Internal function to initialize a 4-Word TX control descriptor
found on AR5212 and later MACs chips.

Returns 0 on success or -EINVAL on false input

.. _`ath5k_hw_setup_mrr_tx_desc`:

ath5k_hw_setup_mrr_tx_desc
==========================

.. c:function:: int ath5k_hw_setup_mrr_tx_desc(struct ath5k_hw *ah, struct ath5k_desc *desc, u_int tx_rate1, u_int tx_tries1, u_int tx_rate2, u_int tx_tries2, u_int tx_rate3, u_int tx_tries3)

    Initialize an MRR tx control descriptor

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param tx_rate1:
        HW idx for rate used on transmission series 1
    :type tx_rate1: u_int

    :param tx_tries1:
        Max number of retransmissions for transmission series 1
    :type tx_tries1: u_int

    :param tx_rate2:
        HW idx for rate used on transmission series 2
    :type tx_rate2: u_int

    :param tx_tries2:
        Max number of retransmissions for transmission series 2
    :type tx_tries2: u_int

    :param tx_rate3:
        HW idx for rate used on transmission series 3
    :type tx_rate3: u_int

    :param tx_tries3:
        Max number of retransmissions for transmission series 3
    :type tx_tries3: u_int

.. _`ath5k_hw_setup_mrr_tx_desc.description`:

Description
-----------

Multi rate retry (MRR) tx control descriptors are available only on AR5212
MACs, they are part of the normal 4-word tx control descriptor (see above)
but we handle them through a separate function for better abstraction.

Returns 0 on success or -EINVAL on invalid input

.. _`ath5k_hw_proc_2word_tx_status`:

ath5k_hw_proc_2word_tx_status
=============================

.. c:function:: int ath5k_hw_proc_2word_tx_status(struct ath5k_hw *ah, struct ath5k_desc *desc, struct ath5k_tx_status *ts)

    Process a tx status descriptor on 5210/1

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param ts:
        The \ :c:type:`struct ath5k_tx_status <ath5k_tx_status>`\ 
    :type ts: struct ath5k_tx_status \*

.. _`ath5k_hw_proc_4word_tx_status`:

ath5k_hw_proc_4word_tx_status
=============================

.. c:function:: int ath5k_hw_proc_4word_tx_status(struct ath5k_hw *ah, struct ath5k_desc *desc, struct ath5k_tx_status *ts)

    Process a tx status descriptor on 5212

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param ts:
        The \ :c:type:`struct ath5k_tx_status <ath5k_tx_status>`\ 
    :type ts: struct ath5k_tx_status \*

.. _`ath5k_hw_setup_rx_desc`:

ath5k_hw_setup_rx_desc
======================

.. c:function:: int ath5k_hw_setup_rx_desc(struct ath5k_hw *ah, struct ath5k_desc *desc, u32 size, unsigned int flags)

    Initialize an rx control descriptor

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param size:
        RX buffer length in bytes
    :type size: u32

    :param flags:
        One of AR5K_RXDESC\_\* flags
    :type flags: unsigned int

.. _`ath5k_hw_proc_5210_rx_status`:

ath5k_hw_proc_5210_rx_status
============================

.. c:function:: int ath5k_hw_proc_5210_rx_status(struct ath5k_hw *ah, struct ath5k_desc *desc, struct ath5k_rx_status *rs)

    Process the rx status descriptor on 5210/1

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param rs:
        The \ :c:type:`struct ath5k_rx_status <ath5k_rx_status>`\ 
    :type rs: struct ath5k_rx_status \*

.. _`ath5k_hw_proc_5210_rx_status.description`:

Description
-----------

Internal function used to process an RX status descriptor
on AR5210/5211 MAC.

Returns 0 on success or -EINPROGRESS in case we haven't received the who;e
frame yet.

.. _`ath5k_hw_proc_5212_rx_status`:

ath5k_hw_proc_5212_rx_status
============================

.. c:function:: int ath5k_hw_proc_5212_rx_status(struct ath5k_hw *ah, struct ath5k_desc *desc, struct ath5k_rx_status *rs)

    Process the rx status descriptor on 5212

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param desc:
        The \ :c:type:`struct ath5k_desc <ath5k_desc>`\ 
    :type desc: struct ath5k_desc \*

    :param rs:
        The \ :c:type:`struct ath5k_rx_status <ath5k_rx_status>`\ 
    :type rs: struct ath5k_rx_status \*

.. _`ath5k_hw_proc_5212_rx_status.description`:

Description
-----------

Internal function used to process an RX status descriptor
on AR5212 and later MAC.

Returns 0 on success or -EINPROGRESS in case we haven't received the who;e
frame yet.

.. _`ath5k_hw_init_desc_functions`:

ath5k_hw_init_desc_functions
============================

.. c:function:: int ath5k_hw_init_desc_functions(struct ath5k_hw *ah)

    Init function pointers inside ah

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_init_desc_functions.description`:

Description
-----------

Maps the internal descriptor functions to the function pointers on ah, used
from above. This is used as an abstraction layer to handle the various chips
the same way.

.. This file was automatic generated / don't edit.

