.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-helper-util.h

.. _`cvmx_helper_interface_mode_to_string`:

cvmx_helper_interface_mode_to_string
====================================

.. c:function:: const char *cvmx_helper_interface_mode_to_string(cvmx_helper_interface_mode_t mode)

    :param mode:
        Mode to convert
    :type mode: cvmx_helper_interface_mode_t

.. _`cvmx_helper_interface_mode_to_string.description`:

Description
-----------

Returns String

.. _`cvmx_helper_dump_packet`:

cvmx_helper_dump_packet
=======================

.. c:function:: int cvmx_helper_dump_packet(cvmx_wqe_t *work)

    :param work:
        Work queue entry containing the packet to dump
        Returns
    :type work: cvmx_wqe_t \*

.. _`cvmx_helper_setup_red_queue`:

cvmx_helper_setup_red_queue
===========================

.. c:function:: int cvmx_helper_setup_red_queue(int queue, int pass_thresh, int drop_thresh)

    :param queue:
        Input queue to setup RED on (0-7)
    :type queue: int

    :param pass_thresh:
        Packets will begin slowly dropping when there are less than
        this many packet buffers free in FPA 0.
    :type pass_thresh: int

    :param drop_thresh:
        All incoming packets will be dropped when there are less
        than this many free packet buffers in FPA 0.
        Returns Zero on success. Negative on failure
    :type drop_thresh: int

.. _`cvmx_helper_setup_red`:

cvmx_helper_setup_red
=====================

.. c:function:: int cvmx_helper_setup_red(int pass_thresh, int drop_thresh)

    :param pass_thresh:
        Packets will begin slowly dropping when there are less than
        this many packet buffers free in FPA 0.
    :type pass_thresh: int

    :param drop_thresh:
        All incoming packets will be dropped when there are less
        than this many free packet buffers in FPA 0.
        Returns Zero on success. Negative on failure
    :type drop_thresh: int

.. _`cvmx_helper_get_version`:

cvmx_helper_get_version
=======================

.. c:function:: const char *cvmx_helper_get_version( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_helper_get_version.description`:

Description
-----------

Returns Version string. Note this buffer is allocated statically
and will be shared by all callers.

.. _`__cvmx_helper_setup_gmx`:

\__cvmx_helper_setup_gmx
========================

.. c:function:: int __cvmx_helper_setup_gmx(int interface, int num_ports)

    ports. These setting apply to almost all configurations of all chips.

    :param interface:
        Interface to configure
    :type interface: int

    :param num_ports:
        Number of ports on the interface
    :type num_ports: int

.. _`__cvmx_helper_setup_gmx.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`cvmx_helper_get_ipd_port`:

cvmx_helper_get_ipd_port
========================

.. c:function:: int cvmx_helper_get_ipd_port(int interface, int port)

    interface.

    :param interface:
        Interface to use
    :type interface: int

    :param port:
        Port on the interface
    :type port: int

.. _`cvmx_helper_get_ipd_port.description`:

Description
-----------

Returns IPD/PKO port number

.. _`cvmx_helper_get_first_ipd_port`:

cvmx_helper_get_first_ipd_port
==============================

.. c:function:: int cvmx_helper_get_first_ipd_port(int interface)

    interface.

    :param interface:
        Interface to use
    :type interface: int

.. _`cvmx_helper_get_first_ipd_port.description`:

Description
-----------

Returns IPD/PKO port number

.. _`cvmx_helper_get_last_ipd_port`:

cvmx_helper_get_last_ipd_port
=============================

.. c:function:: int cvmx_helper_get_last_ipd_port(int interface)

    interface.

    :param interface:
        Interface to use
    :type interface: int

.. _`cvmx_helper_get_last_ipd_port.description`:

Description
-----------

Returns IPD/PKO port number

.. _`cvmx_helper_free_packet_data`:

cvmx_helper_free_packet_data
============================

.. c:function:: void cvmx_helper_free_packet_data(cvmx_wqe_t *work)

    The work queue entry is not freed.

    :param work:
        Work queue entry with packet to free
    :type work: cvmx_wqe_t \*

.. _`cvmx_helper_get_interface_num`:

cvmx_helper_get_interface_num
=============================

.. c:function:: int cvmx_helper_get_interface_num(int ipd_port)

    :param ipd_port:
        IPD/PKO port number
    :type ipd_port: int

.. _`cvmx_helper_get_interface_num.description`:

Description
-----------

Returns Interface number

.. _`cvmx_helper_get_interface_index_num`:

cvmx_helper_get_interface_index_num
===================================

.. c:function:: int cvmx_helper_get_interface_index_num(int ipd_port)

    number.

    :param ipd_port:
        IPD/PKO port number
    :type ipd_port: int

.. _`cvmx_helper_get_interface_index_num.description`:

Description
-----------

Returns Interface index number

.. This file was automatic generated / don't edit.

