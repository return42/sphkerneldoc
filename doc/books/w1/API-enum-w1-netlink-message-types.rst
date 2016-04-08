
.. _API-enum-w1-netlink-message-types:

=============================
enum w1_netlink_message_types
=============================

*man enum w1_netlink_message_types(9)*

*4.6.0-rc1*

message type


Synopsis
========

.. code-block:: c

    enum w1_netlink_message_types {
      W1_SLAVE_ADD,
      W1_SLAVE_REMOVE,
      W1_MASTER_ADD,
      W1_MASTER_REMOVE,
      W1_MASTER_CMD,
      W1_SLAVE_CMD,
      W1_LIST_MASTERS
    };


Constants
=========

W1_SLAVE_ADD
    notification that a slave device was added

W1_SLAVE_REMOVE
    notification that a slave device was removed

W1_MASTER_ADD
    notification that a new bus master was added

W1_MASTER_REMOVE
    notification that a bus masterwas removed

W1_MASTER_CMD
    initiate operations on a specific master

W1_SLAVE_CMD
    sends reset, selects the slave, then does a read/write/touch operation

W1_LIST_MASTERS
    used to determine the bus master identifiers
