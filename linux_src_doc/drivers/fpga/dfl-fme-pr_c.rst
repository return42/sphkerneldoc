.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl-fme-pr.c

.. _`dfl_fme_create_mgr`:

dfl_fme_create_mgr
==================

.. c:function:: struct platform_device *dfl_fme_create_mgr(struct dfl_feature_platform_data *pdata, struct dfl_feature *feature)

    create fpga mgr platform device as child device

    :param pdata:
        fme platform_device's pdata
    :type pdata: struct dfl_feature_platform_data \*

    :param feature:
        *undescribed*
    :type feature: struct dfl_feature \*

.. _`dfl_fme_create_mgr.return`:

Return
------

mgr platform device if successful, and error code otherwise.

.. _`dfl_fme_destroy_mgr`:

dfl_fme_destroy_mgr
===================

.. c:function:: void dfl_fme_destroy_mgr(struct dfl_feature_platform_data *pdata)

    destroy fpga mgr platform device

    :param pdata:
        fme platform device's pdata
    :type pdata: struct dfl_feature_platform_data \*

.. _`dfl_fme_create_bridge`:

dfl_fme_create_bridge
=====================

.. c:function:: struct dfl_fme_bridge *dfl_fme_create_bridge(struct dfl_feature_platform_data *pdata, int port_id)

    create fme fpga bridge platform device as child

    :param pdata:
        fme platform device's pdata
    :type pdata: struct dfl_feature_platform_data \*

    :param port_id:
        port id for the bridge to be created.
    :type port_id: int

.. _`dfl_fme_create_bridge.return`:

Return
------

bridge platform device if successful, and error code otherwise.

.. _`dfl_fme_destroy_bridge`:

dfl_fme_destroy_bridge
======================

.. c:function:: void dfl_fme_destroy_bridge(struct dfl_fme_bridge *fme_br)

    destroy fpga bridge platform device

    :param fme_br:
        fme bridge to destroy
    :type fme_br: struct dfl_fme_bridge \*

.. _`dfl_fme_destroy_bridges`:

dfl_fme_destroy_bridges
=======================

.. c:function:: void dfl_fme_destroy_bridges(struct dfl_feature_platform_data *pdata)

    destroy all fpga bridge platform device

    :param pdata:
        fme platform device's pdata
    :type pdata: struct dfl_feature_platform_data \*

.. _`dfl_fme_create_region`:

dfl_fme_create_region
=====================

.. c:function:: struct dfl_fme_region *dfl_fme_create_region(struct dfl_feature_platform_data *pdata, struct platform_device *mgr, struct platform_device *br, int port_id)

    create fpga region platform device as child

    :param pdata:
        fme platform device's pdata
    :type pdata: struct dfl_feature_platform_data \*

    :param mgr:
        mgr platform device needed for region
    :type mgr: struct platform_device \*

    :param br:
        br platform device needed for region
    :type br: struct platform_device \*

    :param port_id:
        port id
    :type port_id: int

.. _`dfl_fme_create_region.return`:

Return
------

fme region if successful, and error code otherwise.

.. _`dfl_fme_destroy_region`:

dfl_fme_destroy_region
======================

.. c:function:: void dfl_fme_destroy_region(struct dfl_fme_region *fme_region)

    destroy fme region

    :param fme_region:
        fme region to destroy
    :type fme_region: struct dfl_fme_region \*

.. _`dfl_fme_destroy_regions`:

dfl_fme_destroy_regions
=======================

.. c:function:: void dfl_fme_destroy_regions(struct dfl_feature_platform_data *pdata)

    destroy all fme regions

    :param pdata:
        fme platform device's pdata
    :type pdata: struct dfl_feature_platform_data \*

.. This file was automatic generated / don't edit.

