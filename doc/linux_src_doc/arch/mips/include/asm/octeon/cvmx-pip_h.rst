.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-pip.h

.. _`cvmx_pip_rcv_err_t`:

typedef cvmx_pip_rcv_err_t
==========================

.. c:type:: typedef cvmx_pip_rcv_err_t

    late collision (data received before collision) late collisions cannot be detected by the receiver they would appear as JAM bits which would appear as bad FCS or carrier extend error which is CVMX_PIP_EXTEND_ERR

.. _`cvmx_pip_err_t`:

typedef cvmx_pip_err_t
======================

.. c:type:: typedef cvmx_pip_err_t


.. _`cvmx_pip_port_status_t`:

typedef cvmx_pip_port_status_t
==============================

.. c:type:: typedef cvmx_pip_port_status_t


.. _`cvmx_pip_pkt_inst_hdr_t`:

typedef cvmx_pip_pkt_inst_hdr_t
===============================

.. c:type:: typedef cvmx_pip_pkt_inst_hdr_t

    to a packet by external hardware.

.. _`cvmx_pip_config_port`:

cvmx_pip_config_port
====================

.. c:function:: void cvmx_pip_config_port(uint64_t port_num, union cvmx_pip_prt_cfgx port_cfg, union cvmx_pip_prt_tagx port_tag_cfg)

    :param uint64_t port_num:
        Port number to configure

    :param union cvmx_pip_prt_cfgx port_cfg:
        Port hardware configuration

    :param union cvmx_pip_prt_tagx port_tag_cfg:
        Port POW tagging configuration

.. _`cvmx_pip_config_vlan_qos`:

cvmx_pip_config_vlan_qos
========================

.. c:function:: void cvmx_pip_config_vlan_qos(uint64_t vlan_priority, uint64_t qos)

    :param uint64_t vlan_priority:
        VLAN priority (0-7)

    :param uint64_t qos:
        QoS queue for packets matching this watcher

.. _`cvmx_pip_config_diffserv_qos`:

cvmx_pip_config_diffserv_qos
============================

.. c:function:: void cvmx_pip_config_diffserv_qos(uint64_t diffserv, uint64_t qos)

    :param uint64_t diffserv:
        Diffserv field value (0-63)

    :param uint64_t qos:
        QoS queue for packets matching this watcher

.. _`cvmx_pip_get_port_status`:

cvmx_pip_get_port_status
========================

.. c:function:: void cvmx_pip_get_port_status(uint64_t port_num, uint64_t clear, cvmx_pip_port_status_t *status)

    :param uint64_t port_num:
        Port number to get statistics for.

    :param uint64_t clear:
        Set to 1 to clear the counters after they are read

    :param cvmx_pip_port_status_t \*status:
        Where to put the results.

.. _`cvmx_pip_config_crc`:

cvmx_pip_config_crc
===================

.. c:function:: void cvmx_pip_config_crc(uint64_t interface, uint64_t invert_result, uint64_t reflect, uint32_t initialization_vector)

    :param uint64_t interface:
        Interface to configure (0 or 1)

    :param uint64_t invert_result:
        Invert the result of the CRC

    :param uint64_t reflect:
        Reflect

    :param uint32_t initialization_vector:
        CRC initialization vector

.. _`cvmx_pip_tag_mask_clear`:

cvmx_pip_tag_mask_clear
=======================

.. c:function:: void cvmx_pip_tag_mask_clear(uint64_t mask_index)

    startup before any calls to cvmx_pip_tag_mask_set. Each bit set in the final mask represent a byte used in the packet for tag generation.

    :param uint64_t mask_index:
        Which tag mask to clear (0..3)

.. _`cvmx_pip_tag_mask_set`:

cvmx_pip_tag_mask_set
=====================

.. c:function:: void cvmx_pip_tag_mask_set(uint64_t mask_index, uint64_t offset, uint64_t len)

    when the cvmx_pip_port_tag_cfg_t tag_mode is non zero. There are four separate masks that can be configured.

    :param uint64_t mask_index:
        Which tag mask to modify (0..3)

    :param uint64_t offset:
        Offset into the bitmask to set bits at. Use the GCC macro
        \ :c:func:`offsetof`\  to determine the offsets into packet headers.
        For example, offsetof(ethhdr, protocol) returns the offset
        of the ethernet protocol field.  The bitmask selects which
        bytes to include the the tag, with bit offset X selecting
        byte at offset X from the beginning of the packet data.

    :param uint64_t len:
        Number of bytes to include. Usually this is the \ :c:func:`sizeof`\ 
        the field.

.. This file was automatic generated / don't edit.

