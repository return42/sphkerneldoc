.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/stream.c

.. _`sdw_program_port_params`:

sdw_program_port_params
=======================

.. c:function:: int sdw_program_port_params(struct sdw_master_runtime *m_rt)

    Programs transport parameters of Master(s) and Slave(s)

    :param m_rt:
        Master stream runtime
    :type m_rt: struct sdw_master_runtime \*

.. _`sdw_enable_disable_slave_ports`:

sdw_enable_disable_slave_ports
==============================

.. c:function:: int sdw_enable_disable_slave_ports(struct sdw_bus *bus, struct sdw_slave_runtime *s_rt, struct sdw_port_runtime *p_rt, bool en)

    Enable/disable slave data port

    :param bus:
        bus instance
    :type bus: struct sdw_bus \*

    :param s_rt:
        slave runtime
    :type s_rt: struct sdw_slave_runtime \*

    :param p_rt:
        port runtime
    :type p_rt: struct sdw_port_runtime \*

    :param en:
        enable or disable operation
    :type en: bool

.. _`sdw_enable_disable_slave_ports.description`:

Description
-----------

This function only sets the enable/disable bits in the relevant bank, the
actual enable/disable is done with a bank switch

.. _`sdw_enable_disable_ports`:

sdw_enable_disable_ports
========================

.. c:function:: int sdw_enable_disable_ports(struct sdw_master_runtime *m_rt, bool en)

    Enable/disable port(s) for Master and Slave(s)

    :param m_rt:
        Master stream runtime
    :type m_rt: struct sdw_master_runtime \*

    :param en:
        mode (enable/disable)
    :type en: bool

.. _`sdw_prep_deprep_ports`:

sdw_prep_deprep_ports
=====================

.. c:function:: int sdw_prep_deprep_ports(struct sdw_master_runtime *m_rt, bool prep)

    Prepare/De-prepare port(s) for Master(s) and Slave(s)

    :param m_rt:
        Master runtime handle
    :type m_rt: struct sdw_master_runtime \*

    :param prep:
        Prepare or De-prepare
    :type prep: bool

.. _`sdw_notify_config`:

sdw_notify_config
=================

.. c:function:: int sdw_notify_config(struct sdw_master_runtime *m_rt)

    Notify bus configuration

    :param m_rt:
        Master runtime handle
    :type m_rt: struct sdw_master_runtime \*

.. _`sdw_notify_config.description`:

Description
-----------

This function notifies the Master(s) and Slave(s) of the
new bus configuration.

.. _`sdw_program_params`:

sdw_program_params
==================

.. c:function:: int sdw_program_params(struct sdw_bus *bus)

    Program transport and port parameters for Master(s) and Slave(s)

    :param bus:
        SDW bus instance
    :type bus: struct sdw_bus \*

.. _`sdw_ml_sync_bank_switch`:

sdw_ml_sync_bank_switch
=======================

.. c:function:: int sdw_ml_sync_bank_switch(struct sdw_bus *bus)

    Multilink register bank switch

    :param bus:
        SDW bus instance
    :type bus: struct sdw_bus \*

.. _`sdw_ml_sync_bank_switch.description`:

Description
-----------

Caller function should free the buffers on error

.. _`sdw_release_stream`:

sdw_release_stream
==================

.. c:function:: void sdw_release_stream(struct sdw_stream_runtime *stream)

    Free the assigned stream runtime

    :param stream:
        SoundWire stream runtime
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_release_stream.description`:

Description
-----------

sdw_release_stream should be called only once per stream

.. _`sdw_alloc_stream`:

sdw_alloc_stream
================

.. c:function:: struct sdw_stream_runtime *sdw_alloc_stream(char *stream_name)

    Allocate and return stream runtime

    :param stream_name:
        SoundWire stream name
    :type stream_name: char \*

.. _`sdw_alloc_stream.description`:

Description
-----------

Allocates a SoundWire stream runtime instance.
sdw_alloc_stream should be called only once per stream. Typically
invoked from ALSA/ASoC machine/platform driver.

.. _`sdw_alloc_master_rt`:

sdw_alloc_master_rt
===================

.. c:function:: struct sdw_master_runtime *sdw_alloc_master_rt(struct sdw_bus *bus, struct sdw_stream_config *stream_config, struct sdw_stream_runtime *stream)

    Allocates and initialize Master runtime handle

    :param bus:
        SDW bus instance
    :type bus: struct sdw_bus \*

    :param stream_config:
        Stream configuration
    :type stream_config: struct sdw_stream_config \*

    :param stream:
        Stream runtime handle.
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_alloc_master_rt.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_alloc_slave_rt`:

sdw_alloc_slave_rt
==================

.. c:function:: struct sdw_slave_runtime *sdw_alloc_slave_rt(struct sdw_slave *slave, struct sdw_stream_config *stream_config, struct sdw_stream_runtime *stream)

    Allocate and initialize Slave runtime handle.

    :param slave:
        Slave handle
    :type slave: struct sdw_slave \*

    :param stream_config:
        Stream configuration
    :type stream_config: struct sdw_stream_config \*

    :param stream:
        Stream runtime handle
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_alloc_slave_rt.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_release_slave_stream`:

sdw_release_slave_stream
========================

.. c:function:: void sdw_release_slave_stream(struct sdw_slave *slave, struct sdw_stream_runtime *stream)

    Free Slave(s) runtime handle

    :param slave:
        Slave handle.
    :type slave: struct sdw_slave \*

    :param stream:
        Stream runtime handle.
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_release_slave_stream.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_release_master_stream`:

sdw_release_master_stream
=========================

.. c:function:: void sdw_release_master_stream(struct sdw_master_runtime *m_rt, struct sdw_stream_runtime *stream)

    Free Master runtime handle

    :param m_rt:
        Master runtime node
    :type m_rt: struct sdw_master_runtime \*

    :param stream:
        Stream runtime handle.
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_release_master_stream.description`:

Description
-----------

This function is to be called with bus_lock held
It frees the Master runtime handle and associated Slave(s) runtime
handle. If this is called first then \ :c:func:`sdw_release_slave_stream`\  will have
no effect as Slave(s) runtime handle would already be freed up.

.. _`sdw_stream_remove_master`:

sdw_stream_remove_master
========================

.. c:function:: int sdw_stream_remove_master(struct sdw_bus *bus, struct sdw_stream_runtime *stream)

    Remove master from sdw_stream

    :param bus:
        SDW Bus instance
    :type bus: struct sdw_bus \*

    :param stream:
        SoundWire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_stream_remove_master.description`:

Description
-----------

This removes and frees port_rt and master_rt from a stream

.. _`sdw_stream_remove_slave`:

sdw_stream_remove_slave
=======================

.. c:function:: int sdw_stream_remove_slave(struct sdw_slave *slave, struct sdw_stream_runtime *stream)

    Remove slave from sdw_stream

    :param slave:
        SDW Slave instance
    :type slave: struct sdw_slave \*

    :param stream:
        SoundWire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_stream_remove_slave.description`:

Description
-----------

This removes and frees port_rt and slave_rt from a stream

.. _`sdw_config_stream`:

sdw_config_stream
=================

.. c:function:: int sdw_config_stream(struct device *dev, struct sdw_stream_runtime *stream, struct sdw_stream_config *stream_config, bool is_slave)

    Configure the allocated stream

    :param dev:
        SDW device
    :type dev: struct device \*

    :param stream:
        SoundWire stream
    :type stream: struct sdw_stream_runtime \*

    :param stream_config:
        Stream configuration for audio stream
    :type stream_config: struct sdw_stream_config \*

    :param is_slave:
        is API called from Slave or Master
    :type is_slave: bool

.. _`sdw_config_stream.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_stream_add_master`:

sdw_stream_add_master
=====================

.. c:function:: int sdw_stream_add_master(struct sdw_bus *bus, struct sdw_stream_config *stream_config, struct sdw_port_config *port_config, unsigned int num_ports, struct sdw_stream_runtime *stream)

    Allocate and add master runtime to a stream

    :param bus:
        SDW Bus instance
    :type bus: struct sdw_bus \*

    :param stream_config:
        Stream configuration for audio stream
    :type stream_config: struct sdw_stream_config \*

    :param port_config:
        Port configuration for audio stream
    :type port_config: struct sdw_port_config \*

    :param num_ports:
        Number of ports
    :type num_ports: unsigned int

    :param stream:
        SoundWire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_stream_add_slave`:

sdw_stream_add_slave
====================

.. c:function:: int sdw_stream_add_slave(struct sdw_slave *slave, struct sdw_stream_config *stream_config, struct sdw_port_config *port_config, unsigned int num_ports, struct sdw_stream_runtime *stream)

    Allocate and add master/slave runtime to a stream

    :param slave:
        SDW Slave instance
    :type slave: struct sdw_slave \*

    :param stream_config:
        Stream configuration for audio stream
    :type stream_config: struct sdw_stream_config \*

    :param port_config:
        Port configuration for audio stream
    :type port_config: struct sdw_port_config \*

    :param num_ports:
        Number of ports
    :type num_ports: unsigned int

    :param stream:
        SoundWire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_stream_add_slave.description`:

Description
-----------

It is expected that Slave is added before adding Master
to the Stream.

.. _`sdw_get_slave_dpn_prop`:

sdw_get_slave_dpn_prop
======================

.. c:function:: struct sdw_dpn_prop *sdw_get_slave_dpn_prop(struct sdw_slave *slave, enum sdw_data_direction direction, unsigned int port_num)

    Get Slave port capabilities

    :param slave:
        Slave handle
    :type slave: struct sdw_slave \*

    :param direction:
        Data direction.
    :type direction: enum sdw_data_direction

    :param port_num:
        Port number
    :type port_num: unsigned int

.. _`sdw_acquire_bus_lock`:

sdw_acquire_bus_lock
====================

.. c:function:: void sdw_acquire_bus_lock(struct sdw_stream_runtime *stream)

    Acquire bus lock for all Master runtime(s)

    :param stream:
        SoundWire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_acquire_bus_lock.description`:

Description
-----------

Acquire bus_lock for each of the master runtime(m_rt) part of this
stream to reconfigure the bus.

.. _`sdw_acquire_bus_lock.note`:

NOTE
----

This function is called from SoundWire stream ops and is
expected that a global lock is held before acquiring bus_lock.

.. _`sdw_release_bus_lock`:

sdw_release_bus_lock
====================

.. c:function:: void sdw_release_bus_lock(struct sdw_stream_runtime *stream)

    Release bus lock for all Master runtime(s)

    :param stream:
        SoundWire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_release_bus_lock.description`:

Description
-----------

Release the previously held bus_lock after reconfiguring the bus.

.. _`sdw_release_bus_lock.note`:

NOTE
----

This function is called from SoundWire stream ops and is
expected that a global lock is held before releasing bus_lock.

.. _`sdw_prepare_stream`:

sdw_prepare_stream
==================

.. c:function:: int sdw_prepare_stream(struct sdw_stream_runtime *stream)

    Prepare SoundWire stream

    :param stream:
        Soundwire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_prepare_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. _`sdw_enable_stream`:

sdw_enable_stream
=================

.. c:function:: int sdw_enable_stream(struct sdw_stream_runtime *stream)

    Enable SoundWire stream

    :param stream:
        Soundwire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_enable_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. _`sdw_disable_stream`:

sdw_disable_stream
==================

.. c:function:: int sdw_disable_stream(struct sdw_stream_runtime *stream)

    Disable SoundWire stream

    :param stream:
        Soundwire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_disable_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. _`sdw_deprepare_stream`:

sdw_deprepare_stream
====================

.. c:function:: int sdw_deprepare_stream(struct sdw_stream_runtime *stream)

    Deprepare SoundWire stream

    :param stream:
        Soundwire stream
    :type stream: struct sdw_stream_runtime \*

.. _`sdw_deprepare_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. This file was automatic generated / don't edit.

