.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/ethtool.c

.. _`efx_fill_test`:

efx_fill_test
=============

.. c:function:: void efx_fill_test(unsigned int test_index, u8 *strings, u64 *data, int *test, const char *unit_format, int unit_id, const char *test_format, const char *test_id)

    fill in an individual self-test entry

    :param unsigned int test_index:
        Index of the test

    :param u8 \*strings:
        Ethtool strings, or \ ``NULL``\ 

    :param u64 \*data:
        Ethtool test results, or \ ``NULL``\ 

    :param int \*test:
        Pointer to test result (used only if data != \ ``NULL``\ )

    :param const char \*unit_format:
        Unit name format (e.g. "chan%d")

    :param int unit_id:
        Unit id (e.g. 0 for "chan0")

    :param const char \*test_format:
        Test name format (e.g. "loopback.%s.tx.sent")

    :param const char \*test_id:
        Test id (e.g. "PHYXS" for "loopback.PHYXS.tx_sent")

.. _`efx_fill_test.description`:

Description
-----------

Fill in an individual self-test entry.

.. _`efx_fill_loopback_test`:

efx_fill_loopback_test
======================

.. c:function:: int efx_fill_loopback_test(struct efx_nic *efx, struct efx_loopback_self_tests *lb_tests, enum efx_loopback_mode mode, unsigned int test_index, u8 *strings, u64 *data)

    fill in a block of loopback self-test entries

    :param struct efx_nic \*efx:
        Efx NIC

    :param struct efx_loopback_self_tests \*lb_tests:
        Efx loopback self-test results structure

    :param enum efx_loopback_mode mode:
        Loopback test mode

    :param unsigned int test_index:
        Starting index of the test

    :param u8 \*strings:
        Ethtool strings, or \ ``NULL``\ 

    :param u64 \*data:
        Ethtool test results, or \ ``NULL``\ 

.. _`efx_fill_loopback_test.description`:

Description
-----------

Fill in a block of loopback self-test entries.  Return new test
index.

.. _`efx_ethtool_fill_self_tests`:

efx_ethtool_fill_self_tests
===========================

.. c:function:: int efx_ethtool_fill_self_tests(struct efx_nic *efx, struct efx_self_tests *tests, u8 *strings, u64 *data)

    get self-test details

    :param struct efx_nic \*efx:
        Efx NIC

    :param struct efx_self_tests \*tests:
        Efx self-test results structure, or \ ``NULL``\ 

    :param u8 \*strings:
        Ethtool strings, or \ ``NULL``\ 

    :param u64 \*data:
        Ethtool test results, or \ ``NULL``\ 

.. _`efx_ethtool_fill_self_tests.description`:

Description
-----------

Get self-test number of strings, strings, and/or test results.
Return number of strings (== number of test results).

The reason for merging these three functions is to make sure that
they can never be inconsistent.

.. This file was automatic generated / don't edit.
