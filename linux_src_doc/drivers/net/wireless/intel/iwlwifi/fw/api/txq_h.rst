.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/txq.h

.. _`iwl_tx_queue_cfg_actions`:

enum iwl_tx_queue_cfg_actions
=============================

.. c:type:: enum iwl_tx_queue_cfg_actions

    TXQ config options

.. _`iwl_tx_queue_cfg_actions.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tx_queue_cfg_actions {
        TX_QUEUE_CFG_ENABLE_QUEUE,
        TX_QUEUE_CFG_TFD_SHORT_FORMAT
    };

.. _`iwl_tx_queue_cfg_actions.constants`:

Constants
---------

TX_QUEUE_CFG_ENABLE_QUEUE
    enable a queue

TX_QUEUE_CFG_TFD_SHORT_FORMAT
    use short TFD format

.. _`iwl_tx_queue_cfg_cmd`:

struct iwl_tx_queue_cfg_cmd
===========================

.. c:type:: struct iwl_tx_queue_cfg_cmd

    txq hw scheduler config command

.. _`iwl_tx_queue_cfg_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tx_queue_cfg_cmd {
        u8 sta_id;
        u8 tid;
        __le16 flags;
        __le32 cb_size;
        __le64 byte_cnt_addr;
        __le64 tfdq_addr;
    }

.. _`iwl_tx_queue_cfg_cmd.members`:

Members
-------

sta_id
    station id

tid
    tid of the queue

flags
    see \ :c:type:`enum iwl_tx_queue_cfg_actions <iwl_tx_queue_cfg_actions>`\ 

cb_size
    size of TFD cyclic buffer. Value is exponent - 3.
    Minimum value 0 (8 TFDs), maximum value 5 (256 TFDs)

byte_cnt_addr
    address of byte count table

tfdq_addr
    address of TFD circular buffer

.. _`iwl_tx_queue_cfg_rsp`:

struct iwl_tx_queue_cfg_rsp
===========================

.. c:type:: struct iwl_tx_queue_cfg_rsp

    response to txq hw scheduler config

.. _`iwl_tx_queue_cfg_rsp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tx_queue_cfg_rsp {
        __le16 queue_number;
        __le16 flags;
        __le16 write_pointer;
        __le16 reserved;
    }

.. _`iwl_tx_queue_cfg_rsp.members`:

Members
-------

queue_number
    queue number assigned to this RA -TID

flags
    set on failure

write_pointer
    initial value for write pointer

reserved
    reserved

.. This file was automatic generated / don't edit.

