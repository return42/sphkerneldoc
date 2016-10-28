.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/fman/fman_port.c

.. _`fman_port_config`:

fman_port_config
================

.. c:function:: int fman_port_config(struct fman_port *port, struct fman_port_params *params)

    :param struct fman_port \*port:
        Pointer to the port structure

    :param struct fman_port_params \*params:
        Pointer to data structure of parameters

.. _`fman_port_config.description`:

Description
-----------

Creates a descriptor for the FM PORT module.
The routine returns a pointer to the FM PORT object.
This descriptor must be passed as first parameter to all other FM PORT
function calls.
No actual initialization or configuration of FM hardware is done by this
routine.

.. _`fman_port_config.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_port_init`:

fman_port_init
==============

.. c:function:: int fman_port_init(struct fman_port *port)

    :param struct fman_port \*port:
        *undescribed*

.. _`fman_port_init.port`:

port
----

A pointer to a FM Port module.
Initializes the FM PORT module by defining the software structure and
configuring the hardware registers.

.. _`fman_port_init.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_port_cfg_buf_prefix_content`:

fman_port_cfg_buf_prefix_content
================================

.. c:function:: int fman_port_cfg_buf_prefix_content(struct fman_port *port, struct fman_buffer_prefix_content *buffer_prefix_content)

    \ ``port``\                         A pointer to a FM Port module. \ ``buffer_prefix_content``\        A structure of parameters describing the structure of the buffer. Out parameter: Start margin - offset of data from start of external buffer. Defines the structure, size and content of the application buffer. The prefix, in Tx ports, if 'pass_prs_result', the application should set a value to their offsets in the prefix of the FM will save the first 'priv_data_size', than, depending on 'pass_prs_result' and 'pass_time_stamp', copy parse result and timeStamp, and the packet itself (in this order), to the application buffer, and to offset. Calling this routine changes the buffer margins definitions in the internal

    :param struct fman_port \*port:
        *undescribed*

    :param struct fman_buffer_prefix_content \*buffer_prefix_content:
        *undescribed*

.. _`fman_port_cfg_buf_prefix_content.data-size`:

Data size
---------

[DEFAULT_PORT_BUFFER_PREFIX_CONTENT_PRIV_DATA_SIZE]

.. _`fman_port_cfg_buf_prefix_content.pass-parser-result`:

Pass Parser result
------------------

[DEFAULT_PORT_BUFFER_PREFIX_CONTENT_PASS_PRS_RESULT].

.. _`fman_port_cfg_buf_prefix_content.pass-timestamp`:

Pass timestamp
--------------

[DEFAULT_PORT_BUFFER_PREFIX_CONTENT_PASS_TIME_STAMP].
May be used for all ports

Allowed only following \ :c:func:`fman_port_config`\  and before \ :c:func:`fman_port_init`\ .

.. _`fman_port_cfg_buf_prefix_content.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_port_disable`:

fman_port_disable
=================

.. c:function:: int fman_port_disable(struct fman_port *port)

    :param struct fman_port \*port:
        *undescribed*

.. _`fman_port_disable.port`:

port
----

A pointer to a FM Port module.

Gracefully disable an FM port. The port will not start new   tasks after all
tasks associated with the port are terminated.

This is a blocking routine, it returns after port is gracefully stopped,
i.e. the port will not except new frames, but it will finish all frames
or tasks which were already began.
Allowed only following \ :c:func:`fman_port_init`\ .

.. _`fman_port_disable.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_port_enable`:

fman_port_enable
================

.. c:function:: int fman_port_enable(struct fman_port *port)

    :param struct fman_port \*port:
        *undescribed*

.. _`fman_port_enable.port`:

port
----

A pointer to a FM Port module.

A runtime routine provided to allow disable/enable of port.

Allowed only following \ :c:func:`fman_port_init`\ .

.. _`fman_port_enable.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_port_bind`:

fman_port_bind
==============

.. c:function:: struct fman_port *fman_port_bind(struct device *dev)

    :param struct device \*dev:
        *undescribed*

.. _`fman_port_bind.dev`:

dev
---

FMan Port OF device pointer

Bind to a specific FMan Port.

Allowed only after the port was created.

.. _`fman_port_bind.return`:

Return
------

A pointer to the FMan port device.

.. _`fman_port_get_qman_channel_id`:

fman_port_get_qman_channel_id
=============================

.. c:function:: u32 fman_port_get_qman_channel_id(struct fman_port *port)

    :param struct fman_port \*port:
        *undescribed*

.. _`fman_port_get_qman_channel_id.port`:

port
----

Pointer to the FMan port devuce

Get the QMan channel ID for the specific port

.. _`fman_port_get_qman_channel_id.return`:

Return
------

QMan channel ID

.. This file was automatic generated / don't edit.

