.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mips-cps.h

.. _`mips_cps_numclusters`:

mips_cps_numclusters
====================

.. c:function:: unsigned int mips_cps_numclusters( void)

    return the number of clusters present in the system

    :param void:
        no arguments
    :type void: 

.. _`mips_cps_numclusters.description`:

Description
-----------

Returns the number of clusters in the system.

.. _`mips_cps_cluster_config`:

mips_cps_cluster_config
=======================

.. c:function:: uint64_t mips_cps_cluster_config(unsigned int cluster)

    return (GCR\|CPC)_CONFIG from a cluster

    :param cluster:
        the ID of the cluster whose config we want
    :type cluster: unsigned int

.. _`mips_cps_cluster_config.description`:

Description
-----------

Read the value of GCR_CONFIG (or its CPC_CONFIG mirror) from a \ ``cluster``\ .

Returns the value of GCR_CONFIG.

.. _`mips_cps_numcores`:

mips_cps_numcores
=================

.. c:function:: unsigned int mips_cps_numcores(unsigned int cluster)

    return the number of cores present in a cluster

    :param cluster:
        the ID of the cluster whose core count we want
    :type cluster: unsigned int

.. _`mips_cps_numcores.description`:

Description
-----------

Returns the value of the PCORES field of the GCR_CONFIG register plus 1, or
zero if no Coherence Manager is present.

.. _`mips_cps_numiocu`:

mips_cps_numiocu
================

.. c:function:: unsigned int mips_cps_numiocu(unsigned int cluster)

    return the number of IOCUs present in a cluster

    :param cluster:
        the ID of the cluster whose IOCU count we want
    :type cluster: unsigned int

.. _`mips_cps_numiocu.description`:

Description
-----------

Returns the value of the NUMIOCU field of the GCR_CONFIG register, or zero
if no Coherence Manager is present.

.. _`mips_cps_numvps`:

mips_cps_numvps
===============

.. c:function:: unsigned int mips_cps_numvps(unsigned int cluster, unsigned int core)

    return the number of VPs (threads) supported by a core

    :param cluster:
        the ID of the cluster containing the core we want to examine
    :type cluster: unsigned int

    :param core:
        the ID of the core whose VP count we want
    :type core: unsigned int

.. _`mips_cps_numvps.description`:

Description
-----------

Returns the number of Virtual Processors (VPs, ie. hardware threads) that
are supported by the given \ ``core``\  in the given \ ``cluster``\ . If the core or the
kernel do not support hardware mutlti-threading this returns 1.

.. This file was automatic generated / don't edit.

