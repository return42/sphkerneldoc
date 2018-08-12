.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/stream.c

.. _`sdw_program_port_params`:

sdw_program_port_params
=======================

.. c:function:: int sdw_program_port_params(struct sdw_master_runtime *m_rt)

    Programs transport parameters of Master(s) and Slave(s)

    :param struct sdw_master_runtime \*m_rt:
        Master stream runtime

.. _`sdw_enable_disable_slave_ports`:

sdw_enable_disable_slave_ports
==============================

.. c:function:: int sdw_enable_disable_slave_ports(struct sdw_bus *bus, struct sdw_slave_runtime *s_rt, struct sdw_port_runtime *p_rt, bool en)

    Enable/disable slave data port

    :param struct sdw_bus \*bus:
        bus instance

    :param struct sdw_slave_runtime \*s_rt:
        slave runtime

    :param struct sdw_port_runtime \*p_rt:
        port runtime

    :param bool en:
        enable or disable operation

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

    :param struct sdw_master_runtime \*m_rt:
        Master stream runtime

    :param bool en:
        mode (enable/disable)

.. _`sdw_prep_deprep_ports`:

sdw_prep_deprep_ports
=====================

.. c:function:: int sdw_prep_deprep_ports(struct sdw_master_runtime *m_rt, bool prep)

    Prepare/De-prepare port(s) for Master(s) and Slave(s)

    :param struct sdw_master_runtime \*m_rt:
        Master runtime handle

    :param bool prep:
        Prepare or De-prepare

.. _`sdw_notify_config`:

sdw_notify_config
=================

.. c:function:: int sdw_notify_config(struct sdw_master_runtime *m_rt)

    Notify bus configuration

    :param struct sdw_master_runtime \*m_rt:
        Master runtime handle

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

    :param struct sdw_bus \*bus:
        SDW bus instance

.. _`sdw_release_stream`:

sdw_release_stream
==================

.. c:function:: void sdw_release_stream(struct sdw_stream_runtime *stream)

    Free the assigned stream runtime

    :param struct sdw_stream_runtime \*stream:
        SoundWire stream runtime

.. _`sdw_release_stream.description`:

Description
-----------

sdw_release_stream should be called only once per stream

.. _`sdw_alloc_stream`:

sdw_alloc_stream
================

.. c:function:: struct sdw_stream_runtime *sdw_alloc_stream(char *stream_name)

    Allocate and return stream runtime

    :param char \*stream_name:
        SoundWire stream name

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

    :param struct sdw_bus \*bus:
        SDW bus instance

    :param struct sdw_stream_config \*stream_config:
        Stream configuration

    :param struct sdw_stream_runtime \*stream:
        Stream runtime handle.

.. _`sdw_alloc_master_rt.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_alloc_slave_rt`:

sdw_alloc_slave_rt
==================

.. c:function:: struct sdw_slave_runtime *sdw_alloc_slave_rt(struct sdw_slave *slave, struct sdw_stream_config *stream_config, struct sdw_stream_runtime *stream)

    Allocate and initialize Slave runtime handle.

    :param struct sdw_slave \*slave:
        Slave handle

    :param struct sdw_stream_config \*stream_config:
        Stream configuration

    :param struct sdw_stream_runtime \*stream:
        Stream runtime handle

.. _`sdw_alloc_slave_rt.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_release_slave_stream`:

sdw_release_slave_stream
========================

.. c:function:: void sdw_release_slave_stream(struct sdw_slave *slave, struct sdw_stream_runtime *stream)

    Free Slave(s) runtime handle

    :param struct sdw_slave \*slave:
        Slave handle.

    :param struct sdw_stream_runtime \*stream:
        Stream runtime handle.

.. _`sdw_release_slave_stream.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_release_master_stream`:

sdw_release_master_stream
=========================

.. c:function:: void sdw_release_master_stream(struct sdw_stream_runtime *stream)

    Free Master runtime handle

    :param struct sdw_stream_runtime \*stream:
        Stream runtime handle.

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

    :param struct sdw_bus \*bus:
        SDW Bus instance

    :param struct sdw_stream_runtime \*stream:
        SoundWire stream

.. _`sdw_stream_remove_master.description`:

Description
-----------

This removes and frees port_rt and master_rt from a stream

.. _`sdw_stream_remove_slave`:

sdw_stream_remove_slave
=======================

.. c:function:: int sdw_stream_remove_slave(struct sdw_slave *slave, struct sdw_stream_runtime *stream)

    Remove slave from sdw_stream

    :param struct sdw_slave \*slave:
        SDW Slave instance

    :param struct sdw_stream_runtime \*stream:
        SoundWire stream

.. _`sdw_stream_remove_slave.description`:

Description
-----------

This removes and frees port_rt and slave_rt from a stream

.. _`sdw_config_stream`:

sdw_config_stream
=================

.. c:function:: int sdw_config_stream(struct device *dev, struct sdw_stream_runtime *stream, struct sdw_stream_config *stream_config, bool is_slave)

    Configure the allocated stream

    :param struct device \*dev:
        SDW device

    :param struct sdw_stream_runtime \*stream:
        SoundWire stream

    :param struct sdw_stream_config \*stream_config:
        Stream configuration for audio stream

    :param bool is_slave:
        is API called from Slave or Master

.. _`sdw_config_stream.description`:

Description
-----------

This function is to be called with bus_lock held.

.. _`sdw_stream_add_master`:

sdw_stream_add_master
=====================

.. c:function:: int sdw_stream_add_master(struct sdw_bus *bus, struct sdw_stream_config *stream_config, struct sdw_port_config *port_config, unsigned int num_ports, struct sdw_stream_runtime *stream)

    Allocate and add master runtime to a stream

    :param struct sdw_bus \*bus:
        SDW Bus instance

    :param struct sdw_stream_config \*stream_config:
        Stream configuration for audio stream

    :param struct sdw_port_config \*port_config:
        Port configuration for audio stream

    :param unsigned int num_ports:
        Number of ports

    :param struct sdw_stream_runtime \*stream:
        SoundWire stream

.. _`sdw_stream_add_slave`:

sdw_stream_add_slave
====================

.. c:function:: int sdw_stream_add_slave(struct sdw_slave *slave, struct sdw_stream_config *stream_config, struct sdw_port_config *port_config, unsigned int num_ports, struct sdw_stream_runtime *stream)

    Allocate and add master/slave runtime to a stream

    :param struct sdw_slave \*slave:
        SDW Slave instance

    :param struct sdw_stream_config \*stream_config:
        Stream configuration for audio stream

    :param struct sdw_port_config \*port_config:
        Port configuration for audio stream

    :param unsigned int num_ports:
        Number of ports

    :param struct sdw_stream_runtime \*stream:
        SoundWire stream

.. _`sdw_get_slave_dpn_prop`:

sdw_get_slave_dpn_prop
======================

.. c:function:: struct sdw_dpn_prop *sdw_get_slave_dpn_prop(struct sdw_slave *slave, enum sdw_data_direction direction, unsigned int port_num)

    Get Slave port capabilities

    :param struct sdw_slave \*slave:
        Slave handle

    :param enum sdw_data_direction direction:
        Data direction.

    :param unsigned int port_num:
        Port number

.. _`sdw_prepare_stream`:

sdw_prepare_stream
==================

.. c:function:: int sdw_prepare_stream(struct sdw_stream_runtime *stream)

    Prepare SoundWire stream

    :param struct sdw_stream_runtime \*stream:
        Soundwire stream

.. _`sdw_prepare_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. _`sdw_enable_stream`:

sdw_enable_stream
=================

.. c:function:: int sdw_enable_stream(struct sdw_stream_runtime *stream)

    Enable SoundWire stream

    :param struct sdw_stream_runtime \*stream:
        Soundwire stream

.. _`sdw_enable_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. _`sdw_disable_stream`:

sdw_disable_stream
==================

.. c:function:: int sdw_disable_stream(struct sdw_stream_runtime *stream)

    Disable SoundWire stream

    :param struct sdw_stream_runtime \*stream:
        Soundwire stream

.. _`sdw_disable_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. _`sdw_deprepare_stream`:

sdw_deprepare_stream
====================

.. c:function:: int sdw_deprepare_stream(struct sdw_stream_runtime *stream)

    Deprepare SoundWire stream

    :param struct sdw_stream_runtime \*stream:
        Soundwire stream

.. _`sdw_deprepare_stream.description`:

Description
-----------

Documentation/driver-api/soundwire/stream.rst explains this API in detail

.. This file was automatic generated / don't edit.

