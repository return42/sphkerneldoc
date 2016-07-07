.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-ipd.h

.. _`cvmx_ipd_config`:

cvmx_ipd_config
===============

.. c:function:: void cvmx_ipd_config(uint64_t mbuff_size, uint64_t first_mbuff_skip, uint64_t not_first_mbuff_skip, uint64_t first_back, uint64_t second_back, uint64_t wqe_fpa_pool, enum cvmx_ipd_mode cache_mode, uint64_t back_pres_enable_flag)

    :param uint64_t mbuff_size:
        Packets buffer size in 8 byte words

    :param uint64_t first_mbuff_skip:
        Number of 8 byte words to skip in the first buffer

    :param uint64_t not_first_mbuff_skip:
        Number of 8 byte words to skip in each following buffer

    :param uint64_t first_back:
        Must be same as first_mbuff_skip / 128

    :param uint64_t second_back:
        Must be same as not_first_mbuff_skip / 128

    :param uint64_t wqe_fpa_pool:
        FPA pool to get work entries from

    :param enum cvmx_ipd_mode cache_mode:
        *undescribed*

    :param uint64_t back_pres_enable_flag:
        Enable or disable port back pressure

.. _`cvmx_ipd_enable`:

cvmx_ipd_enable
===============

.. c:function:: void cvmx_ipd_enable( void)

    :param  void:
        no arguments

.. _`cvmx_ipd_disable`:

cvmx_ipd_disable
================

.. c:function:: void cvmx_ipd_disable( void)

    :param  void:
        no arguments

.. _`cvmx_ipd_free_ptr`:

cvmx_ipd_free_ptr
=================

.. c:function:: void cvmx_ipd_free_ptr( void)

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

