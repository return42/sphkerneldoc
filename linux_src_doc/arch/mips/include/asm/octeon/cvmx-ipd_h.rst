.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-ipd.h

.. _`cvmx_ipd_config`:

cvmx_ipd_config
===============

.. c:function:: void cvmx_ipd_config(uint64_t mbuff_size, uint64_t first_mbuff_skip, uint64_t not_first_mbuff_skip, uint64_t first_back, uint64_t second_back, uint64_t wqe_fpa_pool, enum cvmx_ipd_mode cache_mode, uint64_t back_pres_enable_flag)

    :param mbuff_size:
        Packets buffer size in 8 byte words
    :type mbuff_size: uint64_t

    :param first_mbuff_skip:
        Number of 8 byte words to skip in the first buffer
    :type first_mbuff_skip: uint64_t

    :param not_first_mbuff_skip:
        Number of 8 byte words to skip in each following buffer
    :type not_first_mbuff_skip: uint64_t

    :param first_back:
        Must be same as first_mbuff_skip / 128
    :type first_back: uint64_t

    :param second_back:
        Must be same as not_first_mbuff_skip / 128
    :type second_back: uint64_t

    :param wqe_fpa_pool:
        FPA pool to get work entries from
    :type wqe_fpa_pool: uint64_t

    :param cache_mode:
        *undescribed*
    :type cache_mode: enum cvmx_ipd_mode

    :param back_pres_enable_flag:
        Enable or disable port back pressure
    :type back_pres_enable_flag: uint64_t

.. _`cvmx_ipd_enable`:

cvmx_ipd_enable
===============

.. c:function:: void cvmx_ipd_enable( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_ipd_disable`:

cvmx_ipd_disable
================

.. c:function:: void cvmx_ipd_disable( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_ipd_free_ptr`:

cvmx_ipd_free_ptr
=================

.. c:function:: void cvmx_ipd_free_ptr( void)

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

