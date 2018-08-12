.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-test.h

.. _`spi_test`:

struct spi_test
===============

.. c:type:: struct spi_test

    describes a specific (set of) tests to execute

.. _`spi_test.definition`:

Definition
----------

.. code-block:: c

    struct spi_test {
        char description[64];
        struct spi_message msg;
        struct spi_transfer transfers[SPI_TEST_MAX_TRANSFERS];
        unsigned int transfer_count;
        int (*run_test)(struct spi_device *spi, struct spi_test *test, void *tx, void *rx);
        int (*execute_msg)(struct spi_device *spi, struct spi_test *test, void *tx, void *rx);
        int expected_return;
        int iterate_len[SPI_TEST_MAX_ITERATE];
        int iterate_tx_align;
        int iterate_rx_align;
        u32 iterate_transfer_mask;
        u32 fill_option;
    #define FILL_MEMSET_8 0
    #define FILL_MEMSET_16 1
    #define FILL_MEMSET_24 2
    #define FILL_MEMSET_32 3
    #define FILL_COUNT_8 4
    #define FILL_COUNT_16 5
    #define FILL_COUNT_24 6
    #define FILL_COUNT_32 7
    #define FILL_TRANSFER_BYTE_8 8
    #define FILL_TRANSFER_BYTE_16 9
    #define FILL_TRANSFER_BYTE_24 10
    #define FILL_TRANSFER_BYTE_32 11
    #define FILL_TRANSFER_NUM 16
        u32 fill_pattern;
        unsigned long long elapsed_time;
    }

.. _`spi_test.members`:

Members
-------

description
    description of the test

msg
    a template \ ``spi_message``\  usedfor the default settings

transfers
    array of \ ``spi_transfers``\  that are part of the
    resulting spi_message.

transfer_count
    number of transfers

run_test
    run a specific spi_test - this allows to override
    the default implementation of \ ``spi_test_run_transfer``\ 
    either to add some custom filters for a specific test
    or to effectively run some very custom tests...

execute_msg
    run the spi_message for real - this allows to override
    \ ``spi_test_execute_msg``\  to apply final modifications
    on the spi_message

expected_return
    the expected return code - in some cases we want to
    test also for error conditions

iterate_len
    list of length to iterate on

iterate_tx_align
    change the alignment of \ ``spi_transfer.tx_buf``\ 
    for all values in the below range if set.
    the ranges are:
    [0 : \ ``spi_master.dma_alignment``\ [ if set
    [0 : iterate_tx_align[ if unset

iterate_rx_align
    change the alignment of \ ``spi_transfer.rx_buf``\ 
    see \ ``iterate_tx_align``\  for details

iterate_transfer_mask
    the bitmask of transfers to which the iterations
    apply - if 0, then it applies to all transfer

fill_option
    define the way how tx_buf is filled

fill_pattern
    fill pattern to apply to the tx_buf
    (used in some of the \ ``fill_options``\ )

elapsed_time
    elapsed time in nanoseconds

.. This file was automatic generated / don't edit.

