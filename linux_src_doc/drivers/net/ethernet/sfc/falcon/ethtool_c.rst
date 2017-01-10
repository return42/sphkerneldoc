.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/ethtool.c

.. _`ef4_fill_test`:

ef4_fill_test
=============

.. c:function:: void ef4_fill_test(unsigned int test_index, u8 *strings, u64 *data, int *test, const char *unit_format, int unit_id, const char *test_format, const char *test_id)

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

.. _`ef4_fill_test.description`:

Description
-----------

Fill in an individual self-test entry.

.. _`ef4_fill_loopback_test`:

ef4_fill_loopback_test
======================

.. c:function:: int ef4_fill_loopback_test(struct ef4_nic *efx, struct ef4_loopback_self_tests *lb_tests, enum ef4_loopback_mode mode, unsigned int test_index, u8 *strings, u64 *data)

    fill in a block of loopback self-test entries

    :param struct ef4_nic \*efx:
        Efx NIC

    :param struct ef4_loopback_self_tests \*lb_tests:
        Efx loopback self-test results structure

    :param enum ef4_loopback_mode mode:
        Loopback test mode

    :param unsigned int test_index:
        Starting index of the test

    :param u8 \*strings:
        Ethtool strings, or \ ``NULL``\ 

    :param u64 \*data:
        Ethtool test results, or \ ``NULL``\ 

.. _`ef4_fill_loopback_test.description`:

Description
-----------

Fill in a block of loopback self-test entries.  Return new test
index.

.. _`ef4_ethtool_fill_self_tests`:

ef4_ethtool_fill_self_tests
===========================

.. c:function:: int ef4_ethtool_fill_self_tests(struct ef4_nic *efx, struct ef4_self_tests *tests, u8 *strings, u64 *data)

    get self-test details

    :param struct ef4_nic \*efx:
        Efx NIC

    :param struct ef4_self_tests \*tests:
        Efx self-test results structure, or \ ``NULL``\ 

    :param u8 \*strings:
        Ethtool strings, or \ ``NULL``\ 

    :param u64 \*data:
        Ethtool test results, or \ ``NULL``\ 

.. _`ef4_ethtool_fill_self_tests.description`:

Description
-----------

Get self-test number of strings, strings, and/or test results.
Return number of strings (== number of test results).

The reason for merging these three functions is to make sure that
they can never be inconsistent.

.. This file was automatic generated / don't edit.

