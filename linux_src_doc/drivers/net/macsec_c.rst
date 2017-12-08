.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/macsec.c

.. _`macsec_key`:

struct macsec_key
=================

.. c:type:: struct macsec_key

    SA key

.. _`macsec_key.definition`:

Definition
----------

.. code-block:: c

    struct macsec_key {
        u8 id[MACSEC_KEYID_LEN];
        struct crypto_aead *tfm;
    }

.. _`macsec_key.members`:

Members
-------

id
    user-provided key identifier

tfm
    crypto struct, key storage

.. _`macsec_rx_sa`:

struct macsec_rx_sa
===================

.. c:type:: struct macsec_rx_sa

    receive secure association

.. _`macsec_rx_sa.definition`:

Definition
----------

.. code-block:: c

    struct macsec_rx_sa {
        struct macsec_key key;
        spinlock_t lock;
        u32 next_pn;
        refcount_t refcnt;
        bool active;
        struct macsec_rx_sa_stats __percpu *stats;
        struct macsec_rx_sc *sc;
        struct rcu_head rcu;
    }

.. _`macsec_rx_sa.members`:

Members
-------

key
    key structure

lock
    protects next_pn manipulations

next_pn
    packet number expected for the next packet

refcnt
    *undescribed*

active
    *undescribed*

stats
    per-SA stats

sc
    *undescribed*

rcu
    *undescribed*

.. _`macsec_rx_sc`:

struct macsec_rx_sc
===================

.. c:type:: struct macsec_rx_sc

    receive secure channel

.. _`macsec_rx_sc.definition`:

Definition
----------

.. code-block:: c

    struct macsec_rx_sc {
        struct macsec_rx_sc __rcu *next;
        sci_t sci;
        bool active;
        struct macsec_rx_sa __rcu *sa[MACSEC_NUM_AN];
        struct pcpu_rx_sc_stats __percpu *stats;
        refcount_t refcnt;
        struct rcu_head rcu_head;
    }

.. _`macsec_rx_sc.members`:

Members
-------

next
    *undescribed*

sci
    secure channel identifier for this SC

active
    channel is active

sa
    array of secure associations

stats
    per-SC stats

refcnt
    *undescribed*

rcu_head
    *undescribed*

.. _`macsec_tx_sa`:

struct macsec_tx_sa
===================

.. c:type:: struct macsec_tx_sa

    transmit secure association

.. _`macsec_tx_sa.definition`:

Definition
----------

.. code-block:: c

    struct macsec_tx_sa {
        struct macsec_key key;
        spinlock_t lock;
        u32 next_pn;
        refcount_t refcnt;
        bool active;
        struct macsec_tx_sa_stats __percpu *stats;
        struct rcu_head rcu;
    }

.. _`macsec_tx_sa.members`:

Members
-------

key
    key structure

lock
    protects next_pn manipulations

next_pn
    packet number to use for the next packet

refcnt
    *undescribed*

active
    *undescribed*

stats
    per-SA stats

rcu
    *undescribed*

.. _`macsec_tx_sc`:

struct macsec_tx_sc
===================

.. c:type:: struct macsec_tx_sc

    transmit secure channel

.. _`macsec_tx_sc.definition`:

Definition
----------

.. code-block:: c

    struct macsec_tx_sc {
        bool active;
        u8 encoding_sa;
        bool encrypt;
        bool send_sci;
        bool end_station;
        bool scb;
        struct macsec_tx_sa __rcu *sa[MACSEC_NUM_AN];
        struct pcpu_tx_sc_stats __percpu *stats;
    }

.. _`macsec_tx_sc.members`:

Members
-------

active
    *undescribed*

encoding_sa
    association number of the SA currently in use

encrypt
    encrypt packets on transmit, or authenticate only

send_sci
    always include the SCI in the SecTAG

end_station
    *undescribed*

scb
    single copy broadcast flag

sa
    array of secure associations

stats
    stats for this TXSC

.. _`macsec_secy`:

struct macsec_secy
==================

.. c:type:: struct macsec_secy

    MACsec Security Entity

.. _`macsec_secy.definition`:

Definition
----------

.. code-block:: c

    struct macsec_secy {
        struct net_device *netdev;
        unsigned int n_rx_sc;
        sci_t sci;
        u16 key_len;
        u16 icv_len;
        enum macsec_validation_type validate_frames;
        bool operational;
        bool protect_frames;
        bool replay_protect;
        u32 replay_window;
        struct macsec_tx_sc tx_sc;
        struct macsec_rx_sc __rcu *rx_sc;
    }

.. _`macsec_secy.members`:

Members
-------

netdev
    netdevice for this SecY

n_rx_sc
    number of receive secure channels configured on this SecY

sci
    secure channel identifier used for tx

key_len
    length of keys used by the cipher suite

icv_len
    length of ICV used by the cipher suite

validate_frames
    validation mode

operational
    MAC_Operational flag

protect_frames
    enable protection for this SecY

replay_protect
    enable packet number checks on receive

replay_window
    size of the replay window

tx_sc
    transmit secure channel

rx_sc
    linked list of receive secure channels

.. _`macsec_dev`:

struct macsec_dev
=================

.. c:type:: struct macsec_dev

    private data

.. _`macsec_dev.definition`:

Definition
----------

.. code-block:: c

    struct macsec_dev {
        struct macsec_secy secy;
        struct net_device *real_dev;
        struct pcpu_secy_stats __percpu *stats;
        struct list_head secys;
        struct gro_cells gro_cells;
        unsigned int nest_level;
    }

.. _`macsec_dev.members`:

Members
-------

secy
    SecY config

real_dev
    pointer to underlying netdevice

stats
    MACsec device stats

secys
    linked list of SecY's on the underlying device

gro_cells
    *undescribed*

nest_level
    *undescribed*

.. _`macsec_rxh_data`:

struct macsec_rxh_data
======================

.. c:type:: struct macsec_rxh_data

    rx_handler private argument

.. _`macsec_rxh_data.definition`:

Definition
----------

.. code-block:: c

    struct macsec_rxh_data {
        struct list_head secys;
    }

.. _`macsec_rxh_data.members`:

Members
-------

secys
    linked list of SecY's on this underlying device

.. This file was automatic generated / don't edit.

