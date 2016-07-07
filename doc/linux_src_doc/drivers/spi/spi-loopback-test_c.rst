.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-loopback-test.c

.. _`spi_test_execute_msg`:

spi_test_execute_msg
====================

.. c:function:: int spi_test_execute_msg(struct spi_device *spi, struct spi_test *test, void *tx, void *rx)

    default implementation to run a test

    :param struct spi_device \*spi:
        *undescribed*

    :param struct spi_test \*test:
        *undescribed*

    :param void \*tx:
        *undescribed*

    :param void \*rx:
        *undescribed*

.. _`spi_test_execute_msg.spi`:

spi
---

\ ``spi_device``\  on which to run the \ ``spi_message``\ 

.. _`spi_test_execute_msg.test`:

test
----

the test to execute, which already contains \ ``msg``\ 
tx:   the tx buffer allocated for the test sequence
rx:   the rx buffer allocated for the test sequence

.. _`spi_test_execute_msg.return`:

Return
------

error code of spi_sync as well as basic error checking

.. _`spi_test_run_test`:

spi_test_run_test
=================

.. c:function:: int spi_test_run_test(struct spi_device *spi, const struct spi_test *test, void *tx, void *rx)

    run an individual spi_test including all the relevant iterations on: length and buffer alignment

    :param struct spi_device \*spi:
        *undescribed*

    :param const struct spi_test \*test:
        *undescribed*

    :param void \*tx:
        *undescribed*

    :param void \*rx:
        *undescribed*

.. _`spi_test_run_test.spi`:

spi
---

the spi_device to send the messages to

.. _`spi_test_run_test.test`:

test
----

the test which we need to execute
tx:   the tx buffer allocated for the test sequence
rx:   the rx buffer allocated for the test sequence

.. _`spi_test_run_test.return`:

Return
------

status code of spi_sync or other failures

.. _`spi_test_run_tests`:

spi_test_run_tests
==================

.. c:function:: int spi_test_run_tests(struct spi_device *spi, struct spi_test *tests)

    run an array of spi_messages tests

    :param struct spi_device \*spi:
        the spi device on which to run the tests

    :param struct spi_test \*tests:
        NULL-terminated array of \ ``spi_test``\ 

.. _`spi_test_run_tests.return`:

Return
------

status errors as per @\ :c:func:`spi_test_run_test`\ 

.. This file was automatic generated / don't edit.

