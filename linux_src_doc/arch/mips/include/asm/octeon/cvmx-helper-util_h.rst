.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-helper-util.h

.. _`cvmx_helper_interface_mode_to_string`:

cvmx_helper_interface_mode_to_string
====================================

.. c:function:: const char *cvmx_helper_interface_mode_to_string(cvmx_helper_interface_mode_t mode)

    :param cvmx_helper_interface_mode_t mode:
        Mode to convert

.. _`cvmx_helper_interface_mode_to_string.description`:

Description
-----------

Returns String

.. _`cvmx_helper_dump_packet`:

cvmx_helper_dump_packet
=======================

.. c:function:: int cvmx_helper_dump_packet(cvmx_wqe_t *work)

    :param cvmx_wqe_t \*work:
        Work queue entry containing the packet to dump
        Returns

.. _`cvmx_helper_setup_red_queue`:

cvmx_helper_setup_red_queue
===========================

.. c:function:: int cvmx_helper_setup_red_queue(int queue, int pass_thresh, int drop_thresh)

    :param int queue:
        Input queue to setup RED on (0-7)

    :param int pass_thresh:
        Packets will begin slowly dropping when there are less than
        this many packet buffers free in FPA 0.

    :param int drop_thresh:
        All incoming packets will be dropped when there are less
        than this many free packet buffers in FPA 0.
        Returns Zero on success. Negative on failure

.. _`cvmx_helper_setup_red`:

cvmx_helper_setup_red
=====================

.. c:function:: int cvmx_helper_setup_red(int pass_thresh, int drop_thresh)

    :param int pass_thresh:
        Packets will begin slowly dropping when there are less than
        this many packet buffers free in FPA 0.

    :param int drop_thresh:
        All incoming packets will be dropped when there are less
        than this many free packet buffers in FPA 0.
        Returns Zero on success. Negative on failure

.. _`cvmx_helper_get_version`:

cvmx_helper_get_version
=======================

.. c:function:: const char *cvmx_helper_get_version( void)

    :param  void:
        no arguments

.. _`cvmx_helper_get_version.description`:

Description
-----------

Returns Version string. Note this buffer is allocated statically
and will be shared by all callers.

.. _`__cvmx_helper_setup_gmx`:

__cvmx_helper_setup_gmx
=======================

.. c:function:: int __cvmx_helper_setup_gmx(int interface, int num_ports)

    ports. These setting apply to almost all configurations of all chips.

    :param int interface:
        Interface to configure

    :param int num_ports:
        Number of ports on the interface

.. _`__cvmx_helper_setup_gmx.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`cvmx_helper_get_ipd_port`:

cvmx_helper_get_ipd_port
========================

.. c:function:: int cvmx_helper_get_ipd_port(int interface, int port)

    interface.

    :param int interface:
        Interface to use

    :param int port:
        Port on the interface

.. _`cvmx_helper_get_ipd_port.description`:

Description
-----------

Returns IPD/PKO port number

.. _`cvmx_helper_get_first_ipd_port`:

cvmx_helper_get_first_ipd_port
==============================

.. c:function:: int cvmx_helper_get_first_ipd_port(int interface)

    interface.

    :param int interface:
        Interface to use

.. _`cvmx_helper_get_first_ipd_port.description`:

Description
-----------

Returns IPD/PKO port number

.. _`cvmx_helper_get_last_ipd_port`:

cvmx_helper_get_last_ipd_port
=============================

.. c:function:: int cvmx_helper_get_last_ipd_port(int interface)

    interface.

    :param int interface:
        Interface to use

.. _`cvmx_helper_get_last_ipd_port.description`:

Description
-----------

Returns IPD/PKO port number

.. _`cvmx_helper_free_packet_data`:

cvmx_helper_free_packet_data
============================

.. c:function:: void cvmx_helper_free_packet_data(cvmx_wqe_t *work)

    The work queue entry is not freed.

    :param cvmx_wqe_t \*work:
        Work queue entry with packet to free

.. _`cvmx_helper_get_interface_num`:

cvmx_helper_get_interface_num
=============================

.. c:function:: int cvmx_helper_get_interface_num(int ipd_port)

    :param int ipd_port:
        IPD/PKO port number

.. _`cvmx_helper_get_interface_num.description`:

Description
-----------

Returns Interface number

.. _`cvmx_helper_get_interface_index_num`:

cvmx_helper_get_interface_index_num
===================================

.. c:function:: int cvmx_helper_get_interface_index_num(int ipd_port)

    number.

    :param int ipd_port:
        IPD/PKO port number

.. _`cvmx_helper_get_interface_index_num.description`:

Description
-----------

Returns Interface index number

.. This file was automatic generated / don't edit.

