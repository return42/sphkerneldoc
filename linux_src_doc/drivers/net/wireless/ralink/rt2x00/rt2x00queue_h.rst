.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ralink/rt2x00/rt2x00queue.h

.. _`data_queue_qid`:

enum data_queue_qid
===================

.. c:type:: enum data_queue_qid

    Queue identification

.. _`data_queue_qid.definition`:

Definition
----------

.. code-block:: c

    enum data_queue_qid {
        QID_AC_VO,
        QID_AC_VI,
        QID_AC_BE,
        QID_AC_BK,
        QID_HCCA,
        QID_MGMT,
        QID_RX,
        QID_OTHER,
        QID_BEACON,
        QID_ATIM
    };

.. _`data_queue_qid.constants`:

Constants
---------

QID_AC_VO
    AC VO queue

QID_AC_VI
    AC VI queue

QID_AC_BE
    AC BE queue

QID_AC_BK
    AC BK queue

QID_HCCA
    HCCA queue

QID_MGMT
    MGMT queue (prio queue)

QID_RX
    RX queue

QID_OTHER
    None of the above (don't use, only present for completeness)

QID_BEACON
    Beacon queue (value unspecified, don't send it to device)

QID_ATIM
    Atim queue (value unspecified, don't send it to device)

.. _`skb_frame_desc_flags`:

enum skb_frame_desc_flags
=========================

.. c:type:: enum skb_frame_desc_flags

    Flags for \ :c:type:`struct skb_frame_desc <skb_frame_desc>`\ 

.. _`skb_frame_desc_flags.definition`:

Definition
----------

.. code-block:: c

    enum skb_frame_desc_flags {
        SKBDESC_DMA_MAPPED_RX,
        SKBDESC_DMA_MAPPED_TX,
        SKBDESC_IV_STRIPPED,
        SKBDESC_NOT_MAC80211,
        SKBDESC_DESC_IN_SKB
    };

.. _`skb_frame_desc_flags.constants`:

Constants
---------

SKBDESC_DMA_MAPPED_RX
    &skb_dma field has been mapped for RX

SKBDESC_DMA_MAPPED_TX
    &skb_dma field has been mapped for TX

SKBDESC_IV_STRIPPED
    Frame contained a IV/EIV provided by
    mac80211 but was stripped for processing by the driver.

SKBDESC_NOT_MAC80211
    Frame didn't originate from mac80211,
    don't try to pass it back.

SKBDESC_DESC_IN_SKB
    The descriptor is at the start of the
    skb, instead of in the desc field.

.. _`skb_frame_desc`:

struct skb_frame_desc
=====================

.. c:type:: struct skb_frame_desc

    Descriptor information for the skb buffer

.. _`skb_frame_desc.definition`:

Definition
----------

.. code-block:: c

    struct skb_frame_desc {
        u8 flags;
        u8 desc_len;
        u8 tx_rate_idx;
        u8 tx_rate_flags;
        void *desc;
        __le32 iv[2];
        dma_addr_t skb_dma;
        struct queue_entry *entry;
    }

.. _`skb_frame_desc.members`:

Members
-------

flags
    Frame flags, see \ :c:type:`enum skb_frame_desc_flags <skb_frame_desc_flags>`\ .

desc_len
    Length of the frame descriptor.

tx_rate_idx
    the index of the TX rate, used for TX status reporting

tx_rate_flags
    the TX rate flags, used for TX status reporting

desc
    Pointer to descriptor part of the frame.
    Note that this pointer could point to something outside
    of the scope of the skb->data pointer.

iv
    IV/EIV data used during encryption/decryption.

skb_dma
    (PCI-only) the DMA address associated with the sk buffer.

entry
    The entry to which this sk buffer belongs.

.. _`skb_frame_desc.description`:

Description
-----------

This structure is placed over the driver_data array, this means that
this structure should not exceed the size of that array (40 bytes).

.. _`get_skb_frame_desc`:

get_skb_frame_desc
==================

.. c:function:: struct skb_frame_desc*get_skb_frame_desc(struct sk_buff *skb)

    Obtain the rt2x00 frame descriptor from a sk_buff.

    :param struct sk_buff \*skb:
        &struct sk_buff from where we obtain the \ :c:type:`struct skb_frame_desc <skb_frame_desc>`\ 

.. _`rxdone_entry_desc_flags`:

enum rxdone_entry_desc_flags
============================

.. c:type:: enum rxdone_entry_desc_flags

    Flags for \ :c:type:`struct rxdone_entry_desc <rxdone_entry_desc>`\ 

.. _`rxdone_entry_desc_flags.definition`:

Definition
----------

.. code-block:: c

    enum rxdone_entry_desc_flags {
        RXDONE_SIGNAL_PLCP,
        RXDONE_SIGNAL_BITRATE,
        RXDONE_SIGNAL_MCS,
        RXDONE_MY_BSS,
        RXDONE_CRYPTO_IV,
        RXDONE_CRYPTO_ICV,
        RXDONE_L2PAD
    };

.. _`rxdone_entry_desc_flags.constants`:

Constants
---------

RXDONE_SIGNAL_PLCP
    Signal field contains the plcp value.

RXDONE_SIGNAL_BITRATE
    Signal field contains the bitrate value.

RXDONE_SIGNAL_MCS
    Signal field contains the mcs value.

RXDONE_MY_BSS
    Does this frame originate from device's BSS.

RXDONE_CRYPTO_IV
    Driver provided IV/EIV data.

RXDONE_CRYPTO_ICV
    Driver provided ICV data.

RXDONE_L2PAD
    802.11 payload has been padded to 4-byte boundary.

.. _`rxdone_signal_mask`:

RXDONE_SIGNAL_MASK
==================

.. c:function::  RXDONE_SIGNAL_MASK()

    Define to mask off all \ :c:type:`struct rxdone_entry_desc_flags <rxdone_entry_desc_flags>`\  flags except for the RXDONE_SIGNAL\_\* flags. This is useful to convert the dev_flags from \ :c:type:`struct rxdone_entry_desc <rxdone_entry_desc>`\  to a signal value type.

.. _`rxdone_entry_desc`:

struct rxdone_entry_desc
========================

.. c:type:: struct rxdone_entry_desc

    RX Entry descriptor

.. _`rxdone_entry_desc.definition`:

Definition
----------

.. code-block:: c

    struct rxdone_entry_desc {
        u64 timestamp;
        int signal;
        int rssi;
        int size;
        int flags;
        int dev_flags;
        u16 rate_mode;
        u8 cipher;
        u8 cipher_status;
        __le32 iv[2];
        __le32 icv;
    }

.. _`rxdone_entry_desc.members`:

Members
-------

timestamp
    RX Timestamp

signal
    Signal of the received frame.

rssi
    RSSI of the received frame.

size
    Data size of the received frame.

flags
    MAC80211 receive flags (See \ :c:type:`enum mac80211_rx_flags <mac80211_rx_flags>`\ ).

dev_flags
    Ralink receive flags (See \ :c:type:`enum rxdone_entry_desc_flags <rxdone_entry_desc_flags>`\ ).

rate_mode
    Rate mode (See \ ``enum``\  rate_modulation).

cipher
    Cipher type used during decryption.

cipher_status
    Decryption status.

iv
    IV/EIV data used during decryption.

icv
    ICV data used during decryption.

.. _`rxdone_entry_desc.description`:

Description
-----------

Summary of information that has been read from the RX frame descriptor.

.. _`txdone_entry_desc_flags`:

enum txdone_entry_desc_flags
============================

.. c:type:: enum txdone_entry_desc_flags

    Flags for \ :c:type:`struct txdone_entry_desc <txdone_entry_desc>`\ 

.. _`txdone_entry_desc_flags.definition`:

Definition
----------

.. code-block:: c

    enum txdone_entry_desc_flags {
        TXDONE_UNKNOWN,
        TXDONE_SUCCESS,
        TXDONE_FALLBACK,
        TXDONE_FAILURE,
        TXDONE_EXCESSIVE_RETRY,
        TXDONE_AMPDU
    };

.. _`txdone_entry_desc_flags.constants`:

Constants
---------

TXDONE_UNKNOWN
    Hardware could not determine success of transmission.

TXDONE_SUCCESS
    Frame was successfully send

TXDONE_FALLBACK
    Hardware used fallback rates for retries

TXDONE_FAILURE
    Frame was not successfully send

TXDONE_EXCESSIVE_RETRY
    In addition to \ :c:type:`struct TXDONE_FAILURE <TXDONE_FAILURE>`\ , the
    frame transmission failed due to excessive retries.

TXDONE_AMPDU
    *undescribed*

.. _`txdone_entry_desc_flags.description`:

Description
-----------

Every txdone report has to contain the basic result of the
transmission, either \ :c:type:`struct TXDONE_UNKNOWN <TXDONE_UNKNOWN>`\ , \ :c:type:`struct TXDONE_SUCCESS <TXDONE_SUCCESS>`\  or
\ :c:type:`struct TXDONE_FAILURE <TXDONE_FAILURE>`\ . The flag \ :c:type:`struct TXDONE_FALLBACK <TXDONE_FALLBACK>`\  can be used in
conjunction with all of these flags but should only be set
if retires > 0. The flag \ :c:type:`struct TXDONE_EXCESSIVE_RETRY <TXDONE_EXCESSIVE_RETRY>`\  can only be used
in conjunction with \ :c:type:`struct TXDONE_FAILURE <TXDONE_FAILURE>`\ .

.. _`txdone_entry_desc`:

struct txdone_entry_desc
========================

.. c:type:: struct txdone_entry_desc

    TX done entry descriptor

.. _`txdone_entry_desc.definition`:

Definition
----------

.. code-block:: c

    struct txdone_entry_desc {
        unsigned long flags;
        int retry;
    }

.. _`txdone_entry_desc.members`:

Members
-------

flags
    TX done flags (See \ :c:type:`enum txdone_entry_desc_flags <txdone_entry_desc_flags>`\ ).

retry
    Retry count.

.. _`txdone_entry_desc.description`:

Description
-----------

Summary of information that has been read from the TX frame descriptor
after the device is done with transmission.

.. _`txentry_desc_flags`:

enum txentry_desc_flags
=======================

.. c:type:: enum txentry_desc_flags

    Status flags for TX entry descriptor

.. _`txentry_desc_flags.definition`:

Definition
----------

.. code-block:: c

    enum txentry_desc_flags {
        ENTRY_TXD_RTS_FRAME,
        ENTRY_TXD_CTS_FRAME,
        ENTRY_TXD_GENERATE_SEQ,
        ENTRY_TXD_FIRST_FRAGMENT,
        ENTRY_TXD_MORE_FRAG,
        ENTRY_TXD_REQ_TIMESTAMP,
        ENTRY_TXD_BURST,
        ENTRY_TXD_ACK,
        ENTRY_TXD_RETRY_MODE,
        ENTRY_TXD_ENCRYPT,
        ENTRY_TXD_ENCRYPT_PAIRWISE,
        ENTRY_TXD_ENCRYPT_IV,
        ENTRY_TXD_ENCRYPT_MMIC,
        ENTRY_TXD_HT_AMPDU,
        ENTRY_TXD_HT_BW_40,
        ENTRY_TXD_HT_SHORT_GI,
        ENTRY_TXD_HT_MIMO_PS
    };

.. _`txentry_desc_flags.constants`:

Constants
---------

ENTRY_TXD_RTS_FRAME
    This frame is a RTS frame.

ENTRY_TXD_CTS_FRAME
    This frame is a CTS-to-self frame.

ENTRY_TXD_GENERATE_SEQ
    This frame requires sequence counter.

ENTRY_TXD_FIRST_FRAGMENT
    This is the first frame.

ENTRY_TXD_MORE_FRAG
    This frame is followed by another fragment.

ENTRY_TXD_REQ_TIMESTAMP
    Require timestamp to be inserted.

ENTRY_TXD_BURST
    This frame belongs to the same burst event.

ENTRY_TXD_ACK
    An ACK is required for this frame.

ENTRY_TXD_RETRY_MODE
    When set, the long retry count is used.

ENTRY_TXD_ENCRYPT
    This frame should be encrypted.

ENTRY_TXD_ENCRYPT_PAIRWISE
    Use pairwise key table (instead of shared).

ENTRY_TXD_ENCRYPT_IV
    Generate IV/EIV in hardware.

ENTRY_TXD_ENCRYPT_MMIC
    Generate MIC in hardware.

ENTRY_TXD_HT_AMPDU
    This frame is part of an AMPDU.

ENTRY_TXD_HT_BW_40
    Use 40MHz Bandwidth.

ENTRY_TXD_HT_SHORT_GI
    Use short GI.

ENTRY_TXD_HT_MIMO_PS
    The receiving STA is in dynamic SM PS mode.

.. _`txentry_desc`:

struct txentry_desc
===================

.. c:type:: struct txentry_desc

    TX Entry descriptor

.. _`txentry_desc.definition`:

Definition
----------

.. code-block:: c

    struct txentry_desc {
        unsigned long flags;
        u16 length;
        u16 header_length;
        union u;
        enum rate_modulation rate_mode;
        short retry_limit;
        enum cipher cipher;
        u16 key_idx;
        u16 iv_offset;
        u16 iv_len;
    }

.. _`txentry_desc.members`:

Members
-------

flags
    Descriptor flags (See \ :c:type:`enum queue_entry_flags <queue_entry_flags>`\ ).

length
    Length of the entire frame.

header_length
    Length of 802.11 header.

u
    *undescribed*

rate_mode
    Rate mode (See \ ``enum``\  rate_modulation).

retry_limit
    Max number of retries.

cipher
    Cipher type used for encryption.

key_idx
    Key index used for encryption.

iv_offset
    Position where IV should be inserted by hardware.

iv_len
    Length of IV data.

.. _`txentry_desc.description`:

Description
-----------

Summary of information for the frame descriptor before sending a TX frame.

.. _`queue_entry_flags`:

enum queue_entry_flags
======================

.. c:type:: enum queue_entry_flags

    Status flags for queue entry

.. _`queue_entry_flags.definition`:

Definition
----------

.. code-block:: c

    enum queue_entry_flags {
        ENTRY_BCN_ASSIGNED,
        ENTRY_BCN_ENABLED,
        ENTRY_OWNER_DEVICE_DATA,
        ENTRY_DATA_PENDING,
        ENTRY_DATA_IO_FAILED,
        ENTRY_DATA_STATUS_PENDING,
        ENTRY_DATA_STATUS_SET
    };

.. _`queue_entry_flags.constants`:

Constants
---------

ENTRY_BCN_ASSIGNED
    This entry has been assigned to an interface.
    As long as this bit is set, this entry may only be touched
    through the interface structure.

ENTRY_BCN_ENABLED
    *undescribed*

ENTRY_OWNER_DEVICE_DATA
    This entry is owned by the device for data
    transfer (either TX or RX depending on the queue). The entry should
    only be touched after the device has signaled it is done with it.

ENTRY_DATA_PENDING
    This entry contains a valid frame and is waiting
    for the signal to start sending.

ENTRY_DATA_IO_FAILED
    Hardware indicated that an IO error occurred
    while transferring the data to the hardware. No TX status report will
    be expected from the hardware.

ENTRY_DATA_STATUS_PENDING
    The entry has been send to the device and
    returned. It is now waiting for the status reporting before the
    entry can be reused again.

ENTRY_DATA_STATUS_SET
    *undescribed*

.. _`queue_entry`:

struct queue_entry
==================

.. c:type:: struct queue_entry

    Entry inside the \ :c:type:`struct data_queue <data_queue>`\ 

.. _`queue_entry.definition`:

Definition
----------

.. code-block:: c

    struct queue_entry {
        unsigned long flags;
        unsigned long last_action;
        struct data_queue *queue;
        struct sk_buff *skb;
        unsigned int entry_idx;
        u32 status;
        void *priv_data;
    }

.. _`queue_entry.members`:

Members
-------

flags
    Entry flags, see \ :c:type:`enum queue_entry_flags <queue_entry_flags>`\ .

last_action
    Timestamp of last change.

queue
    The data queue (&struct data_queue) to which this entry belongs.

skb
    The buffer which is currently being transmitted (for TX queue),
    or used to directly receive data in (for RX queue).

entry_idx
    The entry index number.

status
    Device specific status

priv_data
    Private data belonging to this queue entry. The pointer
    points to data specific to a particular driver and queue type.

.. _`queue_index`:

enum queue_index
================

.. c:type:: enum queue_index

    Queue index type

.. _`queue_index.definition`:

Definition
----------

.. code-block:: c

    enum queue_index {
        Q_INDEX,
        Q_INDEX_DMA_DONE,
        Q_INDEX_DONE,
        Q_INDEX_MAX
    };

.. _`queue_index.constants`:

Constants
---------

Q_INDEX
    Index pointer to the current entry in the queue, if this entry is
    owned by the hardware then the queue is considered to be full.

Q_INDEX_DMA_DONE
    Index pointer for the next entry which will have been
    transferred to the hardware.

Q_INDEX_DONE
    Index pointer to the next entry which will be completed by
    the hardware and for which we need to run the txdone handler. If this
    entry is not owned by the hardware the queue is considered to be empty.

Q_INDEX_MAX
    Keep last, used in \ :c:type:`struct data_queue <data_queue>`\  to determine the size
    of the index array.

.. _`data_queue_flags`:

enum data_queue_flags
=====================

.. c:type:: enum data_queue_flags

    Status flags for data queues

.. _`data_queue_flags.definition`:

Definition
----------

.. code-block:: c

    enum data_queue_flags {
        QUEUE_STARTED,
        QUEUE_PAUSED
    };

.. _`data_queue_flags.constants`:

Constants
---------

QUEUE_STARTED
    The queue has been started. Fox RX queues this means the
    device might be DMA'ing skbuffers. TX queues will accept skbuffers to
    be transmitted and beacon queues will start beaconing the configured
    beacons.

QUEUE_PAUSED
    The queue has been started but is currently paused.
    When this bit is set, the queue has been stopped in mac80211,
    preventing new frames to be enqueued. However, a few frames
    might still appear shortly after the pausing...

.. _`data_queue`:

struct data_queue
=================

.. c:type:: struct data_queue

    Data queue

.. _`data_queue.definition`:

Definition
----------

.. code-block:: c

    struct data_queue {
        struct rt2x00_dev *rt2x00dev;
        struct queue_entry *entries;
        enum data_queue_qid qid;
        unsigned long flags;
        struct mutex status_lock;
        spinlock_t tx_lock;
        spinlock_t index_lock;
        unsigned int count;
        unsigned short limit;
        unsigned short threshold;
        unsigned short length;
        unsigned short index[Q_INDEX_MAX];
        unsigned short txop;
        unsigned short aifs;
        unsigned short cw_min;
        unsigned short cw_max;
        unsigned short data_size;
        unsigned char desc_size;
        unsigned char winfo_size;
        unsigned short priv_size;
        unsigned short usb_endpoint;
        unsigned short usb_maxpacket;
    }

.. _`data_queue.members`:

Members
-------

rt2x00dev
    Pointer to main \ :c:type:`struct rt2x00dev <rt2x00dev>`\  where this queue belongs to.

entries
    Base address of the \ :c:type:`struct queue_entry <queue_entry>`\  which are
    part of this queue.

qid
    The queue identification, see \ :c:type:`enum data_queue_qid <data_queue_qid>`\ .

flags
    Entry flags, see \ :c:type:`enum queue_entry_flags <queue_entry_flags>`\ .

status_lock
    The mutex for protecting the start/stop/flush
    handling on this queue.

tx_lock
    Spinlock to serialize tx operations on this queue.

index_lock
    Spinlock to protect index handling. Whenever \ ``index``\ , \ ``index_done``\  or
    \ ``index_crypt``\  needs to be changed this lock should be grabbed to prevent
    index corruption due to concurrency.

count
    Number of frames handled in the queue.

limit
    Maximum number of entries in the queue.

threshold
    Minimum number of free entries before queue is kicked by force.

length
    Number of frames in queue.

index
    Index pointers to entry positions in the queue,
    use \ :c:type:`enum queue_index <queue_index>`\  to get a specific index field.

txop
    maximum burst time.

aifs
    The aifs value for outgoing frames (field ignored in RX queue).

cw_min
    The cw min value for outgoing frames (field ignored in RX queue).

cw_max
    The cw max value for outgoing frames (field ignored in RX queue).

data_size
    Maximum data size for the frames in this queue.

desc_size
    Hardware descriptor size for the data in this queue.

winfo_size
    *undescribed*

priv_size
    Size of per-queue_entry private data.

usb_endpoint
    Device endpoint used for communication (USB only)

usb_maxpacket
    Max packet size for given endpoint (USB only)

.. _`queue_end`:

queue_end
=========

.. c:function::  queue_end( __dev)

    Return pointer to the last queue (HELPER MACRO).

    :param  __dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

.. _`queue_end.description`:

Description
-----------

Using the base rx pointer and the maximum number of available queues,
this macro will return the address of 1 position beyond  the end of the
queues array.

.. _`tx_queue_end`:

tx_queue_end
============

.. c:function::  tx_queue_end( __dev)

    Return pointer to the last TX queue (HELPER MACRO).

    :param  __dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

.. _`tx_queue_end.description`:

Description
-----------

Using the base tx pointer and the maximum number of available TX
queues, this macro will return the address of 1 position beyond
the end of the TX queue array.

.. _`queue_next`:

queue_next
==========

.. c:function::  queue_next( __queue)

    Return pointer to next queue in list (HELPER MACRO).

    :param  __queue:
        Current queue for which we need the next queue

.. _`queue_next.description`:

Description
-----------

Using the current queue address we take the address directly
after the queue to take the next queue. Note that this macro
should be used carefully since it does not protect against
moving past the end of the list. (See macros \ :c:type:`struct queue_end <queue_end>`\  and
\ :c:type:`struct tx_queue_end <tx_queue_end>`\  for determining the end of the queue).

.. _`queue_loop`:

queue_loop
==========

.. c:function::  queue_loop( __entry,  __start,  __end)

    Loop through the queues within a specific range (HELPER MACRO).

    :param  __entry:
        Pointer where the current queue entry will be stored in.

    :param  __start:
        Start queue pointer.

    :param  __end:
        End queue pointer.

.. _`queue_loop.description`:

Description
-----------

This macro will loop through all queues between \ :c:type:`struct __start <__start>`\  and \ :c:type:`struct __end <__end>`\ .

.. _`queue_for_each`:

queue_for_each
==============

.. c:function::  queue_for_each( __dev,  __entry)

    Loop through all queues

    :param  __dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param  __entry:
        Pointer where the current queue entry will be stored in.

.. _`queue_for_each.description`:

Description
-----------

This macro will loop through all available queues.

.. _`tx_queue_for_each`:

tx_queue_for_each
=================

.. c:function::  tx_queue_for_each( __dev,  __entry)

    Loop through the TX queues

    :param  __dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param  __entry:
        Pointer where the current queue entry will be stored in.

.. _`tx_queue_for_each.description`:

Description
-----------

This macro will loop through all TX related queues excluding
the Beacon and Atim queues.

.. _`txall_queue_for_each`:

txall_queue_for_each
====================

.. c:function::  txall_queue_for_each( __dev,  __entry)

    Loop through all TX related queues

    :param  __dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param  __entry:
        Pointer where the current queue entry will be stored in.

.. _`txall_queue_for_each.description`:

Description
-----------

This macro will loop through all TX related queues including
the Beacon and Atim queues.

.. _`rt2x00queue_for_each_entry`:

rt2x00queue_for_each_entry
==========================

.. c:function:: bool rt2x00queue_for_each_entry(struct data_queue *queue, enum queue_index start, enum queue_index end, void *data, bool (*fn)(struct queue_entry *entry, void *data))

    Loop through all entries in the queue

    :param struct data_queue \*queue:
        Pointer to \ ``data_queue``\ 

    :param enum queue_index start:
        &enum queue_index Pointer to start index

    :param enum queue_index end:
        &enum queue_index Pointer to end index

    :param void \*data:
        Data to pass to the callback function

    :param bool (\*fn)(struct queue_entry \*entry, void \*data):
        The function to call for each \ :c:type:`struct queue_entry <queue_entry>`\ 

.. _`rt2x00queue_for_each_entry.description`:

Description
-----------

This will walk through all entries in the queue, in chronological
order. This means it will start at the current \ ``start``\  pointer
and will walk through the queue until it reaches the \ ``end``\  pointer.

If fn returns true for an entry rt2x00queue_for_each_entry will stop
processing and return true as well.

.. _`rt2x00queue_empty`:

rt2x00queue_empty
=================

.. c:function:: int rt2x00queue_empty(struct data_queue *queue)

    Check if the queue is empty.

    :param struct data_queue \*queue:
        Queue to check if empty.

.. _`rt2x00queue_full`:

rt2x00queue_full
================

.. c:function:: int rt2x00queue_full(struct data_queue *queue)

    Check if the queue is full.

    :param struct data_queue \*queue:
        Queue to check if full.

.. _`rt2x00queue_available`:

rt2x00queue_available
=====================

.. c:function:: int rt2x00queue_available(struct data_queue *queue)

    Check the number of available entries in queue.

    :param struct data_queue \*queue:
        Queue to check.

.. _`rt2x00queue_threshold`:

rt2x00queue_threshold
=====================

.. c:function:: int rt2x00queue_threshold(struct data_queue *queue)

    Check if the queue is below threshold

    :param struct data_queue \*queue:
        Queue to check.

.. _`rt2x00queue_dma_timeout`:

rt2x00queue_dma_timeout
=======================

.. c:function:: int rt2x00queue_dma_timeout(struct queue_entry *entry)

    Check if a timeout occurred for DMA transfers

    :param struct queue_entry \*entry:
        Queue entry to check.

.. _`_rt2x00_desc_read`:

_rt2x00_desc_read
=================

.. c:function:: void _rt2x00_desc_read(__le32 *desc, const u8 word, __le32 *value)

    Read a word from the hardware descriptor.

    :param __le32 \*desc:
        Base descriptor address

    :param const u8 word:
        Word index from where the descriptor should be read.

    :param __le32 \*value:
        Address where the descriptor value should be written into.

.. _`rt2x00_desc_read`:

rt2x00_desc_read
================

.. c:function:: void rt2x00_desc_read(__le32 *desc, const u8 word, u32 *value)

    Read a word from the hardware descriptor, this function will take care of the byte ordering.

    :param __le32 \*desc:
        Base descriptor address

    :param const u8 word:
        Word index from where the descriptor should be read.

    :param u32 \*value:
        Address where the descriptor value should be written into.

.. _`_rt2x00_desc_write`:

_rt2x00_desc_write
==================

.. c:function:: void _rt2x00_desc_write(__le32 *desc, const u8 word, __le32 value)

    write a word to the hardware descriptor, this function will take care of the byte ordering.

    :param __le32 \*desc:
        Base descriptor address

    :param const u8 word:
        Word index from where the descriptor should be written.

    :param __le32 value:
        Value that should be written into the descriptor.

.. _`rt2x00_desc_write`:

rt2x00_desc_write
=================

.. c:function:: void rt2x00_desc_write(__le32 *desc, const u8 word, u32 value)

    write a word to the hardware descriptor.

    :param __le32 \*desc:
        Base descriptor address

    :param const u8 word:
        Word index from where the descriptor should be written.

    :param u32 value:
        Value that should be written into the descriptor.

.. This file was automatic generated / don't edit.

