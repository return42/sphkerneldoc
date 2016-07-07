.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/oprofile/hwsampler.c

.. _`hwsampler_deactivate`:

hwsampler_deactivate
====================

.. c:function:: int hwsampler_deactivate(unsigned int cpu)

    set hardware sampling temporarily inactive

    :param unsigned int cpu:
        specifies the CPU to be set inactive.

.. _`hwsampler_deactivate.description`:

Description
-----------

Returns 0 on success, !0 on failure.

.. _`hwsampler_activate`:

hwsampler_activate
==================

.. c:function:: int hwsampler_activate(unsigned int cpu)

    activate/resume hardware sampling which was deactivated

    :param unsigned int cpu:
        specifies the CPU to be set active.

.. _`hwsampler_activate.description`:

Description
-----------

Returns 0 on success, !0 on failure.

.. _`hwsampler_allocate`:

hwsampler_allocate
==================

.. c:function:: int hwsampler_allocate(unsigned long sdbt, unsigned long sdb)

    allocate memory for the hardware sampler

    :param unsigned long sdbt:
        number of SDBTs per online CPU (must be > 0)

    :param unsigned long sdb:
        number of SDBs per SDBT (minimum 1, maximum 511)

.. _`hwsampler_allocate.description`:

Description
-----------

Returns 0 on success, !0 on failure.

.. _`hwsampler_deallocate`:

hwsampler_deallocate
====================

.. c:function:: int hwsampler_deallocate( void)

    deallocate hardware sampler memory

    :param  void:
        no arguments

.. _`hwsampler_deallocate.description`:

Description
-----------

Returns 0 on success, !0 on failure.

.. _`hwsampler_start_all`:

hwsampler_start_all
===================

.. c:function:: int hwsampler_start_all(unsigned long rate)

    start hardware sampling on all online CPUs

    :param unsigned long rate:
        specifies the used interval when samples are taken

.. _`hwsampler_start_all.description`:

Description
-----------

Returns 0 on success, !0 on failure.

.. _`hwsampler_stop_all`:

hwsampler_stop_all
==================

.. c:function:: int hwsampler_stop_all( void)

    stop hardware sampling on all online CPUs

    :param  void:
        no arguments

.. _`hwsampler_stop_all.description`:

Description
-----------

Returns 0 on success, !0 on failure.

.. This file was automatic generated / don't edit.

