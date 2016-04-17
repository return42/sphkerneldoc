.. -*- coding: utf-8; mode: rst -*-

==========
cvmx-spi.c
==========


.. _`cvmx_spi_get_callbacks`:

cvmx_spi_get_callbacks
======================

.. c:function:: void cvmx_spi_get_callbacks (cvmx_spi_callbacks_t *callbacks)

    :param cvmx_spi_callbacks_t \*callbacks:
        Pointer to the callbacks structure.to fill



.. _`cvmx_spi_get_callbacks.description`:

Description
-----------

Returns Pointer to cvmx_spi_callbacks_t structure.



.. _`cvmx_spi_set_callbacks`:

cvmx_spi_set_callbacks
======================

.. c:function:: void cvmx_spi_set_callbacks (cvmx_spi_callbacks_t *new_callbacks)

    :param cvmx_spi_callbacks_t \*new_callbacks:
        Pointer to an updated callbacks structure.



.. _`cvmx_spi_start_interface`:

cvmx_spi_start_interface
========================

.. c:function:: int cvmx_spi_start_interface (int interface, cvmx_spi_mode_t mode, int timeout, int num_ports)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).

    :param int timeout:
        Timeout to wait for clock synchronization in seconds

    :param int num_ports:
        Number of SPI ports to configure



.. _`cvmx_spi_start_interface.description`:

Description
-----------

Returns Zero on success, negative of failure.



.. _`cvmx_spi_restart_interface`:

cvmx_spi_restart_interface
==========================

.. c:function:: int cvmx_spi_restart_interface (int interface, cvmx_spi_mode_t mode, int timeout)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).

    :param int timeout:
        Timeout to wait for clock synchronization in seconds



.. _`cvmx_spi_restart_interface.description`:

Description
-----------

Returns Zero on success, negative of failure.



.. _`cvmx_spi_restart_interface.description`:

Description
-----------

Returns Zero on success, negative of failure.



.. _`cvmx_spi_reset_cb`:

cvmx_spi_reset_cb
=================

.. c:function:: int cvmx_spi_reset_cb (int interface, cvmx_spi_mode_t mode)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).



.. _`cvmx_spi_reset_cb.description`:

Description
-----------

Returns Zero on success, non-zero error code on failure (will cause
SPI initialization to abort)



.. _`cvmx_spi_calendar_setup_cb`:

cvmx_spi_calendar_setup_cb
==========================

.. c:function:: int cvmx_spi_calendar_setup_cb (int interface, cvmx_spi_mode_t mode, int num_ports)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).

    :param int num_ports:
        Number of ports to configure on SPI



.. _`cvmx_spi_calendar_setup_cb.description`:

Description
-----------

Returns Zero on success, non-zero error code on failure (will cause
SPI initialization to abort)



.. _`cvmx_spi_clock_detect_cb`:

cvmx_spi_clock_detect_cb
========================

.. c:function:: int cvmx_spi_clock_detect_cb (int interface, cvmx_spi_mode_t mode, int timeout)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).

    :param int timeout:
        Timeout to wait for clock synchronization in seconds



.. _`cvmx_spi_clock_detect_cb.description`:

Description
-----------

Returns Zero on success, non-zero error code on failure (will cause
SPI initialization to abort)



.. _`cvmx_spi_training_cb`:

cvmx_spi_training_cb
====================

.. c:function:: int cvmx_spi_training_cb (int interface, cvmx_spi_mode_t mode, int timeout)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).

    :param int timeout:
        Timeout to wait for link to be trained (in seconds)



.. _`cvmx_spi_training_cb.description`:

Description
-----------

Returns Zero on success, non-zero error code on failure (will cause
SPI initialization to abort)



.. _`cvmx_spi_calendar_sync_cb`:

cvmx_spi_calendar_sync_cb
=========================

.. c:function:: int cvmx_spi_calendar_sync_cb (int interface, cvmx_spi_mode_t mode, int timeout)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).

    :param int timeout:
        Timeout to wait for calendar data in seconds



.. _`cvmx_spi_calendar_sync_cb.description`:

Description
-----------

Returns Zero on success, non-zero error code on failure (will cause
SPI initialization to abort)



.. _`cvmx_spi_interface_up_cb`:

cvmx_spi_interface_up_cb
========================

.. c:function:: int cvmx_spi_interface_up_cb (int interface, cvmx_spi_mode_t mode)

    :param int interface:
        The identifier of the packet interface to configure and
        use as a SPI interface.

    :param cvmx_spi_mode_t mode:
        The operating mode for the SPI interface. The interface
        can operate as a full duplex (both Tx and Rx data paths
        active) or as a halfplex (either the Tx data path is
        active or the Rx data path is active, but not both).



.. _`cvmx_spi_interface_up_cb.description`:

Description
-----------

Returns Zero on success, non-zero error code on failure (will cause
SPI initialization to abort)

