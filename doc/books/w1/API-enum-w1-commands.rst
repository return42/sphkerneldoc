
.. _API-enum-w1-commands:

================
enum w1_commands
================

*man enum w1_commands(9)*

*4.6.0-rc1*

commands available for master or slave operations


Synopsis
========

.. code-block:: c

    enum w1_commands {
      W1_CMD_READ,
      W1_CMD_WRITE,
      W1_CMD_SEARCH,
      W1_CMD_ALARM_SEARCH,
      W1_CMD_TOUCH,
      W1_CMD_RESET,
      W1_CMD_SLAVE_ADD,
      W1_CMD_SLAVE_REMOVE,
      W1_CMD_LIST_SLAVES,
      W1_CMD_MAX
    };


Constants
=========

W1_CMD_READ
    read len bytes

W1_CMD_WRITE
    write len bytes

W1_CMD_SEARCH
    initiate a standard search, returns only the slave devices found during that search

W1_CMD_ALARM_SEARCH
    search for devices that are currently alarming

W1_CMD_TOUCH
    Touches a series of bytes.

W1_CMD_RESET
    sends a bus reset on the given master

W1_CMD_SLAVE_ADD
    adds a slave to the given master, 8 byte slave id at data[0]

W1_CMD_SLAVE_REMOVE
    removes a slave to the given master, 8 byte slave id at data[0]

W1_CMD_LIST_SLAVES
    list of slaves registered on this master

W1_CMD_MAX
    number of available commands
